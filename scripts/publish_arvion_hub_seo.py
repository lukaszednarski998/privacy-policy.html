#!/usr/bin/env python3
"""Build useful, static ARVION Hub pages; preserve unrelated site content.
Source of product capabilities: ARVION-WATCH-MEDIA-HUB-PRIVACY.html.
No fabricated ratings, price, downloads, codecs or universal compatibility.
"""
from __future__ import annotations
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://lukaszednarski998.github.io/privacy-policy.html/'
PLAY = 'https://play.google.com/store/apps/details?id=pl.arvion.watchmediahub'
LOCALES = [('en','English'),('pl','Polski'),('de','Deutsch'),('fr','Français'),('es','Español'),('it','Italiano'),('pt-BR','Português (Brasil)'),('ja','日本語'),('ko','한국어'),('zh-CN','简体中文'),('tr','Türkçe'),('id','Bahasa Indonesia'),('ru','Русский'),('uk','Українська')]
D = {}
def add(lang, title, description, intro, sections, questions, labels):
    D[lang] = dict(title=title, description=description, intro=intro, sections=sections, questions=questions, labels=labels)

add('en', 'ARVION Hub: Music, Video, Camera & Files for Wear OS',
'Transfer music, videos and files between Android and Wear OS. Explore ARVION Hub camera preview, local browser sharing and phone-to-watch connections.',
'Bring your Android phone and compatible Wear OS smartwatch together. ARVION Hub combines MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, file management and local browser sharing. Move your own media between devices, play supported files and view your phone camera from your watch.',
[
('Music on your watch — MUSIC 2 WATCH', 'Transfer selected audio files from your Android phone to a compatible Wear OS watch. Keep your own music and recordings in a local library and play supported files on the receiving device. Prepare the audio you need before a walk, a workout or a journey. File playback depends on the format and device capabilities.'),
('Transfer and watch videos — VIDEO 2 WATCH', 'Send your own videos and personal recordings to your smartwatch and play compatible files on its display. Transferring a file and decoding its contents are different operations: the video format, codecs, available storage and receiving hardware affect playback. The app does not supply movies or subscription content.'),
('Phone camera preview — CAM 2 WATCH', 'View the phone camera through a supported live connection. Use a wrist-worn preview when checking the framing of your phone camera. Camera, microphone and recording features require the relevant permissions and a user-initiated session. Live preview needs an active connection; it is not unlimited remote access to any camera.'),
('Files and Browser Share', 'Browse, select, manage, send and receive user-selected media and files. Local browser sharing offers another way to access supported content from a compatible device on the same network. Keep the sharing session active while using it. Connect only to trusted devices and do not publish local pairing addresses or QR codes.'),
('How to connect your phone and watch', 'Install the appropriate Android and Wear OS components, open them on both devices and grant permissions for the feature you want to use. Pair the devices using an available method, then select music, video, files or the camera module. Supported connections may include local Wi-Fi/LAN, Bluetooth, Wi-Fi Direct and QR pairing information, depending on the module and hardware. A QR code exchanges connection details; it does not replace the network connection.'),
('Compatibility, privacy and purchase', 'The watch component requires a compatible Wear OS smartwatch. Check Google Play for your device and country before installation. Local transfers do not require uploading your media to a developer-operated cloud. ARVION Watch Media Hub uses a 60-minute trial and a one-time full-version purchase, without ads or recurring subscriptions. The applicable purchase terms are shown in Google Play.')
], [
('Can I listen to music or watch videos offline?', 'Supported files already stored on the watch can be used for local playback. Transferring new files, browser sharing and live camera preview require an appropriate connection. Installation and purchase verification may need internet access.'),
('Does it work with every smartwatch?', 'No. The watch component is designed for compatible Wear OS devices. Do not assume that an Apple Watch or a smartwatch using another operating system can run it. Check the compatibility shown by Google Play.'),
('Why does a transferred video not play?', 'Successful transfer does not guarantee decoding support. Check the file format, audio and video codecs, available storage and receiving device capabilities. Try a compatible file before transferring a large library.'),
('Can a computer use Browser Share?', 'A compatible browser on the local network can use the supported browser-sharing workflow. This does not mean that every computer, television or browser supports all media formats, nor that a native app is available for every operating system.')
], ['OPEN IN GOOGLE PLAY','Home','All apps','Privacy policy','Frequently asked questions','Explore ARVION Hub','Android + Wear OS','Product information'])

add('pl', 'ARVION Hub: muzyka, filmy, kamera i pliki na Wear OS',
'Przesyłaj muzykę, filmy i pliki z Androida na Wear OS. ARVION Hub łączy podgląd kamery telefonu, udostępnianie w przeglądarce i połączenia lokalne.',
'Połącz telefon z Androidem i zgodny zegarek Wear OS w jednym centrum multimediów. ARVION Hub łączy MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, zarządzanie plikami oraz lokalne udostępnianie w przeglądarce. Przesyłaj własne materiały, odtwarzaj obsługiwane pliki i oglądaj obraz z kamery telefonu na nadgarstku.',
[
('Muzyka na zegarku — MUSIC 2 WATCH', 'Przesyłaj wybrane pliki audio z telefonu z Androidem na zgodny smartwatch Wear OS. Korzystaj z własnej muzyki i nagrań zapisanych lokalnie oraz odtwarzaj obsługiwane pliki na urządzeniu odbiorczym. Przygotuj nagrania przed spacerem, treningiem lub podróżą. Obsługa odtwarzania zależy od formatu pliku i możliwości urządzenia.'),
('Przesyłanie i odtwarzanie filmów — VIDEO 2 WATCH', 'Wyślij własne filmy i nagrania na zegarek, aby oglądać zgodne materiały na jego ekranie. Przesłanie pliku nie jest tym samym co obsługa jego odtwarzania: znaczenie mają format, kodeki, wolna pamięć i możliwości sprzętu. Aplikacja nie dostarcza filmów ani dostępu do płatnych serwisów.'),
('Podgląd kamery telefonu — CAM 2 WATCH', 'Oglądaj obraz z kamery telefonu przez obsługiwane połączenie na żywo. Podgląd na nadgarstku przydaje się podczas sprawdzania kadru telefonu. Kamera, mikrofon i nagrywanie wymagają odpowiednich uprawnień oraz uruchomienia funkcji przez użytkownika. Potrzebne jest aktywne połączenie; nie jest to nieograniczony dostęp do dowolnej kamery przez internet.'),
('Pliki i udostępnianie w przeglądarce', 'Przeglądaj, wybieraj, porządkuj, wysyłaj i odbieraj własne multimedia oraz pliki. Browser Share umożliwia lokalne udostępnianie obsługiwanych treści zgodnym urządzeniom w tej samej sieci. Sesja udostępniania musi pozostać aktywna. Łącz się wyłącznie z zaufanymi urządzeniami i nie publikuj adresów ani kodów QR służących do parowania.'),
('Jak połączyć telefon z zegarkiem?', 'Zainstaluj odpowiednie komponenty na Androidzie i Wear OS, uruchom je na obu urządzeniach i nadaj uprawnienia potrzebne do wybranej funkcji. Sparuj urządzenia dostępną metodą, a następnie wybierz muzykę, filmy, pliki lub kamerę. Zależnie od modułu i sprzętu dostępne mogą być Wi-Fi/LAN, Bluetooth, Wi-Fi Direct oraz informacje do parowania w kodzie QR. Kod QR przekazuje dane połączenia — nie zastępuje sieci.'),
('Zgodność, prywatność i zakup', 'Komponent zegarkowy wymaga zgodnego smartwatcha Wear OS. Przed instalacją sprawdź dostępność dla urządzenia i kraju w Google Play. Lokalne transfery nie wymagają wysyłania multimediów do chmury dewelopera. ARVION Watch Media Hub oferuje 60-minutowy trial i jednorazowy zakup pełnej wersji, bez reklam i cyklicznych subskrypcji. Obowiązujące warunki zakupu zobaczysz w Google Play.')
], [
('Czy muzyka i filmy działają offline?', 'Obsługiwane pliki zapisane już na zegarku można odtwarzać lokalnie. Transfer nowych plików, udostępnianie w przeglądarce i podgląd kamery wymagają odpowiedniego połączenia. Instalacja i weryfikacja zakupu mogą wymagać internetu.'),
('Czy aplikacja działa na każdym smartwatchu?', 'Nie. Część zegarkowa jest przeznaczona dla zgodnych urządzeń Wear OS. Nie należy zakładać obsługi Apple Watch ani zegarków z innymi systemami. Zgodność konkretnego modelu sprawdź w Google Play.'),
('Dlaczego przesłany film się nie odtwarza?', 'Udany transfer nie gwarantuje obsługi formatu. Sprawdź kodeki obrazu i dźwięku, wolną pamięć oraz możliwości urządzenia. Przed wysłaniem dużej biblioteki przetestuj zgodny plik.'),
('Czy mogę korzystać z Browser Share na komputerze?', 'Obsługiwany sposób udostępniania działa w zgodnej przeglądarce w sieci lokalnej. Nie oznacza to obsługi wszystkich formatów przez każdy komputer i telewizor ani dostępności natywnej aplikacji na każdy system.')
], ['OTWÓRZ W GOOGLE PLAY','Strona główna','Wszystkie aplikacje','Polityka prywatności','Najczęstsze pytania','Poznaj ARVION Hub','Android + Wear OS','Informacje o aplikacji'])

add('de', 'ARVION Hub: Musik, Videos, Kamera und Dateien für Wear OS',
'Musik, Videos und Dateien zwischen Android und Wear OS übertragen. ARVION Hub mit Kameravorschau, lokaler Browserfreigabe und Geräteverbindung.',
'Verbinde dein Android-Smartphone mit einer kompatiblen Wear-OS-Smartwatch. ARVION Hub vereint MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, Dateiverwaltung und lokale Browserfreigabe. Übertrage eigene Medien, spiele unterstützte Dateien ab und sieh das Kamerabild deines Smartphones auf der Uhr.',
[
('Musik auf der Uhr — MUSIC 2 WATCH','Übertrage ausgewählte Audiodateien vom Android-Smartphone auf eine kompatible Wear-OS-Uhr. Nutze eigene Musik und Aufnahmen aus dem lokalen Speicher, etwa beim Spaziergang oder auf Reisen. Die Wiedergabe hängt vom Dateiformat und vom Empfangsgerät ab.'),
('Videos übertragen — VIDEO 2 WATCH','Sende eigene Videos an deine Smartwatch und spiele kompatible Dateien auf ihrem Display ab. Eine erfolgreiche Übertragung garantiert keine Unterstützung aller Audio- und Videocodecs. Speicherplatz und Hardware beeinflussen die Wiedergabe. Die App stellt keine Filme oder Abonnementinhalte bereit.'),
('Kameravorschau — CAM 2 WATCH','Sieh das Bild der Smartphone-Kamera über eine unterstützte Live-Verbindung auf der Uhr. Kamera, Mikrofon und Aufnahme benötigen passende Berechtigungen und eine vom Nutzer gestartete Sitzung. Die Vorschau erfordert eine aktive Verbindung und bietet keinen unbegrenzten Fernzugriff.'),
('Dateien und Browser Share','Wähle, verwalte, sende und empfange eigene Dateien und Medien. Die lokale Browserfreigabe ermöglicht den Zugriff auf unterstützte Inhalte über einen kompatiblen Browser im selben Netzwerk. Halte die Sitzung aktiv und teile Verbindungsdaten nur mit vertrauenswürdigen Geräten.'),
('Smartphone und Uhr verbinden','Installiere die passenden Android- und Wear-OS-Komponenten, öffne sie auf beiden Geräten und erteile die benötigten Berechtigungen. Kopple die Geräte mit einer verfügbaren Methode und wähle ein Modul. Je nach Hardware und Funktion kommen WLAN/LAN, Bluetooth, Wi-Fi Direct oder QR-Kopplungsdaten infrage. Ein QR-Code ersetzt keine Netzwerkverbindung.'),
('Kompatibilität und Kauf','Prüfe Gerätekompatibilität und Verfügbarkeit bei Google Play. Lokale Übertragungen erfordern keinen Upload deiner Medien in eine Entwickler-Cloud. ARVION Watch Media Hub bietet eine 60-minütige Testphase und einen einmaligen Kauf der Vollversion, ohne Werbung oder wiederkehrendes Abonnement. Es gelten die in Google Play angezeigten Kaufbedingungen.')
], [
('Kann ich Medien offline abspielen?','Unterstützte Dateien im lokalen Speicher der Uhr lassen sich lokal abspielen. Neue Übertragungen, Browserfreigabe und Live-Kameravorschau benötigen die passende Verbindung.'),
('Funktioniert jede Smartwatch?','Nein. Die Uhrenkomponente erfordert ein kompatibles Wear-OS-Gerät. Gehe nicht von einer Unterstützung für Apple Watch oder andere Betriebssysteme aus.'),
('Warum wird ein übertragenes Video nicht abgespielt?','Übertragung und Decodierung sind unterschiedliche Vorgänge. Prüfe Format, Codecs, Speicherplatz und die Fähigkeiten des Empfangsgeräts.')
], ['IN GOOGLE PLAY ÖFFNEN','Startseite','Alle Apps','Datenschutz','Häufige Fragen','ARVION Hub entdecken','Android + Wear OS','Produktinformationen'])

add('fr', 'ARVION Hub : musique, vidéos, caméra et fichiers sur Wear OS',
'Transférez musique, vidéos et fichiers entre Android et Wear OS. Découvrez ARVION Hub, aperçu caméra et partage local dans le navigateur.',
'Connectez votre téléphone Android à une montre Wear OS compatible. ARVION Hub réunit MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, gestion de fichiers et partage local dans le navigateur. Transférez vos propres médias, lisez les fichiers pris en charge et consultez la caméra du téléphone au poignet.',
[
('Musique sur la montre — MUSIC 2 WATCH','Transférez des fichiers audio sélectionnés depuis Android vers une montre Wear OS compatible. Retrouvez votre musique et vos enregistrements dans une bibliothèque locale, pour une promenade ou un voyage. La lecture dépend du format et des capacités de l’appareil récepteur.'),
('Vidéos sur Wear OS — VIDEO 2 WATCH','Envoyez vos vidéos personnelles vers la montre et lisez les fichiers compatibles sur son écran. Un transfert réussi ne garantit pas la prise en charge de tous les codecs audio et vidéo. Le stockage et le matériel influencent la lecture. L’application ne fournit ni films ni contenus sur abonnement.'),
('Aperçu de la caméra — CAM 2 WATCH','Affichez la caméra du téléphone sur la montre grâce à une connexion en direct prise en charge. Caméra, microphone et enregistrement nécessitent les autorisations correspondantes et une session lancée par l’utilisateur. L’aperçu exige une connexion active, sans accès distant illimité.'),
('Fichiers et Browser Share','Parcourez, sélectionnez, organisez, envoyez et recevez vos médias et fichiers. Le partage local permet d’accéder aux contenus pris en charge depuis un navigateur compatible sur le même réseau. Gardez la session active et ne partagez les informations de connexion qu’avec des appareils de confiance.'),
('Connecter téléphone et montre','Installez les composants Android et Wear OS adaptés, ouvrez-les sur les deux appareils et accordez les autorisations nécessaires. Associez les appareils, puis choisissez un module. Selon le matériel et la fonction, les méthodes peuvent inclure Wi-Fi/LAN, Bluetooth, Wi-Fi Direct et informations d’association par QR. Un code QR ne remplace pas la connexion réseau.'),
('Compatibilité et achat','Vérifiez la compatibilité et la disponibilité dans Google Play. Les transferts locaux n’exigent pas d’envoyer vos médias vers un cloud du développeur. ARVION Watch Media Hub propose un essai de 60 minutes et un achat unique de la version complète, sans publicité ni abonnement récurrent. Les conditions applicables figurent dans Google Play.')
], [
('Puis-je lire des médias hors connexion ?','Les fichiers compatibles déjà stockés sur la montre peuvent être lus localement. Transfert, partage dans le navigateur et aperçu caméra nécessitent une connexion adaptée.'),
('Toutes les montres sont-elles compatibles ?','Non. Le composant pour montre nécessite un appareil Wear OS compatible. Ne supposez pas une prise en charge d’Apple Watch ou d’autres systèmes.'),
('Pourquoi une vidéo transférée ne se lit-elle pas ?','Le transfert et le décodage sont distincts. Vérifiez le format, les codecs, l’espace disponible et les capacités de l’appareil récepteur.')
], ['OUVRIR DANS GOOGLE PLAY','Accueil','Toutes les applications','Confidentialité','Questions fréquentes','Découvrir ARVION Hub','Android + Wear OS','Informations sur l’application'])

add('es', 'ARVION Hub: música, vídeos, cámara y archivos para Wear OS',
'Transfiere música, vídeos y archivos entre Android y Wear OS. ARVION Hub incluye vista de cámara y uso compartido local mediante navegador.',
'Conecta tu teléfono Android con un reloj Wear OS compatible. ARVION Hub reúne MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, gestión de archivos y uso compartido local en el navegador. Transfiere tus propios contenidos, reproduce archivos compatibles y consulta la cámara del teléfono desde la muñeca.',
[
('Música en el reloj — MUSIC 2 WATCH','Transfiere archivos de audio seleccionados desde Android a un reloj Wear OS compatible. Lleva tu música y grabaciones en una biblioteca local para paseos o viajes. La reproducción depende del formato y de las capacidades del dispositivo receptor.'),
('Vídeos en Wear OS — VIDEO 2 WATCH','Envía vídeos personales al reloj y reproduce archivos compatibles en su pantalla. Transferir un archivo correctamente no garantiza que se admitan todos los códecs de audio y vídeo. El almacenamiento y el hardware influyen en la reproducción. La aplicación no proporciona películas ni contenido de suscripción.'),
('Vista de cámara — CAM 2 WATCH','Consulta la cámara del teléfono en el reloj mediante una conexión en directo compatible. La cámara, el micrófono y la grabación necesitan los permisos correspondientes y una sesión iniciada por el usuario. La vista previa requiere una conexión activa y no ofrece acceso remoto ilimitado.'),
('Archivos y Browser Share','Explora, selecciona, organiza, envía y recibe tus archivos y contenidos multimedia. El uso compartido local permite acceder a contenidos compatibles desde un navegador adecuado en la misma red. Mantén activa la sesión y comparte los datos de conexión solo con dispositivos de confianza.'),
('Conectar el teléfono y el reloj','Instala los componentes adecuados para Android y Wear OS, ábrelos en ambos dispositivos y concede los permisos necesarios. Vincula los dispositivos y elige un módulo. Según la función y el hardware, pueden estar disponibles Wi-Fi/LAN, Bluetooth, Wi-Fi Direct y datos de vinculación mediante QR. El código QR no sustituye la conexión de red.'),
('Compatibilidad y compra','Comprueba la compatibilidad y disponibilidad en Google Play. Las transferencias locales no requieren subir tus archivos a una nube del desarrollador. ARVION Watch Media Hub ofrece una prueba de 60 minutos y una compra única de la versión completa, sin anuncios ni suscripciones recurrentes. Consulta las condiciones vigentes en Google Play.')
], [
('¿Puedo reproducir contenido sin internet?','Los archivos compatibles ya guardados en el reloj pueden reproducirse localmente. Las transferencias, el navegador compartido y la cámara en directo necesitan una conexión adecuada.'),
('¿Funciona en todos los relojes?','No. El componente del reloj requiere un dispositivo Wear OS compatible. No supongas compatibilidad con Apple Watch ni con otros sistemas.'),
('¿Por qué no se reproduce un vídeo transferido?','Transferir y decodificar son procesos distintos. Revisa el formato, los códecs, el espacio disponible y las capacidades del dispositivo receptor.')
], ['ABRIR EN GOOGLE PLAY','Inicio','Todas las aplicaciones','Privacidad','Preguntas frecuentes','Descubre ARVION Hub','Android + Wear OS','Información de la aplicación'])

add('it', 'ARVION Hub: musica, video, fotocamera e file per Wear OS',
'Trasferisci musica, video e file tra Android e Wear OS. Scopri ARVION Hub con anteprima fotocamera e condivisione locale tramite browser.',
'Collega il telefono Android a uno smartwatch Wear OS compatibile. ARVION Hub riunisce MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, gestione file e condivisione locale nel browser. Trasferisci i tuoi contenuti, riproduci file supportati e guarda la fotocamera del telefono dal polso.',
[
('Musica sull’orologio — MUSIC 2 WATCH','Trasferisci file audio selezionati da Android a un orologio Wear OS compatibile. Porta musica e registrazioni personali in una libreria locale, per passeggiate o viaggi. La riproduzione dipende dal formato e dalle capacità del dispositivo ricevente.'),
('Video su Wear OS — VIDEO 2 WATCH','Invia video personali all’orologio e riproduci i file compatibili sul display. Il trasferimento riuscito non garantisce il supporto di tutti i codec audio e video. Memoria e hardware influenzano la riproduzione. L’app non fornisce film né contenuti in abbonamento.'),
('Anteprima fotocamera — CAM 2 WATCH','Visualizza la fotocamera del telefono sull’orologio tramite una connessione in diretta supportata. Fotocamera, microfono e registrazione richiedono le autorizzazioni appropriate e una sessione avviata dall’utente. L’anteprima necessita di una connessione attiva e non offre accesso remoto illimitato.'),
('File e Browser Share','Sfoglia, seleziona, organizza, invia e ricevi file e contenuti personali. La condivisione locale consente l’accesso ai contenuti supportati da un browser compatibile sulla stessa rete. Mantieni attiva la sessione e condividi i dati di collegamento solo con dispositivi fidati.'),
('Collegare telefono e orologio','Installa i componenti Android e Wear OS appropriati, aprili su entrambi i dispositivi e concedi le autorizzazioni necessarie. Associa i dispositivi e scegli un modulo. A seconda di hardware e funzione, possono essere disponibili Wi-Fi/LAN, Bluetooth, Wi-Fi Direct e dati di associazione QR. Il codice QR non sostituisce la connessione di rete.'),
('Compatibilità e acquisto','Verifica compatibilità e disponibilità su Google Play. I trasferimenti locali non richiedono di caricare i contenuti su un cloud dello sviluppatore. ARVION Watch Media Hub offre una prova di 60 minuti e un acquisto una tantum della versione completa, senza pubblicità o abbonamenti ricorrenti. Le condizioni applicabili sono mostrate su Google Play.')
], [
('Posso riprodurre contenuti offline?','I file supportati già salvati sull’orologio possono essere riprodotti localmente. Trasferimenti, condivisione nel browser e anteprima in diretta richiedono una connessione adatta.'),
('Funziona su ogni smartwatch?','No. Il componente per orologio richiede un dispositivo Wear OS compatibile. Non dare per scontato il supporto di Apple Watch o di altri sistemi.'),
('Perché un video trasferito non viene riprodotto?','Trasferimento e decodifica sono operazioni distinte. Controlla formato, codec, spazio libero e capacità del dispositivo ricevente.')
], ['APRI IN GOOGLE PLAY','Pagina iniziale','Tutte le app','Privacy','Domande frequenti','Scopri ARVION Hub','Android + Wear OS','Informazioni sull’app'])

add('pt-BR', 'ARVION Hub: músicas, vídeos, câmera e arquivos no Wear OS',
'Transfira músicas, vídeos e arquivos entre Android e Wear OS. Conheça o ARVION Hub, a prévia da câmera e o compartilhamento local pelo navegador.',
'Conecte seu celular Android a um relógio Wear OS compatível. O ARVION Hub reúne MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, gerenciamento de arquivos e compartilhamento local pelo navegador. Transfira seus conteúdos, reproduza arquivos compatíveis e veja a câmera do celular no pulso.',
[
('Música no relógio — MUSIC 2 WATCH','Transfira arquivos de áudio selecionados do Android para um relógio Wear OS compatível. Leve suas músicas e gravações em uma biblioteca local, para caminhadas ou viagens. A reprodução depende do formato e dos recursos do aparelho receptor.'),
('Vídeos no Wear OS — VIDEO 2 WATCH','Envie vídeos pessoais ao relógio e reproduza arquivos compatíveis na tela. Uma transferência bem-sucedida não garante suporte a todos os codecs de áudio e vídeo. Armazenamento e hardware afetam a reprodução. O aplicativo não fornece filmes nem conteúdo por assinatura.'),
('Prévia da câmera — CAM 2 WATCH','Veja a câmera do celular no relógio por uma conexão ao vivo compatível. Câmera, microfone e gravação exigem as permissões correspondentes e uma sessão iniciada pelo usuário. A prévia precisa de conexão ativa e não oferece acesso remoto ilimitado.'),
('Arquivos e Browser Share','Navegue, selecione, organize, envie e receba seus arquivos e mídias. O compartilhamento local permite acessar conteúdos compatíveis em um navegador adequado na mesma rede. Mantenha a sessão ativa e compartilhe os dados de conexão apenas com aparelhos confiáveis.'),
('Conectar celular e relógio','Instale os componentes Android e Wear OS adequados, abra-os nos dois aparelhos e conceda as permissões necessárias. Faça o pareamento e escolha um módulo. Dependendo do hardware e da função, podem estar disponíveis Wi-Fi/LAN, Bluetooth, Wi-Fi Direct e dados de pareamento por QR. O código QR não substitui a conexão de rede.'),
('Compatibilidade e compra','Confira a compatibilidade e a disponibilidade no Google Play. Transferências locais não exigem enviar suas mídias para uma nuvem do desenvolvedor. O ARVION Watch Media Hub oferece teste de 60 minutos e compra única da versão completa, sem anúncios nem assinaturas recorrentes. As condições aplicáveis aparecem no Google Play.')
], [
('Posso reproduzir conteúdo offline?','Arquivos compatíveis já salvos no relógio podem ser reproduzidos localmente. Transferências, compartilhamento no navegador e câmera ao vivo precisam da conexão adequada.'),
('Funciona em qualquer smartwatch?','Não. O componente do relógio exige um dispositivo Wear OS compatível. Não presuma suporte ao Apple Watch ou a outros sistemas.'),
('Por que um vídeo transferido não reproduz?','Transferir e decodificar são operações distintas. Verifique o formato, os codecs, o espaço livre e os recursos do aparelho receptor.')
], ['ABRIR NO GOOGLE PLAY','Início','Todos os aplicativos','Privacidade','Perguntas frequentes','Conheça o ARVION Hub','Android + Wear OS','Informações do aplicativo'])

add('ja', 'ARVION Hub：Wear OSへ音楽・動画・ファイルを転送',
'AndroidとWear OSの間で音楽、動画、ファイルを転送。ARVION Hubのスマートフォンカメラプレビューとローカルブラウザ共有を紹介します。',
'Androidスマートフォンと対応するWear OSスマートウォッチを接続。ARVION HubはMUSIC 2 WATCH、VIDEO 2 WATCH、CAM 2 WATCH、ファイル管理、ローカルブラウザ共有をまとめたアプリです。自分のメディアを転送し、対応ファイルを再生し、スマートフォンのカメラ映像を手元で確認できます。',
[
('ウォッチで音楽 — MUSIC 2 WATCH','選択した音声ファイルをAndroidから対応するWear OSウォッチへ転送します。自分の音楽や録音をローカルライブラリに保存して、散歩や旅行に備えられます。再生できるかどうかは、ファイル形式と受信側の端末の性能によって異なります。'),
('動画を転送 — VIDEO 2 WATCH','自分で用意した動画をウォッチへ送り、対応するファイルを画面で再生します。転送が成功しても、すべての音声・動画コーデックを再生できるとは限りません。空き容量やハードウェアにも依存します。映画や有料サービスのコンテンツは付属しません。'),
('カメラプレビュー — CAM 2 WATCH','対応するライブ接続でスマートフォンのカメラ映像をウォッチに表示します。カメラ、マイク、録画には、必要な権限とユーザーが開始したセッションが必要です。プレビューには接続を維持する必要があり、無制限の遠隔アクセスを提供するものではありません。'),
('ファイルとBrowser Share','自分のメディアやファイルを閲覧、選択、整理、送受信します。ローカル共有では、同じネットワーク上の対応ブラウザからサポート対象のコンテンツにアクセスできます。利用中は共有セッションを有効にし、接続情報は信頼できる端末とのみ共有してください。'),
('スマートフォンとウォッチの接続','対応するAndroid版とWear OS版をインストールし、両端末で開いて必要な権限を許可します。利用可能な方法でペアリングして、使いたい機能を選択します。機能やハードウェアにより、Wi-Fi/LAN、Bluetooth、Wi-Fi Direct、QRペアリング情報などを利用します。QRコード自体がネットワーク接続の代わりになるわけではありません。'),
('対応機種と購入','Google Playで端末の互換性と提供状況を確認してください。ローカル転送では、開発者のクラウドへメディアをアップロードする必要はありません。ARVION Watch Media Hubには60分間の試用と完全版の買い切り購入があり、広告や継続的なサブスクリプションはありません。適用される購入条件はGoogle Playに表示されます。')
], [
('オフラインで再生できますか？','ウォッチに保存済みの対応ファイルはローカルで再生できます。新しいファイルの転送、ブラウザ共有、ライブカメラプレビューには適切な接続が必要です。'),
('すべてのスマートウォッチに対応していますか？','いいえ。ウォッチ側には対応するWear OS端末が必要です。Apple Watchや他のOSを搭載したウォッチへの対応を前提にしないでください。'),
('転送した動画を再生できないのはなぜですか？','転送とデコードは別の処理です。形式、コーデック、空き容量、受信端末の対応状況を確認してください。')
], ['GOOGLE PLAYで開く','ホーム','すべてのアプリ','プライバシーポリシー','よくある質問','ARVION Hubを見る','Android + Wear OS','アプリ情報'])

add('ko', 'ARVION Hub: Wear OS 음악·동영상·카메라·파일',
'Android와 Wear OS 사이에서 음악, 동영상, 파일을 전송하세요. ARVION Hub의 휴대전화 카메라 미리보기와 로컬 브라우저 공유를 알아보세요.',
'Android 휴대전화를 호환되는 Wear OS 스마트워치와 연결하세요. ARVION Hub는 MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, 파일 관리와 로컬 브라우저 공유를 한곳에 제공합니다. 개인 미디어를 전송하고 지원 파일을 재생하며 손목에서 휴대전화 카메라 화면을 확인할 수 있습니다.',
[
('워치에서 음악 듣기 — MUSIC 2 WATCH','선택한 오디오 파일을 Android 휴대전화에서 호환 Wear OS 워치로 전송하세요. 음악과 녹음 파일을 로컬 라이브러리에 준비해 산책이나 여행에 활용할 수 있습니다. 재생 가능 여부는 파일 형식과 수신 기기의 기능에 따라 달라집니다.'),
('동영상 전송 — VIDEO 2 WATCH','개인 동영상을 워치로 보내고 호환되는 파일을 화면에서 재생하세요. 전송 성공이 모든 오디오·비디오 코덱의 지원을 보장하지는 않습니다. 저장 공간과 하드웨어도 재생에 영향을 줍니다. 앱은 영화나 유료 구독 콘텐츠를 제공하지 않습니다.'),
('카메라 미리보기 — CAM 2 WATCH','지원되는 실시간 연결을 통해 휴대전화 카메라 화면을 워치에서 확인하세요. 카메라, 마이크, 녹화에는 관련 권한과 사용자가 시작한 세션이 필요합니다. 미리보기에는 활성 연결이 필요하며 무제한 원격 접근을 제공하는 기능이 아닙니다.'),
('파일과 Browser Share','개인 파일과 미디어를 탐색하고 선택·정리·송수신하세요. 로컬 공유를 사용하면 같은 네트워크의 호환 브라우저에서 지원되는 콘텐츠에 접근할 수 있습니다. 공유 세션을 유지하고 연결 정보는 신뢰하는 기기와만 공유하세요.'),
('휴대전화와 워치 연결','적절한 Android 및 Wear OS 구성 요소를 설치하고 두 기기에서 실행한 다음 필요한 권한을 허용하세요. 사용 가능한 방법으로 페어링하고 원하는 모듈을 선택하세요. 기능과 하드웨어에 따라 Wi-Fi/LAN, Bluetooth, Wi-Fi Direct 및 QR 페어링 정보를 사용할 수 있습니다. QR 코드가 네트워크 연결을 대신하는 것은 아닙니다.'),
('호환성과 구매','Google Play에서 기기 호환성과 제공 여부를 확인하세요. 로컬 전송을 위해 미디어를 개발자 클라우드에 업로드할 필요는 없습니다. ARVION Watch Media Hub는 60분 체험과 정식 버전 일회성 구매를 제공하며 광고나 반복 구독은 없습니다. 적용되는 구매 조건은 Google Play에 표시됩니다.')
], [
('오프라인 재생이 가능한가요?','워치에 이미 저장된 지원 파일은 로컬로 재생할 수 있습니다. 새 파일 전송, 브라우저 공유, 실시간 카메라 미리보기에는 적절한 연결이 필요합니다.'),
('모든 스마트워치에서 작동하나요?','아니요. 워치 구성 요소는 호환되는 Wear OS 기기가 필요합니다. Apple Watch나 다른 운영체제의 지원을 전제로 하지 마세요.'),
('전송한 동영상이 재생되지 않는 이유는 무엇인가요?','전송과 디코딩은 별개입니다. 파일 형식, 코덱, 여유 저장 공간, 수신 기기의 지원 범위를 확인하세요.')
], ['GOOGLE PLAY에서 열기','홈','모든 앱','개인정보 처리방침','자주 묻는 질문','ARVION Hub 알아보기','Android + Wear OS','앱 정보'])

add('zh-CN', 'ARVION Hub：Wear OS 音乐、视频、相机与文件传输',
'在 Android 和 Wear OS 之间传输音乐、视频和文件。了解 ARVION Hub 的手机相机预览、本地浏览器共享及设备连接功能。',
'将 Android 手机与兼容的 Wear OS 智能手表连接起来。ARVION Hub 集成 MUSIC 2 WATCH、VIDEO 2 WATCH、CAM 2 WATCH、文件管理和本地浏览器共享。传输自己的媒体文件，播放受支持的内容，并在手腕上查看手机相机画面。',
[
('在手表上听音乐 — MUSIC 2 WATCH','将选定的音频文件从 Android 手机传输到兼容的 Wear OS 手表。在本地媒体库中准备自己的音乐和录音，方便散步或旅行时使用。能否播放取决于文件格式及接收设备的能力。'),
('传输视频 — VIDEO 2 WATCH','将个人视频发送到手表，在屏幕上播放兼容的文件。传输成功并不保证支持所有音频和视频编码格式。存储空间和硬件也会影响播放。应用不提供电影或付费订阅内容。'),
('手机相机预览 — CAM 2 WATCH','通过受支持的实时连接，在手表上查看手机相机画面。相机、麦克风和录制功能需要相应权限，并由用户主动开启会话。预览需要保持连接，并非不受距离限制的远程访问服务。'),
('文件和 Browser Share','浏览、选择、整理、发送和接收自己的文件及媒体。本地浏览器共享允许同一网络中的兼容浏览器访问受支持的内容。使用时请保持共享会话开启，并仅向可信设备提供连接信息。不要公开配对地址或二维码。'),
('连接手机与手表','安装对应的 Android 和 Wear OS 组件，在两台设备上打开应用并授予所需权限。使用可用方式配对，然后选择功能模块。根据硬件和功能，可能使用 Wi-Fi/LAN、Bluetooth、Wi-Fi Direct 或二维码配对信息。二维码用于交换连接信息，不能代替网络连接。'),
('兼容性与购买','请在 Google Play 中查看设备兼容性和所在地区的可用情况。本地传输无需将媒体上传到开发者运营的云端。ARVION Watch Media Hub 提供 60 分钟试用和完整版一次性购买，不含广告或循环订阅。适用的购买条件以 Google Play 显示为准。')
], [
('可以离线播放吗？','手表中已保存的受支持文件可以本地播放。新文件传输、浏览器共享和实时相机预览仍需要相应连接。'),
('支持所有智能手表吗？','不支持。手表组件需要兼容的 Wear OS 设备。请勿默认其支持 Apple Watch 或采用其他操作系统的手表。'),
('为什么视频传输成功却无法播放？','传输和解码是两个过程。请检查文件格式、音视频编码、剩余空间及接收设备的支持情况。')
], ['在 GOOGLE PLAY 中打开','首页','全部应用','隐私政策','常见问题','了解 ARVION Hub','Android + Wear OS','应用信息'])

add('tr', 'ARVION Hub: Wear OS için müzik, video, kamera ve dosyalar',
'Android ile Wear OS arasında müzik, video ve dosya aktarın. ARVION Hub kamera önizlemesini ve yerel tarayıcı paylaşımını keşfedin.',
'Android telefonunuzu uyumlu bir Wear OS akıllı saatle bağlayın. ARVION Hub; MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, dosya yönetimi ve yerel tarayıcı paylaşımını bir araya getirir. Kendi medyanızı aktarın, desteklenen dosyaları oynatın ve telefon kamerasını bileğinizden görüntüleyin.',
[
('Saatte müzik — MUSIC 2 WATCH','Seçtiğiniz ses dosyalarını Android telefondan uyumlu Wear OS saate aktarın. Müzik ve kayıtlarınızı yürüyüş veya yolculuk için yerel kitaplıkta hazırlayın. Oynatma desteği dosya biçimine ve alıcı cihazın özelliklerine bağlıdır.'),
('Video aktarımı — VIDEO 2 WATCH','Kişisel videolarınızı saate gönderin ve uyumlu dosyaları ekranında oynatın. Başarılı aktarım, tüm ses ve video kodeklerinin desteklendiği anlamına gelmez. Depolama ve donanım da oynatmayı etkiler. Uygulama film veya abonelik içeriği sağlamaz.'),
('Kamera önizlemesi — CAM 2 WATCH','Desteklenen canlı bağlantı üzerinden telefon kamerasını saatte görüntüleyin. Kamera, mikrofon ve kayıt için ilgili izinler ve kullanıcının başlattığı bir oturum gerekir. Önizleme etkin bağlantı gerektirir; sınırsız uzaktan erişim hizmeti değildir.'),
('Dosyalar ve Browser Share','Kendi dosyalarınızı ve medyanızı görüntüleyin, seçin, düzenleyin, gönderin ve alın. Yerel paylaşım, aynı ağdaki uyumlu bir tarayıcıdan desteklenen içeriğe erişim sağlar. Oturumu açık tutun ve bağlantı bilgilerini yalnızca güvendiğiniz cihazlarla paylaşın.'),
('Telefon ile saati bağlama','Uygun Android ve Wear OS bileşenlerini kurun, iki cihazda açın ve gerekli izinleri verin. Kullanılabilir bir yöntemle eşleştirin ve istediğiniz modülü seçin. Donanım ve işleve göre Wi-Fi/LAN, Bluetooth, Wi-Fi Direct ve QR eşleştirme bilgileri kullanılabilir. QR kodu ağ bağlantısının yerini almaz.'),
('Uyumluluk ve satın alma','Google Play üzerinden cihaz uyumluluğunu ve kullanılabilirliği kontrol edin. Yerel aktarımlar için medyanızı geliştiricinin bulutuna yüklemeniz gerekmez. ARVION Watch Media Hub, 60 dakikalık deneme ve tam sürüm için tek seferlik satın alma sunar; reklam veya tekrarlayan abonelik yoktur. Geçerli satın alma koşulları Google Play’de gösterilir.')
], [
('Çevrimdışı oynatabilir miyim?','Saatte kayıtlı desteklenen dosyalar yerel olarak oynatılabilir. Yeni dosya aktarımı, tarayıcı paylaşımı ve canlı kamera önizlemesi uygun bağlantı gerektirir.'),
('Her akıllı saatte çalışır mı?','Hayır. Saat bileşeni uyumlu bir Wear OS cihaz gerektirir. Apple Watch veya başka işletim sistemleri için destek varsaymayın.'),
('Aktarılan video neden oynatılmıyor?','Aktarım ve kod çözme farklı işlemlerdir. Biçimi, kodekleri, boş alanı ve alıcı cihazın özelliklerini kontrol edin.')
], ['GOOGLE PLAY’DE AÇ','Ana sayfa','Tüm uygulamalar','Gizlilik politikası','Sık sorulan sorular','ARVION Hub’ı keşfedin','Android + Wear OS','Uygulama bilgileri'])

add('id', 'ARVION Hub: Musik, Video, Kamera dan File untuk Wear OS',
'Transfer musik, video, dan file antara Android dan Wear OS. Kenali pratinjau kamera serta berbagi lewat browser di jaringan lokal dengan ARVION Hub.',
'Hubungkan ponsel Android dengan smartwatch Wear OS yang kompatibel. ARVION Hub menggabungkan MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, pengelolaan file, dan berbagi melalui browser lokal. Transfer media milik Anda, putar file yang didukung, dan lihat kamera ponsel dari pergelangan tangan.',
[
('Musik di jam — MUSIC 2 WATCH','Transfer file audio pilihan dari Android ke jam Wear OS yang kompatibel. Siapkan musik dan rekaman sendiri dalam koleksi lokal untuk berjalan-jalan atau bepergian. Dukungan pemutaran bergantung pada format file dan kemampuan perangkat penerima.'),
('Transfer video — VIDEO 2 WATCH','Kirim video pribadi ke jam dan putar file yang kompatibel pada layarnya. Transfer yang berhasil tidak menjamin dukungan semua codec audio dan video. Penyimpanan dan perangkat keras juga memengaruhi pemutaran. Aplikasi tidak menyediakan film atau konten berlangganan.'),
('Pratinjau kamera — CAM 2 WATCH','Lihat kamera ponsel pada jam melalui koneksi langsung yang didukung. Kamera, mikrofon, dan perekaman memerlukan izin terkait serta sesi yang dimulai pengguna. Pratinjau membutuhkan koneksi aktif dan bukan layanan akses jarak jauh tanpa batas.'),
('File dan Browser Share','Jelajahi, pilih, kelola, kirim, dan terima media serta file sendiri. Berbagi lokal memungkinkan akses ke konten yang didukung melalui browser kompatibel pada jaringan yang sama. Biarkan sesi tetap aktif dan bagikan informasi koneksi hanya kepada perangkat tepercaya.'),
('Menghubungkan ponsel dan jam','Pasang komponen Android dan Wear OS yang sesuai, buka pada kedua perangkat, lalu berikan izin yang diperlukan. Pasangkan perangkat dengan metode yang tersedia dan pilih modul. Tergantung fungsi serta perangkat keras, metode dapat mencakup Wi-Fi/LAN, Bluetooth, Wi-Fi Direct, dan informasi pemasangan QR. Kode QR tidak menggantikan koneksi jaringan.'),
('Kompatibilitas dan pembelian','Periksa kompatibilitas serta ketersediaan di Google Play. Transfer lokal tidak mengharuskan media diunggah ke cloud pengembang. ARVION Watch Media Hub menawarkan uji coba 60 menit dan pembelian satu kali untuk versi lengkap, tanpa iklan atau langganan berulang. Ketentuan pembelian yang berlaku ditampilkan di Google Play.')
], [
('Bisakah media diputar offline?','File yang didukung dan sudah tersimpan di jam dapat diputar secara lokal. Transfer baru, berbagi lewat browser, dan pratinjau kamera langsung membutuhkan koneksi yang sesuai.'),
('Apakah semua smartwatch didukung?','Tidak. Komponen jam memerlukan perangkat Wear OS yang kompatibel. Jangan menganggap Apple Watch atau sistem operasi lain didukung.'),
('Mengapa video yang ditransfer tidak bisa diputar?','Transfer dan decoding merupakan proses berbeda. Periksa format, codec, ruang kosong, serta kemampuan perangkat penerima.')
], ['BUKA DI GOOGLE PLAY','Beranda','Semua aplikasi','Kebijakan privasi','Pertanyaan umum','Jelajahi ARVION Hub','Android + Wear OS','Informasi aplikasi'])

add('ru', 'ARVION Hub: музыка, видео, камера и файлы для Wear OS',
'Передавайте музыку, видео и файлы между Android и Wear OS. ARVION Hub: просмотр камеры телефона и локальный доступ через браузер.',
'Соедините телефон Android с совместимыми часами Wear OS. ARVION Hub объединяет MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, управление файлами и локальный доступ через браузер. Передавайте собственные материалы, воспроизводите поддерживаемые файлы и смотрите изображение с камеры телефона на запястье.',
[
('Музыка на часах — MUSIC 2 WATCH','Передавайте выбранные аудиофайлы с Android на совместимые часы Wear OS. Подготовьте собственную музыку и записи в локальной библиотеке для прогулки или поездки. Воспроизведение зависит от формата и возможностей принимающего устройства.'),
('Передача видео — VIDEO 2 WATCH','Отправляйте личные видео на часы и воспроизводите совместимые файлы на их экране. Успешная передача не гарантирует поддержку всех аудио- и видеокодеков. На воспроизведение также влияют память и оборудование. Приложение не предоставляет фильмы или контент по подписке.'),
('Просмотр камеры — CAM 2 WATCH','Смотрите изображение с камеры телефона на часах через поддерживаемое соединение в реальном времени. Камере, микрофону и записи нужны соответствующие разрешения и сеанс, запущенный пользователем. Для просмотра необходимо активное соединение; это не безграничный удалённый доступ.'),
('Файлы и Browser Share','Просматривайте, выбирайте, упорядочивайте, отправляйте и получайте собственные файлы и мультимедиа. Локальный доступ позволяет открыть поддерживаемое содержимое в совместимом браузере в той же сети. Не закрывайте сеанс и передавайте данные подключения только доверенным устройствам.'),
('Подключение телефона и часов','Установите подходящие компоненты Android и Wear OS, откройте их на обоих устройствах и выдайте нужные разрешения. Выполните сопряжение доступным способом и выберите модуль. В зависимости от функции и оборудования могут использоваться Wi-Fi/LAN, Bluetooth, Wi-Fi Direct и данные сопряжения QR. QR-код не заменяет сетевое соединение.'),
('Совместимость и покупка','Проверьте совместимость устройства и доступность в Google Play. Локальная передача не требует загрузки материалов в облако разработчика. ARVION Watch Media Hub предлагает пробный период 60 минут и разовую покупку полной версии, без рекламы и регулярных подписок. Действующие условия покупки указаны в Google Play.')
], [
('Можно воспроизводить файлы без интернета?','Поддерживаемые файлы, уже сохранённые на часах, можно воспроизводить локально. Новая передача, доступ через браузер и изображение с камеры требуют подходящего соединения.'),
('Поддерживаются любые смарт-часы?','Нет. Компонент для часов требует совместимого устройства Wear OS. Не следует предполагать поддержку Apple Watch или других операционных систем.'),
('Почему переданное видео не воспроизводится?','Передача и декодирование — разные операции. Проверьте формат, кодеки, свободное место и возможности принимающего устройства.')
], ['ОТКРЫТЬ В GOOGLE PLAY','Главная','Все приложения','Конфиденциальность','Частые вопросы','Узнать об ARVION Hub','Android + Wear OS','Информация о приложении'])

add('uk', 'ARVION Hub: музика, відео, камера та файли для Wear OS',
'Передавайте музику, відео та файли між Android і Wear OS. ARVION Hub: перегляд камери телефона та локальний доступ через браузер.',
'Поєднайте телефон Android із сумісним годинником Wear OS. ARVION Hub об’єднує MUSIC 2 WATCH, VIDEO 2 WATCH, CAM 2 WATCH, керування файлами та локальний доступ через браузер. Передавайте власні матеріали, відтворюйте підтримувані файли й переглядайте камеру телефона на зап’ясті.',
[
('Музика на годиннику — MUSIC 2 WATCH','Передавайте вибрані аудіофайли з Android на сумісний годинник Wear OS. Підготуйте власну музику й записи в локальній бібліотеці для прогулянки або подорожі. Відтворення залежить від формату й можливостей пристрою-одержувача.'),
('Передавання відео — VIDEO 2 WATCH','Надсилайте особисті відео на годинник і відтворюйте сумісні файли на його екрані. Успішне передавання не гарантує підтримки всіх аудіо- та відеокодеків. На відтворення також впливають пам’ять і обладнання. Застосунок не надає фільмів або контенту за підпискою.'),
('Перегляд камери — CAM 2 WATCH','Переглядайте камеру телефона на годиннику через підтримуване з’єднання наживо. Камера, мікрофон і запис потребують відповідних дозволів та сеансу, який запускає користувач. Для перегляду потрібне активне з’єднання; це не необмежений віддалений доступ.'),
('Файли та Browser Share','Переглядайте, вибирайте, впорядковуйте, надсилайте й отримуйте власні файли та мультимедіа. Локальний доступ дозволяє відкривати підтримуваний вміст у сумісному браузері в тій самій мережі. Залишайте сеанс активним і передавайте дані підключення лише надійним пристроям.'),
('Підключення телефона й годинника','Установіть відповідні компоненти Android і Wear OS, відкрийте їх на обох пристроях і надайте потрібні дозволи. Створіть пару доступним способом і виберіть модуль. Залежно від функції та обладнання можуть використовуватися Wi-Fi/LAN, Bluetooth, Wi-Fi Direct та дані сполучення QR. QR-код не замінює мережеве з’єднання.'),
('Сумісність і придбання','Перевірте сумісність пристрою та доступність у Google Play. Локальне передавання не вимагає завантажувати матеріали в хмару розробника. ARVION Watch Media Hub пропонує 60-хвилинну пробну версію та одноразове придбання повної версії, без реклами й регулярних підписок. Чинні умови придбання показано в Google Play.')
], [
('Чи можна відтворювати файли без інтернету?','Підтримувані файли, уже збережені на годиннику, можна відтворювати локально. Нове передавання, доступ через браузер і камера наживо потребують відповідного з’єднання.'),
('Чи підтримуються всі смартгодинники?','Ні. Компонент для годинника потребує сумісного пристрою Wear OS. Не варто припускати підтримку Apple Watch чи інших операційних систем.'),
('Чому передане відео не відтворюється?','Передавання й декодування — різні операції. Перевірте формат, кодеки, вільне місце та можливості пристрою-одержувача.')
], ['ВІДКРИТИ В GOOGLE PLAY','Головна','Усі застосунки','Конфіденційність','Поширені запитання','Дізнатися про ARVION Hub','Android + Wear OS','Інформація про застосунок'])

CSS = '''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#070707;color:#f5f5f5;font:17px/1.75 Arial,Helvetica,sans-serif}a{color:#f1d17a;text-underline-offset:4px}a:focus-visible,summary:focus-visible{outline:3px solid #f1d17a;outline-offset:5px}.wrap{width:min(1120px,calc(100% - 40px));margin:auto}header{border-bottom:1px solid #3b3320;background:#0d0d0d}header .wrap{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:18px 0;flex-wrap:wrap}.brand{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:.12em;text-decoration:none}.brand img{width:40px;height:40px}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px}.hero{padding:54px 0 38px}.eyebrow{color:#f1d17a;font-size:13px;letter-spacing:.08em}h1{font-size:clamp(30px,5vw,56px);line-height:1.15;margin:16px 0 22px;max-width:1020px;overflow-wrap:anywhere}.lead{max-width:860px;color:#d2d2d2;font-size:20px;line-height:1.75}.actions{display:flex;flex-wrap:wrap;align-items:center;gap:18px;margin:26px 0}.cta{display:inline-flex;align-items:center;justify-content:center;background:#f1d17a;color:#18130a;text-decoration:none;font-weight:800;line-height:1.4;padding:14px 22px;border-radius:12px;min-height:48px;max-width:100%;text-align:center}.cta:hover{background:#ffe5a5}.languages{padding:20px 0;border-top:1px solid #3b3320;border-bottom:1px solid #3b3320}.languages a{padding:6px 9px;border:1px solid #3b3320;border-radius:8px}.languages a[aria-current=page]{background:#f1d17a;color:#18130a}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin:32px 0 46px}.feature{background:#101010;border:1px solid #3b3320;border-radius:18px;padding:25px}.feature h2{font-size:23px;line-height:1.35;color:#f1d17a;margin:0 0 16px}.feature p{margin:0;color:#cecece}.faq{margin:0 0 50px}.faq h2{font-size:30px;line-height:1.3}.faq details{border-bottom:1px solid #3b3320;padding:16px 0}.faq summary{font-weight:700;cursor:pointer}.faq p{color:#cecece;max-width:930px}.closing{padding:25px;border:1px solid #3b3320;border-radius:18px;background:#101010;margin-bottom:40px}.closing h2{line-height:1.3;margin-top:0}footer{border-top:1px solid #3b3320;padding:24px 0 40px;color:#aaa;font-size:14px}footer p{overflow-wrap:anywhere}@media(max-width:680px){.wrap{width:calc(100% - 32px)}.hero{padding:30px 0 24px}.lead{font-size:18px}.grid{grid-template-columns:1fr;gap:14px}.feature{padding:20px}.cta{width:100%}header nav{gap:13px}body{font-size:16px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'''

def suffix(lang):
    return '' if lang == 'en' else '-' + lang.lower()
def page_name(lang):
    return 'arvion-hub' + suffix(lang) + '.html'
def home_path(lang):
    return 'index' + suffix(lang) + '.html'
def url_for(lang):
    return BASE + 'apps/' + page_name(lang)
def esc(value):
    return html.escape(str(value), quote=True)
def language_nav(lang):
    return '\n'.join('<a href="'+page_name(k)+'" hreflang="'+k+'" lang="'+k+'"'+(' aria-current="page"' if k == lang else '')+'>'+esc(name)+'</a>' for k,name in LOCALES)

def render(lang):
    d = D[lang]
    label = d['labels']
    home = '../' if lang == 'en' else '../' + home_path(lang)
    catalog = './' if lang == 'en' else home_path(lang)
    alts = '\n'.join('<link rel="alternate" hreflang="'+k+'" href="'+url_for(k)+'">' for k,_ in LOCALES)
    alts += '\n<link rel="alternate" hreflang="x-default" href="'+url_for('en')+'">'
    schema = {'@context':'https://schema.org','@graph':[
        {'@type':'WebPage','@id':url_for(lang)+'#webpage','url':url_for(lang),'name':d['title'],'description':d['description'],'inLanguage':lang,'mainEntity':{'@id':url_for(lang)+'#app'}},
        {'@type':'SoftwareApplication','@id':url_for(lang)+'#app','name':'ARVION Watch Media Hub','alternateName':'ARVION Hub','operatingSystem':'Android, Wear OS','applicationCategory':'MultimediaApplication','url':url_for(lang),'installUrl':PLAY,'description':d['description'],'featureList':[x[0] for x in d['sections'][:4]],'publisher':{'@type':'Organization','name':'ARVION','url':BASE}},
        {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':label[1],'item':BASE+('' if lang=='en' else home_path(lang))},{'@type':'ListItem','position':2,'name':label[2],'item':BASE+'apps/'+('' if lang=='en' else home_path(lang))},{'@type':'ListItem','position':3,'name':'ARVION Hub','item':url_for(lang)}]}
    ]}
    blocks = '\n'.join('<section class="feature" id="feature-'+str(i)+'"><h2>'+esc(h)+'</h2><p>'+esc(p)+'</p></section>' for i,(h,p) in enumerate(d['sections'],1))
    faq = '\n'.join('<details open><summary>'+esc(q)+'</summary><p>'+esc(a)+'</p></details>' for q,a in d['questions'])
    json_ld = json.dumps(schema, ensure_ascii=False, separators=(',',':')).replace('<','\\u003c')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(d['title'])}</title>
<meta name="description" content="{esc(d['description'])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url_for(lang)}">
{alts}
<link rel="icon" type="image/svg+xml" href="../assets/arvion-logo.svg">
<link rel="stylesheet" href="../assets/arvion-hub-product.css">
<meta name="theme-color" content="#070707">
<meta property="og:type" content="website">
<meta property="og:url" content="{url_for(lang)}">
<meta property="og:title" content="{esc(d['title'])}">
<meta property="og:description" content="{esc(d['description'])}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{esc(d['title'])}">
<meta name="twitter:description" content="{esc(d['description'])}">
<script type="application/ld+json">{json_ld}</script>
</head>
<body>
<header><div class="wrap"><a class="brand" href="{home}"><img src="../assets/arvion-logo.svg" alt="ARVION" width="40" height="40">ARVION</a><nav><a href="{home}">{esc(label[1])}</a><a href="{catalog}">{esc(label[2])}</a><a href="../ARVION-WATCH-MEDIA-HUB-PRIVACY.html">{esc(label[3])}</a></nav></div></header>
<main class="wrap">
<section class="hero"><div class="eyebrow">ARVION Watch Media Hub · {esc(label[6])}</div><h1>{esc(d['title'])}</h1><p class="lead">{esc(d['intro'])}</p><div class="actions"><a class="cta" href="{PLAY}" target="_blank" rel="noopener noreferrer">{esc(label[0])}</a><a href="#features">{esc(label[7])}</a></div></section>
<nav class="languages" aria-label="Language">{language_nav(lang)}</nav>
<div class="grid" id="features">{blocks}</div>
<section class="faq"><h2>{esc(label[4])}</h2>{faq}</section>
<section class="closing"><h2>{esc(label[5])}</h2><p>{esc(d['description'])}</p><a class="cta" href="{PLAY}" target="_blank" rel="noopener noreferrer">{esc(label[0])}</a></section>
</main>
<footer><div class="wrap"><nav><a href="{home}">{esc(label[1])}</a><a href="{catalog}">{esc(label[2])}</a><a href="../ARVION-WATCH-MEDIA-HUB-PRIVACY.html">{esc(label[3])}</a></nav><p>ARVION Hub · ARVION Watch Media Hub · <code>pl.arvion.watchmediahub</code></p></div></footer>
<script defer src="../assets/analytics-config.js"></script>
<script defer src="../assets/site-analytics.js"></script>
</body>
</html>
'''

MARK_A = '<!-- ARVION HUB DISCOVERY START -->'
MARK_B = '<!-- ARVION HUB DISCOVERY END -->'

def discovery(lang, in_catalog=False):
    d = D[lang]
    label = d['labels']
    target = ('' if in_catalog else 'apps/') + page_name(lang)
    return f'''{MARK_A}
<section style="width:min(1080px,calc(100% - 32px));margin:28px auto;padding:26px;border:1px solid #5b4926;border-radius:18px;background:#101010;color:#f5f5f5;box-sizing:border-box">
<h2 style="font:700 clamp(24px,3vw,34px)/1.3 Arial,sans-serif;margin:0 0 15px">{esc(d['title'])}</h2>
<p style="font:16px/1.75 Arial,sans-serif;color:#cecece;max-width:940px">{esc(d['description'])}</p>
<div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center"><a href="{target}" style="color:#f1d17a;font-weight:700">{esc(label[5])}</a><a href="{PLAY}" target="_blank" rel="noopener noreferrer" style="background:#f1d17a;color:#18130a;padding:12px 18px;border-radius:10px;text-decoration:none;font:700 14px/1.5 Arial,sans-serif">{esc(label[0])}</a></div>
</section>
{MARK_B}
'''

def integrate(text, block):
    if MARK_A in text:
        return re.sub(re.escape(MARK_A)+r'.*?'+re.escape(MARK_B), lambda m:block.strip(), text, count=1, flags=re.S)
    if '</main>' not in text:
        raise ValueError('Expected closing main element is missing')
    return text.replace('</main>', block+'\n</main>',1)

def build():
    assert set(D) == {k for k,_ in LOCALES}
    policy = ROOT / 'ARVION-WATCH-MEDIA-HUB-PRIVACY.html'
    if 'pl.arvion.watchmediahub' not in policy.read_text(encoding='utf-8'):
        raise ValueError('Product package does not match the source privacy policy')
    pending = {}
    for lang,_ in LOCALES:
        pending['apps/'+page_name(lang)] = render(lang)
        for prefix in ('','apps/'):
            path = prefix+home_path(lang)
            original = (ROOT/path).read_text(encoding='utf-8')
            pending[path] = integrate(original, discovery(lang,bool(prefix)))
    pending['assets/arvion-hub-product.css'] = CSS+'\n'
    sitemap_file = ROOT/'sitemap.xml'
    sitemap = sitemap_file.read_text(encoding='utf-8')
    doc = ET.fromstring(sitemap)
    known = {node.text for node in doc.findall('.//{*}loc')}
    new_urls = [url_for(k) for k,_ in LOCALES if url_for(k) not in known]
    if new_urls:
        addition = ''.join('  <url><loc>'+esc(url)+'</loc></url>\n' for url in new_urls)
        if '</urlset>' not in sitemap:
            raise ValueError('Unsupported sitemap format')
        sitemap = sitemap.replace('</urlset>',addition+'</urlset>',1)
    ET.fromstring(sitemap)
    pending['sitemap.xml'] = sitemap
    # Validate every output before changing any tracked file.
    for lang,_ in LOCALES:
        body = pending['apps/'+page_name(lang)]
        assert body.count('<h1>') == 1
        assert body.count('rel="canonical"') == 1
        assert body.count('rel="alternate"') == 15
        assert body.count('<section class="feature"') == 6
        assert body.count('<details open>') >= 3
        assert '<html lang="'+lang+'">' in body
        assert 'noindex' not in body
        for script in re.findall(r'<script type="application/ld\+json">(.*?)</script>',body,re.S):
            json.loads(script)
        for other,_ in LOCALES:
            assert 'hreflang="'+other+'" href="'+url_for(other)+'"' in body
        for prefix in ('','apps/'):
            assert pending[prefix+home_path(lang)].count(MARK_A) == 1
    changed = []
    for relative, content in pending.items():
        path = ROOT/relative
        if path.exists() and path.read_text(encoding='utf-8') == content:
            continue
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(content,encoding='utf-8')
        changed.append(relative)
    print(json.dumps({'product_pages':14,'localized_discovery_sections':28,'new_sitemap_urls':len(new_urls),'changed_files':changed,'checks':'passed'},ensure_ascii=False,indent=2))
    return changed

if __name__ == '__main__':
    build()
