from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size=0

def progress(stream,chunk,file_handle,remaining=None):
    file_downloaded = (file_size-file_handle)
    percent = float(file_downloaded/file_size)*100
    dBtn.config(text="{:00.0f} % Downloaded".format(percent))

def startdownload():
    global file_size
    try:
        url = urlField.get()
        print(url)
        dBtn.config(text="Please Wait...")
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return

        #creating youtube object with url..
        ob = YouTube(url,on_progress_callback=progress)
        #strms = ob.streams.all()
        #for s in strms:
         #   print(s)
        strm = ob.streams.first()
        file_size=strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        print(file_size)

        strm.download(path_to_save_video)
        print("done...")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded Successfully")
        urlField.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("error!")

def StartDownloadThread():
    thread=Thread(target=startdownload)
    thread.start()

#starting gui building
main=Tk()

main.title("YOUTUBE DOWNLOADER (Created by SaMsUz ZaMaN)")

main.iconbitmap('./res/icon.ico')

main.geometry("500x600")

file = PhotoImage(file='./res/youtube.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)
#urlTextfield
urlField=Entry(main,font =("calibri",20),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)

#download button
dBtn= Button(main, text ="Paste URL and Start Download",font =("comic sans ms",14),relief='ridge',command=StartDownloadThread)
dBtn.pack(side=TOP,pady=10)
vTitle = Label(main, text="Video Title")


main.mainloop()