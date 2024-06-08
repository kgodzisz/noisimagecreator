import json
import argparse
from google.cloud import storage
from google.oauth2 import service_account
from vertexai.preview.vision_models import ImageGenerationModel
import vertexai
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import io

class BaseProject:
    def __init__(self, project_id, credentials_path):
        self.project_id = project_id
        self._setup_credentials(credentials_path)

    def _setup_credentials(self, credentials_path):
        with open(credentials_path) as source:
            info = json.load(source)
        self.storage_credentials = service_account.Credentials.from_service_account_info(info)
        self.storage_client = storage.Client(project=self.project_id, credentials=self.storage_credentials)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

class VertexAIProject(BaseProject):
    def __init__(self, project_id, credentials_path, location):
        super().__init__(project_id, credentials_path)
        vertexai.init(project=self.project_id, location=location)
        self.model = ImageGenerationModel.from_pretrained("imagegeneration@005")

    def generate_images(self, prompt, number_of_images, negative_prompt=None, aspect_ratio=None, guidance_scale=None, language=None, seed=None, output_gcs_uri=None, add_watermark=True, safety_filter_level=None):
        for i in range(number_of_images):
            response = self.model.generate_images(prompt=prompt, negative_prompt=negative_prompt, aspect_ratio=aspect_ratio, guidance_scale=guidance_scale, language=language, seed=seed, output_gcs_uri=output_gcs_uri, add_watermark=add_watermark, safety_filter_level=safety_filter_level)
            self._display_image(response.images[0], i)

    def _display_image(self, image, i):
        pil_image = Image.open(io.BytesIO(image._image_bytes))
        np_image = np.array(pil_image)
        plt.imshow(np_image)
        plt.title(f"Generated Image {i+1}")
        plt.show()

class ImageGenerator(VertexAIProject):
    class ArgumentParserError(Exception): 
        pass

    class ThrowingArgumentParser(argparse.ArgumentParser):
        def error(self, message):
            raise ImageGenerator.ArgumentParserError(message)

    def __init__(self, project_id, credentials_path, location):
        super().__init__(project_id, credentials_path, location)

    def parse_arguments(self):
        parser = self.ThrowingArgumentParser(description='Generate images from a prompt.')
        parser.add_argument('prompt', type=str, help='The description of the image to be generated.')
        parser.add_argument('-n', '--number_of_images', type=int, default=1, help='The number of images to be generated.')
        parser.add_argument('-np', '--negative_prompt', type=str, default=None, help='The description of what you do not want to see in the image.')
        parser.add_argument('-ar', '--aspect_ratio', type=str, default=None, help='The aspect ratio of the image.')
        parser.add_argument('-gs', '--guidance_scale', type=float, default=None, help='The scale of guidance, which affects how strictly the model adheres to the prompt.')
        parser.add_argument('-s', '--seed', type=int, default=None, help='The seed for randomness, which affects the results of image generation.')
        parser.add_argument('-o', '--output_gcs_uri', type=str, default=None, help='The URI to save the generated images.')
        parser.add_argument('-aw', '--add_watermark', type=bool, default=False, help='Whether to add a watermark to the generated images.')
        parser.add_argument('-sf', '--safety_filter_level', type=str, default=None, help='The level of the safety filter, which can be one of the following: "block_most", "block_some", "block_few", "block_fewest".')
        return parser.parse_args()

    def run(self):
        try:
            args = self.parse_arguments()
            self.generate_images(args.prompt, args.number_of_images, args.negative_prompt, args.aspect_ratio, args.guidance_scale, args.seed, args.output_gcs_uri, args.add_watermark, args.safety_filter_level)
        except self.ArgumentParserError as e:
            if "the following arguments are required: prompt" in str(e):
                print('You must enter a description of the image you want to generate between the quotation marks. Example: "blue building"')

if __name__ == "__main__":
    config_file = 'config.json'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
        generator = ImageGenerator(config['project_id'], config['credentials_path'], config['location'])
    else:
        project_id = input('Enter project_id: ')
        credentials_path = input('Enter the path to the credentials file: ')
        location = input('Enter the location: ')
        generator = ImageGenerator(project_id, credentials_path, location)
        config = {'project_id': project_id, 'credentials_path': credentials_path, 'location': location}
        with open(config_file, 'w') as f:
            json.dump(config, f)
    generator.run()