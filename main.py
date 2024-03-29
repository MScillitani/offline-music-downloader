from pytube import YouTube
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


def button_click():
    if ("youtube" or ".com/") not in link.get().lower():
        showerror('Invalid URL', 'You must use a valid YouTube URL')
        return
    youtube_music = YouTube(link.get())  # sets to the user-input URL
    youtube_music = youtube_music.streams.get_audio_only()  # specifies audio
    try:
        youtube_music.download()  # attempts to download YouTube audio
        download_label = ttk.Label(root, text="Download Successful")
        download_label.pack(expand=False, pady=10)
    except IOError:
        download_label = ttk.Label(root, text="Something went wrong. Please try again.")
        download_label.pack(expand=False, pady=10)


root = tk.Tk()
root.title("Offline Music Downloader")
root.geometry('400x250+50+50')
root.resizable(False, False)

link = tk.StringVar()

link_label = ttk.Label(root, text="Enter YouTube URL:")
link_label.pack(expand=False, padx=50, pady=40)

link_entry = ttk.Entry(root, textvariable=link)
link_entry.pack(fill='x', expand=False, padx=20)
link_entry.focus()

button = ttk.Button(root, text='Download', command=button_click)

button.pack(side="bottom", fill='both', expand=False, padx=150, pady=30)

root.mainloop()

