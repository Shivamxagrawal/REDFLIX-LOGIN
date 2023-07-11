import tkinter
from tkinter import *
from tkinter import messagebox
cur=tkinter.Tk()
cur.geometry("400x400")
name=StringVar()
passw=StringVar()
def new():
    name1=name.get()
    passwd1=passwd.get()                            
    import mysql.connector
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tiger",
        database="system5")
    cursor1=con.cursor()
    sql="select sub_id,password from subscribers"
    c=0
    cursor1.execute(sql)
    data=cursor1.fetchall()
    for i in data:
        if i[0]==name1 and i[1]==passwd1:
            messagebox.showinfo("  ","LOGIN COMPLETE")
            break    
    else:
        messagebox.showinfo("  ","username or password is invalid")
  
     
    con.commit()

x=tkinter.Label(cur,text="NETFLIX",font=("bebas neue",28),fg="red")    

use=tkinter.Label(cur,text="USERNAME",font=("bebas neue",10,"bold"))

pas=tkinter.Label(cur,text="PASSWORD",font=("bebas neue",10,"bold"))

q=tkinter.Label(cur,text="WELCOME BACK.",font=("bebas neue",20))




username=tkinter.Entry(cur,textvariable=name,font=("titan romans",16))

passwd=tkinter.Entry(cur,textvariable=passw,font=("titan romans",16))

y=Button(cur,text="Sign In",font=(20),fg="red",command=new)




x.place(x=0,y=0)
use.place(x=150,y=100)
q.place(x=30,y=62)
username.place(x=85,y=130)
pas.place(x=150,y=160)
passwd.place(x=85,y=190)
y.place(x=150,y=230)
