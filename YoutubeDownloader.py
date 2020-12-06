from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
from pytube import YouTube ##pip install pytube


FileSize = 0
Folder_Name = ""


#To set the folder for saving the downloaded video
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):#To check if folder is selected properly
        PathErrormsg.config(text=Folder_Name,fg="green")

    else:
        PathErrormsg.config(text="Please Choose Folder!!",fg="red")


#To download the video from the provied youtube link
def downloadVideo():
    global FileSize
    Choice = ChoiceMenu.get()
    url = LinkBox.get()

    if(len(url)>1):#To check if the link is valid
        yt = YouTube(url,on_progress_callback=show_progress_bar)
        if(Choice == Choices[0]):
            select = yt.streams.filter(res="1080p").first()
        
        elif(Choice ==Choices[1]):
            select = yt.streams.filter(res="720p").first()

        elif(Choice ==Choices[2]):
            select = yt.streams.filter(res="480p").first()
            
        elif(Choice == Choices[3]):
            LinkErrormsg.config(text="Paste Link Again!!",fg="red")

        else:
            LinkErrormsg.config(text="Please Slect the qulity!!",fg="red")
        FileSize = select.filesize
        select.download(Folder_Name)
        LinkErrormsg.config(text="Download Completed!!",fg="green")
    else:
        LinkErrormsg.config(text="Please Paste the proper link again")
    

#To download the audio file only
def downloadAudio():
    global FileSize
    url =LinkBox.get()

    if(len(url)>1):
        yt =YouTube(url,on_progress_callback=show_progress_bar)
        select = yt.streams.filter(only_audio=True).first()
    else:
         LinkErrormsg.config(text="Paste your link properly!!",fg="green")
    FileSize = select.filesize
    select.download(Folder_Name)
    LinkErrormsg.config(text="Download Completed!!")


#To update the progessbar while downloading video
def show_progress_bar(chunk,file_handler, bytes_remaining):
    #print(bytes_remaining)
    global FileSize
    FileDownloaded = FileSize - bytes_remaining
    #print(FileDownloaded)
    percent = (FileDownloaded/FileSize)*100
    #print(percent)
    ProgressVar.set(percent)
    time.sleep(0.02)
    root.update_idletasks()



#initialization
root=Tk()
root.title("youtube Downloader")
root.geometry("800x500") #window size

#adding an image 
file = PhotoImage(file='logo1.png')
headerIcon = Label(root, image=file,bg="lightgreen")
headerIcon.place(x=100,y=0)

root.config(bg="lightgreen")

#UI design
TextLabel = Label(root,text="Youtube Video and Audio Downloader", font=("Maiandra GD",16,"bold"),bg="lightgreen")
TextLabel.place(x=200,y=20)

LinkLabel = Label(root,text="Enter the video link : ", font=("Comic Sans MS",15),bg="lightgreen")
LinkLabel.place(x=30,y=80)

LinkBoxVar = StringVar()
LinkBox = Entry(root,width=80,textvariable = LinkBoxVar,bg="pink")
LinkBox.place(x=240, y=86)

LinkErrormsg = Label(root, text = "",fg="red",font=("Comic Sans MS",12),bg="lightgreen")
LinkErrormsg.place(x=300, y=130)

PathLabel = Label(root,text="Select the folder where you want save the video : ", font=("Comic Sans MS",15),bg="lightgreen")
PathLabel.place(x=30,y=180)

SaveButton = Button(root, width =15, bg="red",fg="white",text="Choose Path",font=("Arial Rounded MT Bold",12,"bold"),command=openLocation)
SaveButton.place(x=520,y=180)

PathErrormsg = Label(root, text = "",fg="red",font=("Comic Sans MS",12),bg="lightgreen")
PathErrormsg.place(x=300, y=240)

ChoiceLabel = Label(root,text="Select the Quality of the video : ", font=("Comic Sans MS",15),bg="lightgreen")
ChoiceLabel.place(x=100,y=300)

Choices = ["1080p","720p","480p"]
ChoiceMenu = ttk.Combobox(root, values = Choices)
ChoiceMenu.place(x=450,y=305,)

QualityErrormsg = Label(root, text = "",fg="red",font=("Comic Sans MS",12),bg="lightgreen")
QualityErrormsg.place(x=280, y=360)

ProgressVar = DoubleVar()
ProgressBar = ttk.Progressbar(root,orient=HORIZONTAL,variable=ProgressVar,length=500,mode='determinate') #Label(root,text="progress",fg="red",font=("Comic Sans MS",12),bg="lightgreen")
ProgressBar.place(x=150,y=390)

VideoButton = Button(root, width =20, bg="red",fg="white",text="Download Video",font=("Arial Rounded MT Bold",12,"bold"),command=downloadVideo)
VideoButton.place(x=80,y=450)

AudioButton = Button(root, width =20, bg="red",fg="white",text="Download Audio",font=("Arial Rounded MT Bold",12,"bold"),command=downloadAudio)
AudioButton.place(x=500,y=450)

root.mainloop()

