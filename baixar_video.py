import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from yt_dlp import YoutubeDL

FFMPEG_PATH = r'C:\ffmpeg\bin'

def baixar_audio():
    url = entrada_url.get().strip()
    if not url:
        messagebox.showwarning("Atenção", "Por favor, insira uma URL do YouTube.")
        return

    pasta_destino = filedialog.askdirectory(title="Selecione a pasta para salvar o MP3")
    if not pasta_destino:
        messagebox.showwarning("Atenção", "Nenhuma pasta selecionada.")
        return

    barra_progresso['value'] = 0
    label_progresso.config(text="")

    def progresso_hook(d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded_bytes = d.get('downloaded_bytes', 0)
            if total_bytes:
                progresso = int(downloaded_bytes / total_bytes * 100)
                barra_progresso['value'] = progresso
                label_progresso.config(text=f"Baixando... {progresso}%")
                janela.update_idletasks()
        elif d['status'] == 'finished':
            barra_progresso['value'] = 100
            label_progresso.config(text="Download concluído. Convertendo...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'ffmpeg_location': FFMPEG_PATH,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progresso_hook],
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        label_progresso.config(text="Download e conversão concluídos com sucesso!")
        messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
        entrada_url.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")
        label_progresso.config(text="")

janela = tk.Tk()
janela.title("Baixar MP3 do YouTube")
janela.geometry("400x220")

titulo = tk.Label(janela, text="Insira a URL do vídeo e clique em baixar:")
titulo.pack(pady=10)

entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(pady=5)

botao = tk.Button(janela, text="Baixar Áudio", command=baixar_audio)
botao.pack(pady=10)

barra_progresso = ttk.Progressbar(janela, orient='horizontal', length=350, mode='determinate')
barra_progresso.pack(pady=10)

label_progresso = tk.Label(janela, text="")
label_progresso.pack()

janela.mainloop()
