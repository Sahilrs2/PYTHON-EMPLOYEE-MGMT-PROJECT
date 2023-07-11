from tkinter import *
from tkinter import messagebox
def test():
	window.destroy()
	import display
def onsearch():
	window.destroy()
	import search
def onupdate():
	window.destroy()
	import update
window=Tk()
window.configure(bg="light blue")
window.geometry("925x500+300+200")
l=Label(window,text="Welcome HR",fg="black",bg="light blue",width=30,height=3,font=("Times",40,"bold italic"))
l.place(x=20,y=-25)
img=PhotoImage(file='hrm.png')
l1=Label(window,image=img,bg="light blue",border=2)
l1.place(x=10,y=120)
f=Frame(window,width=500,height=350,bg="light blue")
f.place(x=500,y=100)
bttn=Button(f,width=15,pady=2,text="Display Employee",fg="white",bg="black",command=test,border=0,font=("Times",19,"bold italic"))
bttn.place(x=95,y=80)
bttn=Button(f,width=15,pady=2,text="Update Employee",fg="white",bg="black",border=0,font=("Times",19,"bold italic"),command=onupdate)
bttn.place(x=95,y=155)
bttn=Button(f,width=15,pady=2,text="Search Employee",fg="white",bg="black",border=0,font=("Times",19,"bold italic"),command=onsearch)
bttn.place(x=95,y=230)
window.mainloop()	