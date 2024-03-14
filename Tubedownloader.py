import tkinter
from pytube import  YouTube
import customtkinter
from PIL import Image,ImageTk

def download(): 
               try:  
                    Youtube_link=link_input.get()                           #variable from the link input
                    Youtube_object=YouTube(Youtube_link)                    #create a Youtube object
                    video=Youtube_object.streams.get_highest_resolution()   #get  high video resolution
                    link_label.update()                                     #should update to video title
                    link_label.configure(text=Youtube_object.title)
                    video.download(output_path="C:\\Users\\User\\Downloads")#initiate download

                    


                    downloaded_label.configure(text="Download complete!")
               except:
                    downloaded_label.configure(text='Download unsuccessful.Please verify link')

#application appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#application window
window=customtkinter.CTk()
window.geometry("600x600")
window.title("Youtube Downloader")


#link box
link_label=customtkinter.CTkLabel(master=window,
                                  text="Insert Youtube link",font=("Aeriel black",12,"bold")
                                  )
link_label.pack(padx=10,pady=10)

#using image from link 
                    

#link input
url=tkinter.StringVar()
link_input=customtkinter.CTkEntry(master=window,
                                  width=300,
                                  textvariable=url)
link_input.pack(padx=1,pady=1)


#download completed
downloaded_label=customtkinter.CTkLabel(master=window,text=" ")
downloaded_label.pack(padx=5,pady=5)



#download button
download_button=customtkinter.CTkButton(master=window,text="Download",
                                        font=("Aeriel black",20,"bold"),
                                        command=download)
download_button.pack(padx=10,pady=10)


#launh application
window.mainloop() 