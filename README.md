<h1>NoisImageCreator</h1>

<p>Read this in Polish :poland:</p>

<p>NoisImageCreator generates graphic files using VertexAI, available in Google Cloud. Before we run NoisImageCreator on our Google account, we need to create a new project or use an existing one.</p>

<p>Currently, Google allows you to set up a free account, assigning $300 to it. As of today, this is about 1200 PLN to be used for 90 days. To get such an account, it is necessary to confirm with a payment card. However, remember that after 90 days and/or using all the funds, if we do not switch to a paid account, all projects will be deleted. Google, as part of a free trial account, does not charge any fees, even after using up the available funds.</p>

<h2>Creating a new project</h2>
<p>When we have an account, we create a new project and enter it. We need to activate VertexAI to be able to use it. In the upper left corner, next to the Google Cloud logo, we click on the "hamburger" menu. When the list appears, we select "APIs & Services", then "Enabled APIs & Services". After the page loads, roughly in the middle, there will be a link "+ ENABLE APIS AND SERVICES", we click on it. We will be redirected to a page where in the search field we enter "Vertex AI API", we click on the appropriate service. Then on the new page we press the "enable" button. We wait a moment for the service to be launched in our project.</p>

<p>After launching, we go to the main page of our project.</p>

<h2>Generating an access key</h2>
<p>Now we need to generate the appropriate access key, so that we can use VertexAI from the system level. Again, we use the hamburger menu. We go to "APIs & Services" -> "Credentials". At the top, we find the link "+ CREATE CREDENTIALS" and from the drop-down menu we choose "Service account". We provide the name of the service account. Here I entered python-noisimagegenerator, I skipped the description. Then we click on the "CREATE AND CONTINUE" button. We choose "Currently used" -> "Owner" and click the "NEXT" button. In the next two fields, we do not enter anything, just press the "DONE" button.</p>

<p>After performing the above actions, a new item should appear on the list. It is a link, which we enter. At the top there will be a menu, from which we choose "KEYS". We click the "ADD KEY" button and from the list we choose "create new key". A window will appear with the possibility of choosing the type of key. We leave the option marked by default without changes, i.e. we create a key in JSON format and click the "CREATE" button. A security-related message will appear. We familiarize ourselves with it, then click the "CLOSE" button. The key was automatically downloaded to our disk. We move it to the folder where the NoisImageCreator.py program file is located.</p>

<p><strong>Note!</strong> All account data, especially permanently stored in files, should be properly secured. Remember that only the appropriate people should have access to these files.</p>

<h2>Installing Python libraries</h2>
<p>We have prepared the Google Cloud platform to work with our script. Now we need to install the appropriate libraries for Python.</p>

<pre><code>pip3 install json argparse google-cloud-storage google-auth vertex-ai matplotlib Pillow numpy</code></pre>

<h2>First launch</h2>
<p>After all the above preparations, we can proceed to the first launch. We do this using the standard command for running programs in Python:</p>

<pre><code>python3 NoisImageCreator.py</code></pre>

<p>At the first launch, we need to set the data for our project. All this information is included on the main page after entering the project. In the "project information" section, we will need information such as:</p>

<pre><code>Enter project_id:</code></pre>

<p>We provide the project identifier, in my case it is noisimagecreator.</p>

<pre><code>Enter the path to the credentials file:</code></pre>

<p>We provide the path to the key file in JSON format, which we generated some time ago. If you put it in the folder where the program code is located, just enter its name. Otherwise, you need to provide the absolute path to the file.</p>

<code>Enter the location:</code>

<p>In the last initial configuration, we are asked to provide the location of our Google Cloud. In my case, it is us-central1.</p>

<p>After filling in the data, you will receive the information: <code>You must enter a description of the image you want to generate between the quotation marks. Example: "blue building".</code></p>

<p>A config.json configuration file has been generated, with which you will not need to re-enter the above data. In the case of the message we received, for our program to work, we need to write what we want to generate. The simplest way to generate an image is:</p>

<code>python3 NoisImageCreator.py "a desk with coffee, notebook and blue monitor"</code>

<p>This is the simplest solution to create an image from a description. However, the program is more advanced. It has options that allow you to create images according to our requirements.</p>

<p>NOTE! At the moment, the description must be given in English. I am working on the possibility of entering data in other languages.</p>

<p>Here are the options added in the latest version:</p>

<code>-n, --negative_prompt</code> - description of what you don't want to see in the image.
<code>-np, --number_of_images</code> - number of images to generate (default 1).
<code>-ar, --aspect_ratio</code> - image proportions, which can be one of the following: “1:1”, “9:16”.
<code>-gs, --guidance_scale</code> - input scale, which affects how strictly the model adheres to prompts.
<code>-s, --seed</code> - randomness seed, which affects the results of image generation.
<code>-o, --output_gcs_uri</code> - URI to save the generated images.
<code>-aw, --add_watermark</code> - whether to add a watermark to the generated images (default FALSE).
<code>-sf, --safety_filter_level</code> - safety filter level, which can be one of the following: “block_most”, “block_some”, “block_few”, “block_fewest”

<p>Program written with the help of Microsoft Copilot.</p>

<p>In future releases, I plan to add:</p>

<ul>
<li>The ability to enter text to generate in other languages, with an emphasis on Polish.</li>
<li>Improvement of the code in terms of "exceptions".</li>
<li>Creating a Dockerfile to run the program using Docker.</li>
</ul>