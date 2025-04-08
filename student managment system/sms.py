from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

# Functions part
def iexit():
    result=messagebox.askyesno('confirm','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfile(defaultextension='.csv')
    indexing=studenttable.get_children()
    newlist=[]
    for index in indexing:
        content=studenttable.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table=pandas.DataFrame(newlist,columns=['ID','NAME','AGE','GENDER','BRANCH','EMAIL','ADDRESS','MOBILE NO.','D.O.B'])
    table.to_csv(url,index=False)
    messagebox.showinfo('success','Data is saved successfully')

import pymysql
from tkinter import *
from tkinter import ttk, messagebox
def update_student():
    def update_data():
        # Define your SQL update query
        query = 'UPDATE student SET name=%s, age=%s, gender=%s, branch=%s, email=%s, address=%s, mobile=%s, dob=%s WHERE id=%s'

        # Collect all the values to be updated
        name = nameentry.get()
        age = ageentry.get()
        gender = genderentry.get()
        branch = branchentry.get()
        email = emailentry.get()
        address = addressentry.get()
        mobile = mobileentry.get()
        dob = dobentry.get()
        student_id = identry.get()


        try:
            mycursor.execute(query, (name, age, gender, branch, email, address, mobile, dob, student_id))
            con.commit()  # Commit the changes t  o the database

            # Show success message after updating
            messagebox.showinfo('Success', f'ID {student_id} is modified successfully')
            updatewindow.destroy()  # Close the update window
            show_student()  # Refresh the student list
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update student data: {e}")
            print("Error:", e)

    updatewindow = Toplevel()
    updatewindow.resizable(False, False)
    updatewindow.grab_set()
    idlabel = Label(updatewindow, text="Student ID", font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0, pady=10, padx=10, sticky=W)
    identry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    identry.grid(row=0, column=1, padx=10, pady=10)

    namelabel = Label(updatewindow, text="Student Name", font=('times new roman', 20, 'bold'))
    namelabel.grid(row=0, column=2, pady=10, padx=10, sticky=W)
    nameentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    nameentry.grid(row=0, column=3, padx=10, pady=10)

    agelabel = Label(updatewindow, text="Student Age", font=('times new roman', 20, 'bold'))
    agelabel.grid(row=0, column=4, pady=10, padx=10, sticky=W)
    ageentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    ageentry.grid(row=0, column=5, padx=10, pady=10)

    genderlabel = Label(updatewindow, text="Student Gender", font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=1, column=0, pady=10, padx=10, sticky=W)
    genderentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    genderentry.grid(row=1, column=1, padx=10, pady=10)

    branchlabel = Label(updatewindow, text="Branch", font=('times new roman', 20, 'bold'))
    branchlabel.grid(row=1, column=2, pady=10, padx=10, sticky=W)
    branchentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    branchentry.grid(row=1, column=3, padx=10, pady=10)

    emaillabel = Label(updatewindow, text="Student Email", font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=1, column=4, pady=10, padx=10, sticky=W)
    emailentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    emailentry.grid(row=1, column=5, padx=10, pady=10)

    addresslabel = Label(updatewindow, text="Student Address", font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=2, column=0, pady=10, padx=10, sticky=W)
    addressentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    addressentry.grid(row=2, column=1, padx=10, pady=10)

    mobilelabel = Label(updatewindow, text="Mobile NO.", font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=2, column=2, pady=10, padx=10, sticky=W)
    mobileentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    mobileentry.grid(row=2, column=3, padx=10, pady=10)

    doblabel = Label(updatewindow, text="Student D.O.B", font=('times new roman', 20, 'bold'))
    doblabel.grid(row=2, column=4, pady=10, padx=10, sticky=W)
    dobentry = Entry(updatewindow, font=('times new roman', 15, 'bold'))
    dobentry.grid(row=2, column=5, padx=10, pady=10)

    update_student_button = ttk.Button(updatewindow, text="UPDATE", style="Custom.TButton",command=update_data)
    update_student_button.grid(row=3, columnspan=6, pady=10)

    indexing=studenttable.focus()
    print(indexing)
    content=studenttable.item(indexing)
    listdata=content['values']
    identry.insert(0,listdata[0])
    nameentry.insert(0,listdata[1])
    ageentry.insert(0,listdata[2])
    genderentry.insert(0,listdata[3])
    branchentry.insert(0,listdata[4])
    emailentry.insert(0,listdata[5])
    addressentry.insert(0,listdata[6])
    mobileentry.insert(0,listdata[7])
    dobentry.insert(0,listdata[8])
def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert('', END, values=data)


def delete_student():
    indexing=studenttable.focus()
    print(indexing)
    content=studenttable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('deleted',f'ID{content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert('',END,values=data)

def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or age=%s or gender=%s or branch=%s or email=%s or address=%s or dob=%s'
        mycursor.execute(query,(identry.get(),nameentry.get(),ageentry.get(),genderentry.get(),branchentry.get(),emailentry.get(),addressentry.get(),dobentry.get()))
        studenttable.delete(*studenttable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studenttable.insert('',END,values=data)


    searchwindow = Toplevel()
    searchwindow.resizable(False, False)
    searchwindow.grab_set()
    searchwindow.title('search window')
    idlabel = Label(searchwindow, text="Student ID", font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0, pady=10, padx=10, sticky=W)
    identry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    identry.grid(row=0, column=1, padx=10, pady=10)

    namelabel = Label(searchwindow, text="Student Name", font=('times new roman', 20, 'bold'))
    namelabel.grid(row=0, column=2, pady=10, padx=10, sticky=W)
    nameentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    nameentry.grid(row=0, column=3, padx=10, pady=10)

    agelabel = Label(searchwindow, text="Student Age", font=('times new roman', 20, 'bold'))
    agelabel.grid(row=0, column=4, pady=10, padx=10, sticky=W)
    ageentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    ageentry.grid(row=0, column=5, padx=10, pady=10)

    genderlabel = Label(searchwindow, text="Student Gender", font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=1, column=0, pady=10, padx=10, sticky=W)
    genderentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    genderentry.grid(row=1, column=1, padx=10, pady=10)

    branchlabel = Label(searchwindow, text="Branch", font=('times new roman', 20, 'bold'))
    branchlabel.grid(row=1, column=2, pady=10, padx=10, sticky=W)
    branchentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    branchentry.grid(row=1, column=3, padx=10, pady=10)

    emaillabel = Label(searchwindow, text="Student Email", font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=1, column=4, pady=10, padx=10, sticky=W)
    emailentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    emailentry.grid(row=1, column=5, padx=10, pady=10)

    addresslabel = Label(searchwindow, text="Student Address", font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=2, column=0, pady=10, padx=10, sticky=W)
    addressentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    addressentry.grid(row=2, column=1, padx=10, pady=10)

    mobilelabel = Label(searchwindow, text="Mobile NO.", font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=2, column=2, pady=10, padx=10, sticky=W)
    mobileentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    mobileentry.grid(row=2, column=3, padx=10, pady=10)

    doblabel = Label(searchwindow, text="Student D.O.B", font=('times new roman', 20, 'bold'))
    doblabel.grid(row=2, column=4, pady=10, padx=10, sticky=W)
    dobentry = Entry(searchwindow, font=('times new roman', 15, 'bold'))
    dobentry.grid(row=2, column=5, padx=10, pady=10)

    search_student_button = ttk.Button(searchwindow, text="SEARCH STUDENT", style="Custom.TButton", command=search_data)
    search_student_button.grid(row=3, columnspan=6, pady=10)


def add_student():
    def add_data():
        if identry.get()=='' or nameentry.get()=='' or ageentry.get()=='' or genderentry.get()=='' or \
            branchentry.get()=='' or emailentry.get()=='' or mobileentry.get()=='' or addressentry.get()=='' or \
            dobentry.get()=='':
            messagebox.showerror("Error","All feilds are required",parent=addwindow)
        else:
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(identry.get(),nameentry.get(),ageentry.get(),genderentry.get(),\
                                        branchentry.get(),emailentry.get(),addressentry.get(),mobileentry.get(),dobentry.get()))
                con.commit()
                result=messagebox.askyesno('confirm',"data added successfully. do you want to clean the form?")
                if result:
                    identry.delete(0,END)
                    nameentry.delete(0, END)
                    ageentry.delete(0, END)
                    branchentry.delete(0, END)
                    mobileentry.delete(0, END)
                    emailentry.delete(0, END)
                    addressentry.delete(0, END)
                    genderentry.delete(0, END)
                    dobentry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror("error","id cannot be repeated",parent=addwindow)
                return
            query='select * from student'
            mycursor.execute(query)
            fetch_data=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for data in fetch_data:
                datalist=list(data)
                studenttable.insert('',END,values=datalist)


    addwindow=Toplevel()
    addwindow.resizable(False,False)
    addwindow.grab_set()
    idlabel=Label(addwindow,text="Student ID",font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0,pady=10,padx=10,sticky=W)
    identry=Entry(addwindow,font=('times new roman',15,'bold'))
    identry.grid(row=0,column=1,padx=10,pady=10)

    namelabel = Label(addwindow, text="Student Name", font=('times new roman', 20, 'bold'))
    namelabel.grid(row=0, column=2, pady=10, padx=10,sticky=W)
    nameentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    nameentry.grid(row=0, column=3, padx=10, pady=10)

    agelabel = Label(addwindow, text="Student Age", font=('times new roman', 20, 'bold'))
    agelabel.grid(row=0, column=4, pady=10, padx=10,sticky=W)
    ageentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    ageentry.grid(row=0, column=5, padx=10, pady=10)

    genderlabel = Label(addwindow, text="Student Gender", font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=1, column=0, pady=10, padx=10,sticky=W)
    genderentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    genderentry.grid(row=1, column=1, padx=10, pady=10)

    branchlabel = Label(addwindow, text="Branch", font=('times new roman', 20, 'bold'))
    branchlabel.grid(row=1, column=2, pady=10, padx=10,sticky=W)
    branchentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    branchentry.grid(row=1, column=3, padx=10, pady=10)

    emaillabel = Label(addwindow, text="Student Email", font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=1, column=4, pady=10, padx=10,sticky=W)
    emailentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    emailentry.grid(row=1, column=5, padx=10, pady=10)

    addresslabel = Label(addwindow, text="Student Address", font=('times new roman', 20, 'bold'))
    addresslabel.grid(row=2, column=0, pady=10, padx=10,sticky=W)
    addressentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    addressentry.grid(row=2, column=1, padx=10, pady=10)

    mobilelabel = Label(addwindow, text="Mobile NO.", font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=2, column=2, pady=10, padx=10,sticky=W)
    mobileentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    mobileentry.grid(row=2, column=3, padx=10, pady=10)

    doblabel = Label(addwindow, text="Student D.O.B", font=('times new roman', 20, 'bold'))
    doblabel.grid(row=2, column=4, pady=10, padx=10,sticky=W)
    dobentry = Entry(addwindow, font=('times new roman', 15, 'bold'))
    dobentry.grid(row=2, column=5, padx=10, pady=10)

    add_student_button=ttk.Button(addwindow,text="ADD STUDENT",style="Custom.TButton",command=add_data)
    add_student_button.grid(row=3,columnspan=6,pady=10)


def connectdatabase():

    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostentry.get(),user=userentry.get(),password=passwordentry.get())
            mycursor=con.cursor()
            messagebox.showinfo("success","database connection is successfull")
        except:
            messagebox.showerror("Error","invalid details",parent=connectwindow)
            return
        try:
            # Attempt to create the database
            query = 'CREATE DATABASE studentmanagementsystem'
            mycursor.execute(query)
            print("Database created successfully.")

            # Use the newly created database
            query = 'USE studentmanagementsystem'
            mycursor.execute(query)
            print("Using database studentmanagementsystem.")

            # Create the table
            query = '''CREATE TABLE student(
                       id INT NOT NULL PRIMARY KEY, 
                       name VARCHAR(30),
                       age INT, 
                       branch VARCHAR(10),
                       mobile VARCHAR(10),
                       email VARCHAR(30), 
                       address VARCHAR(100), 
                       gender VARCHAR(30), 
                       dob VARCHAR(20)
                       )'''
            print(f"Executing query: {query}")
            mycursor.execute(query)
            print("Table 'student' created successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
            query = 'USE studentmanagementsystem'
            mycursor.execute(query)
            connectwindow.destroy()
        addstudentbutton.config(state=NORMAL)
        searchstudentbutton.config(state=NORMAL)
        deletestudentbutton.config(state=NORMAL)
        updatestudentbutton.config(state=NORMAL)
        showstudentbutton.config(state=NORMAL)
        exportstudentbutton.config(state=NORMAL)
        exitbutton.config(state=NORMAL)

    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry("470x250+800+230")
    connectwindow.title("Database connection")
    connectwindow.resizable(0,0)

    hostnamelabel=Label(connectwindow,text="Host name:",font=('arial,20,"bold'))
    hostnamelabel.grid(row=0,column=0,padx=20)
    hostentry=Entry(connectwindow,font=('roman,20,"bold'),bd=2)
    hostentry.grid(row=0,column=1,pady=20,padx=40)

    usernamelabel = Label(connectwindow, text="User name:", font=('arial,20,"bold'))
    usernamelabel.grid(row=1, column=0, padx=20)
    userentry = Entry(connectwindow, font=('roman,20,"bold'), bd=2)
    userentry.grid(row=1, column=1, pady=20, padx=40)

    passwordlabel = Label(connectwindow, text="Password:", font=('arial,20,"bold'))
    passwordlabel.grid(row=2, column=0, padx=20)
    passwordentry = Entry(connectwindow, font=('roman,20,"bold'), bd=2,show="*")
    passwordentry.grid(row=2, column=1, pady=20, padx=40)

    connectbutton=ttk.Button(connectwindow,text="Connect",style="Custom.TButton",command=connect)
    connectbutton.grid(row=3,column=1 )


def clock():
    date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'    Date: {date} \n Time: {current_time}')
    datetimelabel.after(1000, clock)

root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('itft1')
root.geometry("1500x750+10+10")
root.resizable(0, 0)
root.title("STUDENT MANAGEMENT SYSTEM")

# Top frame
top_frame = Frame(root)
top_frame.place(x=0, y=0, width=1500, height=80)

datetimelabel = Label(top_frame, font=("times new roman", 14, "bold"))
datetimelabel.place(x=5, y=5)
clock()
# Define a custom style for the button with a custom font
style = ttk.Style()
style.configure("Custom.TButton", font=("Helvetica", 16, "bold"),anchor='center')
connectButton = ttk.Button(top_frame,  text="CONNECT  DATABASE",style="Custom.TButton" ,command=connectdatabase)
connectButton.place(x=1230, y=6)

s = "Student Management System"
titlelabel = Label(top_frame, text=s, font=("arial", 28, "italic bold"))
titlelabel.place(x=500, y=3)

leftframe=Frame(root)
leftframe.place(x=50,y=81,width=300,height=650)

logo_image=PhotoImage(file="limg.png")
logolabel=Label(leftframe,image=logo_image)
logolabel.grid(row=0,column=0)

addstudentbutton=ttk.Button(leftframe,text="ADD STUDENT",width=20,style="Custom.TButton",state=DISABLED,command=add_student)
addstudentbutton.grid(row=1,column=0)

searchstudentbutton=ttk.Button(leftframe,text="SEARCH STUDENT",width=20,style="Custom.TButton",state=DISABLED,command=search_student)
searchstudentbutton.grid(row=2,column=0,pady=20)

deletestudentbutton=ttk.Button(leftframe,text="DELETE STUDENT",width=20,style="Custom.TButton",state=DISABLED,command=delete_student)
deletestudentbutton.grid(row=3,column=0,pady=15)

updatestudentbutton=ttk.Button(leftframe,text="UPDATE STUDENT",width=20,style="Custom.TButton",state=DISABLED,command=update_student)
updatestudentbutton.grid(row=4,column=0,pady=15)

showstudentbutton=ttk.Button(leftframe,text="SHOW STUDENT",width=20,style="Custom.TButton",state=DISABLED,command=show_student)
showstudentbutton.grid(row=5,column=0,pady=15)

exportstudentbutton=ttk.Button(leftframe,text="EXPORT DATA",width=20,style="Custom.TButton",state=DISABLED,command=export_data)
exportstudentbutton.grid(row=6,column=0,pady=15)

exitbutton=ttk.Button(leftframe,text="EXIT",width=20,style="Custom.TButton",state=DISABLED,command=iexit)
exitbutton.grid(row=7,column=0,pady=15)

rightframe=Frame(root)
rightframe.place(x=350,y=81,width=1150,height=650)

scrollbarx=Scrollbar(rightframe,orient=HORIZONTAL)
scrollbary=Scrollbar(rightframe,orient=VERTICAL)

studenttable=ttk.Treeview(rightframe,columns=('ID','Name','Age','Gender','Branch','Email','Address','Mobile','D.O.B'),
                          xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
scrollbarx.config(command=studenttable.xview)
scrollbary.config(command=studenttable.yview)
scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)
studenttable.pack(fill=BOTH,expand=1)

studenttable.heading('ID',text=" Student ID")
studenttable.heading('Name',text=" Student Name")
studenttable.heading('Age',text=" Student age")
studenttable.heading('Gender',text="Gender")
studenttable.heading('Branch',text="Branch")
studenttable.heading('Email',text=" Student Email")
studenttable.heading('Mobile',text="Mobile No.")
studenttable.heading('Address',text="Address")
studenttable.heading('D.O.B',text=" Student D.O.B")
studenttable.config(show='headings')

studenttable.column('ID',width=120,anchor=CENTER)
studenttable.column('Name',anchor=CENTER)
studenttable.column('Age',anchor=CENTER)
studenttable.column('Gender',anchor=CENTER)
studenttable.column('Branch',anchor=CENTER)
studenttable.column('Email',anchor=CENTER)
studenttable.column('Mobile',anchor=CENTER)
studenttable.column('Address',anchor=CENTER)
studenttable.column('D.O.B',anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=30,font=('arial',12,'bold'))
style.configure('Treeview.Heading',font=('arial',12,'bold'))

root.mainloop()