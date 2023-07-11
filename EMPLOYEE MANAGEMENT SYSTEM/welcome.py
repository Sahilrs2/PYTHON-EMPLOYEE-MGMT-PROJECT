from tkinter import *

def redirect():
#======Login Page Code=========
	window.destroy()
	import login

#======Home Page Code==========
#===Basic Formation=====
window= Tk()
window.title("Home Page")
window.configure(bg="light blue")
window.resizable(False,False)
window.geometry("925x500+300+200")
#===Image Addon=========
img=PhotoImage(file="main.png")
#===Label to hold on Image===
l=Label(window,image=img,bg="light blue",border=0)
l.place(x=30,y=80)
#====Frame for Welcome and Button===
f=Frame(window,width=2000,height=450,bg="light blue")
f.place(x=515,y=50)
#===Label inside frame(f) for description====
desc=Label(f,text="Welcome To Software Solutions",fg="black",bg="light blue",font=("Times",20,"bold"),border=5)
desc.place(x=2,y=10)
#======Underlining Frame for Desc=====
fdesc=Frame(f,width=400,height=2,bg="black")
fdesc.place(x=2,y=50)
#====Label for Description Of The Company=====
desc=Label(f,text="We at Software Solutions,\nDesign and Develop,\nCustom Software Applications\nFrameworks and Tools that help\nSolve problems or Achieve\nor Achieve a specific Outcome\nLike You Have already guessesd,\nPeople that work here are\npretty smart!!",fg="black",bg="light blue",font=("Times",20,"bold italic"),border=5)
desc.place(x=2,y=70)
#====Button For Login=====
b=Button(f,width=40,pady=7,text="Click Here For Login",fg="white",bg="black",font=("Times",13,"bold"),border=0,command=redirect)
b.place(x=-10,y=375)
window.mainloop()