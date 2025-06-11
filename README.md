# music_downloader

Instalações necessárias
Python 3.6 ou superior

ffmpeg (e configure o caminho no script ou no PATH do sistema)

Biblioteca Python yt-dlp

pip install yt-dlp
(Opcional) tkinter (geralmente já vem com Python, mas no Linux pode precisar:

sudo apt-get install python3-tk
PyInstaller para empacotar o script

pip install pyinstaller

Como gerar o executável (.exe)
No terminal, dentro da pasta do projeto, rode:

pyinstaller --onefile --windowed nome_do_seu_script.py
O executável será criado dentro da pasta dist/.

Para incluir o ffmpeg junto ou garantir que o caminho esteja correto, você pode:

Manter o ffmpeg instalado no sistema e configurar FFMPEG_PATH para o local do ffmpeg.exe, ou

Copiar o executável do ffmpeg para a mesma pasta do .exe.
