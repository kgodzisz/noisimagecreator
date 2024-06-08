<h1>NoisImageCreator</h1>

<p>Read this in <a href="https://github.com/kgodzisz/noisimagecreator/blob/master/README.md">English</a> :uk:</p>

<p>NoisImageCreator generuje pliki graficzne za pomocą VertexAI, udostępnionego w Google Cloud. Nim uruchomimy NoisImageCreator na naszym koncie Google, musimy stworzyć nowy projekt lub skorzystać z już istniejącego.</p>

<p>Obecnie Google umożliwia założenie darmowego konta, przypisując do niego środki w wysokości 300 USD. Na dzień dzisiejszy jest to około 1200 zł do wykorzystania przez 90 dni. Aby uzyskać takie konto, konieczne jest potwierdzenie za pomocą karty płatniczej. Należy jednak pamiętać, że po upłynięciu 90 dni lub/i wykorzystaniu wszystkich środków, jeżeli nie przejdziemy na płatne konto, wszystkie projekty zostaną usunięte. Google, w ramach darmowego konta próbnego, nie pobiera żadnych opłat, nawet po wykorzystaniu dostępnych środków.</p>

<h2>Tworzenie nowego projektu</h2>
<p>Gdy dysponujemy kontem, tworzymy nowy projekt i do niego wchodzimy. Musimy aktywować VertexAi, aby móc z niego skorzystać. W lewym górnym rogu, obok logo Google Cloud, klikamy na menu typu “hamburger”. Po pojawieniu się listy wybieramy "Interfejsy API i usługi", następnie "Włączone interfejsy API i usługi". Po załadowaniu strony, mniej więcej na środku, pojawi się link "+ WŁĄCZ INTERFEJSY API I USŁUGI", klikamy w niego. Zostaniemy przekierowani do strony, gdzie w miejscu umożliwiającym wyszukiwanie wpisujemy "Vertex AI API", klikamy na odpowiednią usługę. Następnie na nowej stronie wciskamy przycisk "włącz". Odczekujemy chwilę, aby usługa została uruchomiona w naszym projekcie.</p>

<p>Po uruchomieniu przechodzimy do strony głównej naszego projektu.</p>

<h2>Generowanie klucza dostępu</h2>
<p>Teraz musimy wygenerować odpowiedni klucz dostępu, tak abyśmy mogli z poziomu systemu korzystać z VertexAI. Ponownie korzystamy z menu typu hamburger. Wchodzimy w "Interfejsy API i usługi" -> "Dane logowania". W górnej części odnajdujemy link "+ UTWÓRZ DANE LOGOWANIA" i z rozwijanego menu wybieramy "Konto usługi". Podajemy nazwę konta usługi. Ja tu wpisałem python-noisimagegenerator, opis pominąłem. Następnie klikamy w przycisk "UTWÓRZ I KONTYNUUJ". Wybieramy "Obecnie używane" -> "Właściciel" i klikamy przycisk "DALEJ". W kolejnych dwóch polach nie wpisujemy nic, tylko wciskamy przycisk "GOTOWE".</p>

<p>Po wykonaniu powyższych czynności, pojawić się powinna nowa pozycja na liście. Jest ona linkiem, w który wchodzimy. W górnej części pojawi się menu, z którego wybieramy "KLUCZE". Klikamy przycisk "DODAJ KLUCZ" i z listy wybieramy "utwórz nowy klucz". Pojawi się okno z możliwością wyboru typu klucza. Pozostawiamy opcję standardowo zaznaczoną bez zmian, czyli tworzymy klucz w formacie JSON i klikamy przycisk "UTWÓRZ". Pojawi się komunikat związany z bezpieczeństwem. Zapoznajemy się z nim, następnie klikamy przycisk "ZAMKNIJ". Klucz automatycznie został pobrany na nasz dysk. Przenosimy go do folderu, w którym znajduje się plik programu NoisImageCreator.py.</p>

<p><strong>Uwaga!</strong> Wszelkie dane do konta, szczególnie trwale umieszczone w plikach, powinny być odpowiednio zabezpieczone. Pamiętaj, aby dostęp do tych plików miały tylko odpowiednie osoby.</p>

<h2>Instalacja bibliotek Python</h2>
<p>Przygotowaliśmy platformę Google Cloud do współpracy z naszym skryptem. Teraz należy zainstalować odpowiednie biblioteki do języka Python.</p>

<pre><code>pip3 install json argparse google-cloud-storage google-auth vertex-ai matplotlib Pillow numpy</code></pre>

<h2>Pierwsze uruchomienie</h2>
<p>Po wszystkich powyższych przygotowaniach możemy przejść do pierwszego uruchomienia. Robimy to za pomocą standardowego polecenia uruchamiania programów w języku python:</p>

<pre><code>python3 NoisImageCreator.py</code></pre>

<p>Przy pierwszym uruchomieniu musimy ustawić dane do naszego projektu. Wszystkie te informacje zawarte są na stronie głównej po wejściu do projektu. W części "informacje o projekcie" potrzebne będą nam informacje takie jak:</p>

<pre><code>Enter project_id:</code></pre>

<p>Podajemy identyfikator projektu, w moim przypadku to noisimagecreator.</p>

<pre><code>Enter the path to the credentials file:</code></pre>

<p>Podajemy ścieżkę do pliku z kluczem w formacie JSON, który wygenerowaliśmy jakąś chwilę temu. Jeśli umieściłeś go w folderze, gdzie znajduje się kod programu, to wystarczy wpisać jego nazwę. W innym wypadku należy podać ścieżkę bezwzględną do pliku.</p>

<code>Enter the location:</code>

<p>W ostatniej wstępnej konfiguracji proszeni jesteśmy o podanie lokalizacji naszej chmury Google. W moim przypadku jest to us-central1.</p>

<p>Po uzupełnieniu danych otrzymasz informację: <code>You must enter a description of the image you want to generate between the quotation marks. Example: "blue building".</code></p>

<p>Został wygenerowany plik konfiguracyjny config.json, za pomocą którego nie będzie konieczności ponownego podawania powyższych danych. W przypadku komunikatu, jaki otrzymaliśmy, aby nasz program zadziałał, musimy napisać, co chcemy wygenerować. Najprostszym sposobem na wygenerowanie obrazu jest:</p>

<code>python3 NoisImageCreator.py "a desk with coffee, notebook and blue monitor"</code>

<p>Jest to najprostsze rozwiązanie pozwalające na stworzenie obrazu z opisu. Jednak program jest bardziej rozbudowany. Posiada opcje umożliwiające stworzenie obrazów według naszych wymagań.</p>

<p>UWAGA! Na obecną chwilę opis musi być podany w języku angielskim. Pracuję nad możliwością wprowadzania danych w innych językach.</p>

<p>Oto opcje dodane w najnowszej wersji:</p>

<code>-n, --negative_prompt</code> - opis tego, czego nie chcesz widzieć na obrazie.
<code>-np, --number_of_images</code> - liczba obrazów do wygenerowania (domyślnie 1).
<code>-ar, --aspect_ratio</code> - proporcje obrazu, które mogą być jednym z następujących: “1:1”, “9:16”.
<code>-gs, --guidance_scale</code> - skala wprowadzania, która wpływa na to, jak ściśle model przestrzega podpowiedzi.
<code>-s, --seed</code> - ziarno losowości, które wpływa na wyniki generowania obrazów.
<code>-o, --output_gcs_uri</code> - URI do zapisania wygenerowanych obrazów.
<code>-aw, --add_watermark</code> - czy dodać znak wodny do wygenerowanych obrazów (domyślnie FALSE).
<code>-sf, --safety_filter_level</code> - poziom filtru bezpieczeństwa, który może być jednym z następujących: “block_most”, “block_some”, “block_few”, “block_fewest”

<p>Program napisany z pomocą Microsoft Copilot.</p>

<p>W przyszłych wydaniach planuję dodać:</p>

<ul>
<li>Możliwość wprowadzania tekstu do generowania w innych językach, z naciskiem na język Polski.</li>
<li>Poprawa kodu pod względem “wyjątków”.</li>
<li>Stworzenie Dockerfile umożliwiającym uruchomienie programu za pomocą Dockera.</li>
</ul>
