import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os
def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()
    progress_label.pack(pady=("10p,5p"))
    progres_bar.pack(pady=("10p,5p") )
    status_label.pack(pady=("10p,5p") )
    try:
        yt = YouTube(url, on_progress_callback=on_progess)
        stream = yt.streams.filter(res = resolution).first()
        os.path.join("downloads", f"{yt.title}.mkv")
        stream.download(output_path="downloads")
        status_label.configure(text ="Downloaded!", text_color ="white")
        status_label.pack(pady=("10p,5p"))
    except Exception as e:
        print(f"Error: {e}")
        status_label.configure(text="NO URL PROVIDED", text_color="red")
        status_label.pack(pady=("10p,5p"))
        
def on_progess(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage_completed = bytes_download/total_size * 100
    
    progress_label.configure(text = str(int(percentage_completed)) + "%")
    progress_label.update()

    progres_bar.set(float(percentage_completed/100))
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root.title("Youtube Video Downloader")

root.geometry("720x480")
root.maxsize(1080, 720)
root.minsize(720, 480)
# mainframe of screen
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand = True,pady = 10)
# url dalne ki tab
url_label = ctk.CTkLabel(content_frame, text = "Enter the URL here ")
entry_url = ctk.CTkEntry(content_frame, width=400,height=40,corner_radius=15,fg_color="grey",text_color="black")
url_label.pack(pady=("10p,15p") )
entry_url.pack(pady=("10p,15p") )
# download button ke liye
download_button = ctk.CTkButton(content_frame, text = "DOWNLOAD",command=download_video,corner_radius=10,fg_color=("blue"))
download_button.pack(pady=("10p,5p") )
# resolution ke liye
resolution = ["1080","720p", "360p", "240p"]
resolution_var = ctk.StringVar()

resolution_combobox = ttk.Combobox(content_frame, values = resolution, textvariable=resolution_var)
resolution_combobox.pack(pady=("10p,5p"))
resolution_combobox.set("1080p")

progress_label = ctk.CTkLabel(content_frame, text = "0%")

progres_bar = ctk.CTkProgressBar(content_frame, width = 450)
progres_bar.set(0)

status_label = ctk.CTkLabel(content_frame, text = "Downloaded")
# run app
root.mainloop()