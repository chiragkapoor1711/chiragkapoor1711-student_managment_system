from tkinter import  *
from tkinter import messagebox
window=Tk()
def login():
    if userentry.get()=="" or passwordentry.get()=="":
        messagebox.showerror("ERROR","Fields cannot be empty")
    elif userentry.get()=="chirag" and passwordentry.get()=="123":
        messagebox.showinfo("success","welcome")
        window.destroy()
        import sms

    else:
        messagebox.showerror("Error","please enter correct credentials")

window.title("LOGIN SYSTEM OF STUDENT MANAGEMENT SYSTEM ")
window.geometry("1050x700+170+10")
window.resizable(False,False)
backgroundimg=PhotoImage(file='loginimg.png')
bglabel=Label(window,image=backgroundimg)
bglabel.place(x=0,y=0)
loginframe=Frame(window,bg="white")
loginframe.place(x=600,y=100)
logoimg=PhotoImage(file="limg.png")
logolabel=Label(loginframe,image=logoimg,bg="white")
logolabel.grid(row=0,column=0,columnspan=2,pady=5)
userimage=PhotoImage(file="user.png")
usernamelabel=Label(loginframe,image=userimage,text="Username",compound=LEFT,font=("time new roman",16,"bold"),bg="white")
usernamelabel.grid(row=1,column=0,pady=5,padx=5)
userentry=Entry(loginframe,font=("time new roman",14,"bold"),bd=5)
userentry.grid(row=1,column=1,pady=10,padx=5)

passwordimage=PhotoImage(file="padlock.png")
passwordlabel=Label(loginframe,image=passwordimage,text="Password",compound=LEFT,font=("time new roman",16,"bold"),bg="white")
passwordlabel.grid(row=2,column=0,pady=5,padx=5)
passwordentry=Entry(loginframe,font=("time new roman",14,"bold"),bd=5,show="*")
passwordentry.grid(row=2,column=1,pady=5,padx=5)

loginbutton=Button(loginframe,text="Login",font=("time new roman",14,"bold"),width=12,fg="white",bg="black",activebackground="black",activeforeground="white",cursor="hand2",command=login)
loginbutton.grid(row=3,column=1)
window.mainloop()