import tkinter
from tkinter import *
from tkinter import messagebox
cur=tkinter.Tk()
cur.geometry("500x500")
cur.configure(bg="white")
he=tkinter.Label(cur,text="Step 2 of 3",font=("bebas neue",15),bg="white")
de=tkinter.Label(cur,text="ENTER YOUR DETAILS")
k=tkinter.Label(cur,text="NETFLIX",font=("bebas neue",28),fg="red",bg="white")



def signup():
    email1=email.get()
    ph1=phone.get()
    pass1=passwd1.get()
    pass2=passwd2.get()
    plan=pln.get()
    import mysql.connector
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tiger",
        database="system35")
    cursor1=con.cursor()
    
    if pass1==pass2:
        sql="insert into subscriber values("+str(email)+","+str(ph1)+","+str(pass1)+")"
        cursor1.execute(sql)
    else:
        messagebox.showinfo("  ","  INCORRECT PASSWORD")
    con.commit()

#y=Button(cur,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=func)
x=tkinter.Label(cur,text="EMAIL ID      ",bg="white")
a=tkinter.Label(cur,text="PHONE NO.        ",bg="white")
b=tkinter.Label(cur,text="ENTER PASSWORD                                ",bg="white")
c=tkinter.Label(cur,text="RE-ENTER PASSWORD             ",bg="white")
d=tkinter.Label(cur,text="ENTER PLAN(499/799)             ",bg="white")

email=StringVar()
phone=StringVar()
passwd1=StringVar()
passwd2=StringVar()
pln=StringVar()

na=tkinter.Entry(cur,textvariable=email)
ph=tkinter.Entry(cur,textvariable=phone)
pas1=tkinter.Entry(cur,textvariable=passwd1)
pas2=tkinter.Entry(cur,textvariable=passwd2)
pla=tkinter.Entry(cur,textvariable=pln)

k.place(x=0,y=0)
x.place(x=100,y=100)
a.place(x=100,y=150)
na.place(x=300,y=100)
b.place(x=100,y=200)
ph.place(x=300,y=150)
c.place(x=100,y=250)
pas1.place(x=300,y=200)
he.place(x=50,y=50)
#y.place(x=430,y=0)
pas2.place(x=300,y=250)
pla.place(x=300,y=300)
d.place(x=100,y=300)


button=tkinter.Button(cur,text="PROCEED AND PAY",bg="red",fg="white",font=("titan romans",10,"bold"),command=signup)
button.place(x=200,y=350)
cur.mainloop()

