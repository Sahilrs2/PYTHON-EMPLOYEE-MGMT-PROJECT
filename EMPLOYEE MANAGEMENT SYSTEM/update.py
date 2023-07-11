import tkinter as tk
import mysql.connector

def onclick():
    employee_id = entry1.get()
    name = entry2.get()
    skills = entry3.get()
    designation = entry4.get()
    awards = entry5.get()

    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hrm_db"
    )

    if mydb:
        print("Connection Successful")
    else:
        print("Connection Unsuccessful")

    # Create a cursor
    cursor = mydb.cursor()

    # SQL statement to update the employee record
    sql = "UPDATE employee SET Name=%s, Skills=%s, Designation=%s, Awards=%s WHERE id=%s"
    values = (name, skills, designation, awards, employee_id)

    try:
        # Execute the update query
        cursor.execute(sql, values)
        mydb.commit()
        print("Update successful")
    except mysql.connector.Error as error:
        print("Error updating record:", error)

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

root = tk.Tk()
root.geometry("500x525+300+200")
root.title("Update Employees")
root.configure(bg="light blue")

# Create labels
label1 = tk.Label(root, text="ID:",bg="light blue")
label1.place(x=50, y=30)

label2 = tk.Label(root, text="Name:",bg="light blue")
label2.place(x=50, y=60)

label3 = tk.Label(root, text="Skills:",bg="light blue")
label3.place(x=50, y=90)

label4 = tk.Label(root, text="Designation:",bg="light blue")
label4.place(x=50, y=120)

label5 = tk.Label(root, text="Awards:",bg="light blue")
label5.place(x=50, y=150)

# Create entry fields
entry1 = tk.Entry(root,border=0,bg="light blue")
entry1.place(x=150, y=30)

entry2 = tk.Entry(root,border=0,bg="light blue")
entry2.place(x=150, y=60)

entry3 = tk.Entry(root,border=0,bg="light blue")
entry3.place(x=150, y=90)

entry4 = tk.Entry(root,border=0,bg="light blue")
entry4.place(x=150, y=120)

entry5 = tk.Entry(root,border=0,bg="light blue")
entry5.place(x=150, y=150)

f=tk.Frame(root,width=145,height=2,bg="black")
f.place(x=150,y=50)

f1=tk.Frame(root,width=145,height=2,bg="black")
f1.place(x=150,y=80)

f2=tk.Frame(root,width=145,height=2,bg="black")
f2.place(x=150,y=110)

f3=tk.Frame(root,width=145,height=2,bg="black")
f3.place(x=150,y=140)

f4=tk.Frame(root,width=145,height=2,bg="black")
f4.place(x=150,y=170)

# Create button
button = tk.Button(root, width=50, pady=7, text="Update Employees",command=onclick,bg="black",fg="white")
button.place(x=50, y=300)

root.mainloop()
