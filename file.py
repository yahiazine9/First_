from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title()
root.iconbitmap()


# input box
e=Entry(root,width=25)
e.pack()    
e.get()
e.insert(0,"Enter your name")
# Creating a label widget
myLabel=Label(root,text="hello")
#myLabel1=Label(root,text="My name is").grid(row=0, column=0)
myLabel2=Label(root,text="I'am who I'am")


#Shoving it in the screen
#myLabel.pack() center widget

#myLabel2.grid(row=1, column=1)

# Button
def myClick():
     myLabel3=Label(root,text="Hello "+ e.get())
     myLabel3.pack()
myButton=Button(root,text="Enter",padx=50,command=myClick,fg="white",bg="blue")
myButton.pack()

# exit button  
button_exit=Button(root,text="Exit Program",command=root.quit)
button_exit.pack()

# add an image 

my_img=ImageTk.PhotoImage(Image.open("img.jpg"))
myLabel_img=Label(image=my_img)
myLabel_img.pack()
root.mainloop() 
