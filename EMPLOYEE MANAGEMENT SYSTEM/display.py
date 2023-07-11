from tkinter import *
import mysql.connector
window=Tk()

''''try:'''
mydb = mysql.connector.connect(
  	host="localhost",
  	user="root",
  	password="",
  	database="hrm_db"
  	)
if mydb:
	print("Connection Successfull")
else:
	print("Connection Unsuccessfull")
cursor=mydb.cursor()
sql="select * from Employee"
cursor.execute(sql)
results=cursor.fetchall()
cnt=len(results)
print(cnt)
if results:
    for j in range(1,len(results)):
	    for i in results:
                id1=Label(window,text=i[0],font="times 12 bold",fg="blue")
                id1.grid(row=j,column=0,padx=10,pady=10)

                name=Label(window,text=i[1],font="times 12 bold",fg="blue",width= 15)
                name.grid(row=j,column=1,padx=10,pady=10)

                doj=Label(window,text=i[2],font="times 12 bold",fg="blue",width= 15)
                doj.grid(row=j,column=2,padx=10,pady=10)

                dob=Label(window,text=i[3],font="times 12 bold",fg="blue",width= 15)
                dob.grid(row=j,column=3,padx=10,pady=10)

                salary=Label(window,text=i[4],font="times 12 bold",fg="blue",width= 15)
                salary.grid(row=j,column=4,padx=10,pady=10)

                overtime=Label(window,text=i[5],font="times 12 bold",fg="blue",width= 15)
                overtime.grid(row=j,column=5,padx=10,pady=10)

                address=Label(window,text=i[6],font="times 12 bold",fg="blue",width= 15)
                address.grid(row=j,column=6,padx=10,pady=10)

                skills=Label(window,text=i[7],font="times 12 bold",fg="blue",width= 15)
                skills.grid(row=j,column=7,padx=10,pady=10)

                awards=Label(window,text=i[8],font="times 12 bold",fg="blue",width= 15)
                awards.grid(row=j,column=8,padx=10,pady=10)

                designation=Label(window,text=i[9],font="times 12 bold",fg="blue",width= 15)
                designation.grid(row=j,column=9,padx=10,pady=10)

                j+=1
                
id2=Label(window,text="ID")
id2.grid(row=0,column=0)
l=Label(window,text="Name")
l.grid(row=0,column=1)
l1=Label(window,text="DOJ")
l1.grid(row=0,column=2)
l1=Label(window,text="DOB")
l1.grid(row=0,column=3)
l1=Label(window,text="Salary")
l1.grid(row=0,column=4)
l1=Label(window,text="Overtime")
l1.grid(row=0,column=5)
l1=Label(window,text="Address")
l1.grid(row=0,column=6)
l1=Label(window,text="Skills")
l1.grid(row=0,column=7)
l1=Label(window,text="Awards")
l1.grid(row=0,column=8)
l1=Label(window,text="Designation")
l1.grid(row=0,column=9)
''''except Exception as e:
	print(e)'''
''''finally:
	mydb.close()'''
print("Resources Released...")
window.geometry("1000x700+300+150")
window.title("Display Details:")
window.mainloop()