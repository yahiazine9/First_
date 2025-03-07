from tkinter import *

root=Tk()
# input box
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=5)  
e.get()

def Button_Click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,f"{current}{number}")
    
def Button_Clear():
    e.delete(0,END)

def Button_Add():
    global f_num
    f_num= int(e.get())
    global math 
    math="addition"
    e.delete(0,END)

def Button_Equal():
    s_num=int(e.get())
    e.delete(0,END)
    if math =="addition":
        e.insert(0,f_num+s_num)
    if math =="substraction":
        e.insert(0,f_num-s_num)
    if math =="multiplication":
        e.insert(0,f_num*s_num)
    if math =="division":
        e.insert(0,f_num/s_num)

def Button_Subtract():
    global f_num
    global math 
    math="substraction"
    f_num= int(e.get())
    e.delete(0,END)  

def Button_Multiply():
    global f_num
    global math 
    math="multiplication"
    f_num= int(e.get())
    e.delete(0,END)

def Button_Divide():
    global f_num
    global math 
    math="division"
    f_num= int(e.get())
    e.delete(0,END)


Button_1=Button(root,text="1",padx=23,pady=25,command=lambda:Button_Click(1))
Button_2=Button(root,text="2",padx=23,pady=25,command=lambda:Button_Click(2))
Button_3=Button(root,text="3",padx=23,pady=25,command=lambda:Button_Click(3))
Button_4=Button(root,text="4",padx=23,pady=25,command=lambda:Button_Click(4))
Button_5=Button(root,text="5",padx=23,pady=25,command=lambda:Button_Click(5))
Button_6=Button(root,text="6",padx=23,pady=25,command=lambda:Button_Click(6))
Button_7=Button(root,text="7",padx=23,pady=25,command=lambda:Button_Click(7))
Button_8=Button(root,text="8",padx=23,pady=25,command=lambda:Button_Click(8))
Button_9=Button(root,text="9",padx=23,pady=25,command=lambda:Button_Click(9))
Button_0=Button(root,text="0",padx=23,pady=25,command=lambda:Button_Click(0))
Button_add=Button(root,text="+",padx=23,pady=25,command=Button_Add)
Button_equal=Button(root,text="=",padx=50,pady=25,command=Button_Equal)
Button_clear=Button(root,text="AC",padx=46,pady=25,command=Button_Clear)
Button_subtract=Button(root,text="-",padx=23,pady=25,command=Button_Subtract)
Button_multi=Button(root,text="x",padx=23,pady=25,command=Button_Multiply)
Button_division=Button(root,text="/",padx=23,pady=25,command=Button_Divide)

Button_equal.grid(row=4,column=3,columnspan=2)
Button_clear.grid(row=1,column=3,columnspan=2)
Button_add.grid(row=2,column=3)
Button_subtract.grid(row=3,column=3)
Button_multi.grid(row=2,column=4)
Button_division.grid(row=3,column=4)

Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)  
Button_3.grid(row=3,column=2)
Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)
Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)
Button_0.grid(row=4,column=0)

root.mainloop() 
