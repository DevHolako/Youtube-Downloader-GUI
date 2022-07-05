#import Modules
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog,messagebox

def GUIfunction():
    link_Label = Label(root , text="Youtube URL : ",bg="#F8F8F2")
    link_Label.grid(row=1,column=0,pady=5,padx=5)

    root.link_text = Entry(root,width=60,textvariable=vedio_link)
    root.link_text.grid(row=1,column=1,pady=5,padx=5)

    destination_Label = Label(root, text="Destination",bg="#F8F8F2")
    destination_Label.grid(row=2,column=0,pady=5,padx=5)

    root.destination_text = Entry(root,width=45,textvariable=download_path)
    root.destination_text.grid(row=2,column=1,pady=3,padx=3)

    browse_btn = Button(root,text="Browse...",command=browse,width=10,bg="#F8F8F2")
    browse_btn.grid(row=2,column=2,pady=1,padx=1)

    download_btn = Button(root,text="Download",command=download_vedio,width=10,bg="#F8F8F2")
    download_btn.grid(row=3,column=1,pady=3,padx=3)

def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    download_path.set(download_dir)
def download_vedio():
    url = vedio_link.get()
    folder = download_path.get()

    get_vd = YouTube(url)
    get_stream = get_vd.streams.first()
    get_stream.download(folder)
    messagebox.showinfo(title="Status",message="Download finished !!")





root = tk.Tk()
root.geometry("650x120")
root.resizable(False,False)
root.title("YouTube Gruber")
root.config(background="#282C34")

vedio_link = StringVar()
download_path = StringVar()
GUIfunction()

root.mainloop()