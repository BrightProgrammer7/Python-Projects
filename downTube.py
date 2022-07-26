import tkinter as tk
from tkinter import *
from pytube import *
from tkinter import messagebox

# from pytube import YouTube
# from pytube import streams
# from pytube.streams import Stream

root = tk.Tk()
root.title('Youtube Downloader')
root.geometry('500x200')

link_var = StringVar()
link = link_var.get()

ytb = YouTube

# video = ytb(link)


def url():
    link = link_var.get()
    yt = ytb(link)
    # filter(progressive=True, res=" 1080p", subtype='mp4')
    stream = yt.streams.get_highest_resolution()
    stream.download('C:/Users/abdel/Videos/Youtube')
    link_var.set("")
    messagebox.showinfo(title='Download', message='Done')


def info():
    video = ytb(link)

    print(f"Title: \n {video.title} \n ")
    print(f"Description: \n {video.description} \n")
    print(f"Views: \n {video.views} watchers \n ")
    print(f"Rating: \n {video.rating} / 5 \n ")
    print(f"Duration \n{video.length/60} minutes \n ")


title = Label(root, text='Youtube Downloader',
              font=('Helvatical bold', 30, 'bold')).pack()

ent = Entry(root, width="50", textvariable=link_var).pack()

info = Button(root, text='Get Info', command=info).pack()

down = Button(root, text='Download', command=url).pack()

l = Label(root, text='By ABDELILAH').pack(side=BOTTOM)

root.mainloop()


def finish():
    print("Download Done")


video.register_on_complete_callback(finish())
