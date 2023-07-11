import tkinter
from tkinter import *
from tkinter import messagebox
import datetime
cur=tkinter.Tk()
def func():
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


def pay():
    noc1=noc.get()
    cn1=cn.get()
    vu1=vu.get()
    cvv1=cvv.get()
    import mysql.connector
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tiger",
        database="system35")
    cursor1=con.cursor()
    sql="insert into payment values('"+str(noc1)+"',"+str(cn1)+",'"+str(cvv)+"');"    
    cursor1.execute(sql)
    messagebox.showinfo("  ","Rs.499 has been debited")

    con.commit()
    
    
    con.commit()
cur.geometry("500x500")
cur.configure(bg="white")
he=tkinter.Label(cur,text="Step 3 of 3",font=("bebas neue",15),bg="white")
de=tkinter.Label(cur,text="ENTER your payment details",bg="white")
k=tkinter.Label(cur,text="NETFLIX",font=("bebas neue",28),fg="red",bg="white")
y=Button(cur,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=func)
x=tkinter.Label(cur,text="NAME ON CARD     :",bg="white")
a=tkinter.Label(cur,text="CARD NUMBER       :",bg="white")
b=tkinter.Label(cur,text="VALID UPTO            :",bg="white")
c=tkinter.Label(cur,text="CVV                          :",bg="white")

noc=StringVar()
cn=IntVar()
vu=IntVar()
cvv=IntVar()

na=tkinter.Entry(cur,textvariable=noc)
ph=tkinter.Entry(cur,textvariable=cn)
pas1=tkinter.Entry(cur,textvariable=vu)
pas2=tkinter.Entry(cur,textvariable=cvv)

k.place(x=0,y=0)
x.place(x=100,y=115)
a.place(x=100,y=165)
na.place(x=300,y=115)
b.place(x=100,y=215)
ph.place(x=300,y=165)
c.place(x=100,y=265)
pas1.place(x=300,y=215)
he.place(x=50,y=65)
y.place(x=430,y=0)
pas2.place(x=300,y=265)
de.place(x=45,y=50)



button=tkinter.Button(cur,text="PROCEED TO PAY Rs.499",bg="red",fg="white",font=("titan romans",10,"bold"),command=pay)
button.place(x=180,y=300)

button2=tkinter.Button(cur,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=pay)
button2.place(x=190,y=340)
cur.mainloop()

