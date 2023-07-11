import tkinter
from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
window = Tk()
window.configure(bg="light blue")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hrm_db"
    )
print(mydb)
if mydb:
    print("Connection Successfull")
else:
    print("Connection Unsuccessfull")
def search():
    selected=drop.get()
    searched=search_box.get()
    if selected=="Search By...":
        print("Hey You forgot to Pick an Option")
    if selected=="Skills":
        sql="SELECT * FROM employee where Skills LIKE '%"+searched+"%'"
        print("You Picked Skills")
    if selected=="Rewards":
        sql="SELECT * FROM employee where Awards LIKE '%"+searched+"%'"
        print("You Picked Awards")
    if selected=="ID":
        sql="SELECT * FROM employee where ID LIKE '%"+searched+"%'"
        print("You Picked ID")
    if selected=="Name":
        sql="SELECT * FROM employee where Name LIKE '%"+searched+"%'"
        print("You Picked Name")
    #=====CURSOR METHOD=====
    cursor=mydb.cursor()
    
    name=(searched, )
    result=cursor.execute(sql)
    # result=cursor.execute(name)
    result=cursor.fetchall()
    #=====If else for Result=====
    if not result:
        messagebox.showinfo(0,"Record Not Found")
    #====Label For Search========
    drop_label=Label(frame,text=result)
    drop_label.place(x=5 ,y=250)
#======Heading=========
l=Label(window,text="HRM Database",fg="black",bg="light blue",width=30,height=3,font=("Source Code",25,"italic"))
l.place(x=150,y=-30)
#======Image Addon=====
img=PhotoImage(file='search.png')
Label(window,image=img,bg="light blue").place(x=50,y=150)
#=====Frame For Sign In=======
frame=Frame(window,width=350,height=350,bg="light blue")
frame.place(x=480,y=100)
#=====Entry for Search Label=====
def onclick(e):
    search_box.delete(0,'end')
search_box=Entry(frame,width=25,fg="black",border=0,bg="light blue",font=("Source Code",15))
search_box.place(x=180,y=126)
search_box.insert(0,"What to Search?")
search_box.bind("<FocusIn>",onclick)
#======Frame for making Underline======
f=Frame(frame,width=295,height=2,bg="black")
f.place(x=175,y=150)
#======Label for Entry===========
search_label=Label(frame,text="Search By :",bg="light blue",font=("Source Code",15))
search_label.place(x=60,y=125)
#=====Heading for Sign In=========
heading=Label(frame,text="Search Employees",fg="black",bg="light blue",font=("Source Code",23,"italic"))
heading.place(x=75,y=20)
#=====Dropdown for Search=====
drop=ttk.Combobox(frame,value=["Search By...","Skills","Rewards","ID","Name"])
drop.current(0)
drop.place(x=135,y=200)
#=====Button for Search=======
b=Button(frame,width=30,pady=7,text="Search",bg="black",fg="white",border=0,command=search)
b.place(x=100,y=300)
window.geometry("925x500+300+200")
window.title("Display Details:")
window.mainloop()