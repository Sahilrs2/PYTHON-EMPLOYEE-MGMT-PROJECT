from tkinter import *
import mysql.connector
from tkinter import messagebox
def redirect2():
	try:

		mydb = mysql.connector.connect(
  			host="localhost",
  			user="root",
  			password="",
  			database="hrm_db"
  			)
		print(mydb)
		if mydb:
  			print("Connection Established Successfully")
		else:
 			print("Connection Error")
		username=user.get()
		password=pwd.get()
		print("The Password & Username Entered By you is :")
		print(username,password)
		cursor=mydb.cursor()
		sql="select * from login where username =%s and password=%s"
		cursor.execute(sql,[(username),(password)])
		results=cursor.fetchall()
		if results:
			messagebox.showinfo(0,"Login Successfull")
			window.destroy()
			import welcomehr
		else:
			messagebox.showinfo(0,"Login Unsuccessfull")
	except Exception as e:
		messagebox.showinfo(0,e)
		print(e)
	finally:
		mydb.close()
		print("Resources Released....")
def onclick():
	user.focus_set()
window=Tk()
window.title("Login Page by Infosys")
window.geometry("925x500+300+200")
window.configure(bg="white")
window.resizable(False,False)

#======Image Addon=====
img=PhotoImage(file='login.png')
Label(window,image=img,bg="white").place(x=50,y=50)
#=====Frame For Sign In=======
frame=Frame(window,width=350,height=350,bg="white")
frame.place(x=480,y=70)


#=====Heading for Sign In=========
heading=Label(frame,text="Login",fg="#0077b6",bg="white",font=("Source Code",23,"italic"))
heading.place(x=100,y=5)

#====Entry/Input for Username and pwd========
def onuserclick(e):
	user.delete(0,'end')
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Source Code",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",onuserclick)
#======Frame for making Underline======
f=Frame(frame,width=295,height=2,bg="black")
f.place(x=25,y=107)
#------Password Entry=======
def onpwdclick(e):
	pwd.delete(0,'end')
pwd=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Source Code",11))
pwd.place(x=30,y=150)
pwd.insert(0,"Password")
pwd.bind("<FocusIn>",onpwdclick)

#=====Password Undeline======
u=Frame(frame,width=295,height=2,bg="black")
u.place(x=25,y=177)

#====Buton=====
b=Button(frame,width=39,pady=7,text="Login",bg="black",fg="white",border=0,command=redirect2)
b.place(x=35,y=204)

window.mainloop()