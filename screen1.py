from tkinter import *
from tkinter import messagebox
m=Tk()
m.geometry('500x500')
import mysql.connector
con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tiger",
        database="system5")

def Signup(a):
   
    cur=Toplevel()
    cur.geometry("500x500")
    cur.configure(bg="white")
    he=Label(cur,text="Step 2 of 3",font=("bebas neue",15),bg="white")
    de=Label(cur,text="ENTER YOUR DETAILS")
    photo=PhotoImage(file="netflix1.png")
    label=Label(cur,image=photo,height=51,width=177,bg="white")
    label.place(x=0,y=0)
    
    email=StringVar()
    phone=IntVar()
    passwd1=StringVar()
    passwd2=StringVar()

    na=Entry(cur,textvariable=email)
    ph=Entry(cur,textvariable=phone)
    pas1=Entry(cur,textvariable=passwd1)
    pas2=Entry(cur,textvariable=passwd2)

        
    import mysql.connector
    con=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="tiger",
            database="system35")
    cursor1=con.cursor()
    email1=email.get()
    ph1=phone.get()
    pass1=passwd1.get()
    pass2=passwd2.get()
    if pass1==pass2:
            sql="insert into subscriber values('"+str(email1)+"','"+str(ph1)+"','"+str(pass1)+"')"    
            cursor1.execute(sql)
            if a=="Basic":
                curb=Toplevel()
                def pay():
                    signup.destroy()
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
                        sql="insert into payment values('"+str(noc1)+"',"+str(cn1)+",'"+str(cvv)+"','"+str(email1)+"');"    
                        cursor1.execute(sql)
                    
                        messagebox.showinfo("  ","Rs.499 has been debited")

                        con.commit()
    
    
                        con.commit()
                curb.geometry("500x500")
                curb.configure(bg="white")
                he=Label(curb,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                de=Label(curb,text="ENTER your payment details",bg="white")
                l=PhotoImage(file="netflix1.png")
                Q1=Label(curb,image=l,height=51,width=177,bg="white")
                y=Button(curb,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                x=Label(curb,text="NAME ON CARD     :",bg="white")
                Pq=Label(curb,text="CARD NUMBER       :",bg="white")
                b=Label(curb,text="VALID UPTO            :",bg="white")
                c=Label(curb,text="CVV                          :",bg="white")

                noc=StringVar()
                cn=IntVar()
                vu=IntVar()
                cvv=IntVar()

                na=Entry(curb,textvariable=noc)
                ph=Entry(curb,textvariable=cn)
                pas1=Entry(curb,textvariable=vu)
                pas2=Entry(curb,textvariable=cvv)

                Q1.place(x=0,y=0)
                x.place(x=100,y=115)
                Pq.place(x=100,y=165)
                na.place(x=300,y=115)
                b.place(x=100,y=215)
                ph.place(x=300,y=165)
                c.place(x=100,y=265)
                pas1.place(x=300,y=215)
                he.place(x=50,y=65)
                y.place(x=430,y=0)
                pas2.place(x=300,y=265)
                de.place(x=45,y=50)
                button=Button(curb,text="PROCEED TO PAY Rs.499",bg="red",fg="white",font=("titan romans",10,"bold"),command=pay)
                button.place(x=180,y=300)

                button2=Button(cur,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func())
                button2.place(x=190,y=340)
                curb.mainloop()
            elif a=="Mobile":
                
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
                        sql="insert into payment values('"+str(noc1)+"',"+str(cn1)+",'"+str(cvv)+"','"+str(email1)+"');"    
                        cursor1.execute(sql)
                        messagebox.showinfo("  ","Rs.199 has been debited")

                        con.commit()
                curm=Toplevel()
                curm.geometry("500x500")
                curm.configure(bg="white")
                he=Label(curm,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                de=Label(curm,text="ENTER your payment details",bg="white")
                l=PhotoImage(file="netflix1.png")
                Q1=Label(curm,image=l,height=51,width=177,bg="white")
                y=Button(curm,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                x=Label(curm,text="NAME ON CARD     :",bg="white")
                Po=Label(curm,text="CARD NUMBER       :",bg="white")
                b=Label(curm,text="VALID UPTO            :",bg="white")
                c=Label(curm,text="CVV                          :",bg="white")

                noc=StringVar()
                cn=IntVar()
                vu=IntVar()
                cvv=IntVar()

                na=Entry(curm,textvariable=noc)
                ph=Entry(curm,textvariable=cn)
                pas1=Entry(curm,textvariable=vu)
                pas2=Entry(curm,textvariable=cvv)

                Q1.place(x=0,y=0)
                x.place(x=100,y=115)
                Po.place(x=100,y=165)
                na.place(x=300,y=115)
                b.place(x=100,y=215)
                ph.place(x=300,y=165)
                c.place(x=100,y=265)
                pas1.place(x=300,y=215)
                he.place(x=50,y=65)
                y.place(x=430,y=0)
                pas2.place(x=300,y=265)
                de.place(x=45,y=50)



                button=Button(curm,text="PROCEED TO PAY Rs.199",bg="red",fg="white",font=("titan romans",10,"bold"),command=pay)
                button.place(x=180,y=300)
                button2=Button(curm,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func)
                button2.place(x=190,y=340)
                curm.mainloop()
            elif a=="Standard":
                    
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
                            messagebox.showinfo("  ","Rs.649 has been debited")
                            con.commit()
                            
                    curst=Toplevel()
                    curst.geometry("500x500")
                    curst.configure(bg="white")
                    he=Label(curst,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                    de=Label(curst,text="ENTER your payment details",bg="white")
                    l=PhotoImage(file="netflix1.png")
                    Q1=Label(curst,image=l,height=51,width=177,bg="white")
                    y=Button(curst,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                    x=Label(curst,text="NAME ON CARD     :",bg="white")
                    a=Label(curst,text="CARD NUMBER       :",bg="white")
                    b=Label(curst,text="VALID UPTO            :",bg="white")
                    c=Label(curst,text="CVV                          :",bg="white")
                    
                    noc=StringVar()
                    cn=IntVar()
                    vu=IntVar()
                    cvv=IntVar()
                    
                    na=Entry(curst,textvariable=noc)
                    ph=Entry(curst,textvariable=cn)
                    pas1=Entry(curst,textvariable=vu)
                    pas2=Entry(curst,textvariable=cvv)
                    
                    Q1.place(x=0,y=0)
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
                    button=Button(curst,text="PROCEED TO PAY Rs.649",bg="red",fg="white",font=("titan romans",10,"bold"),command=pay)
                    button.place(x=180,y=300)
                    button2=Button(curst,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func)
                    button2.place(x=190,y=340)
                    curst.mainloop()
            elif a=="Premium":
                    
                    cur0=Toplevel()
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
                            messagebox.showinfo("  ","Rs.799 has been debited")
                            con.commit()    
                            con.commit()
                    cur0.geometry("500x500")
                    cur0.configure(bg="white")
                    he=Label(cur0,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                    de=Label(cur0,text="ENTER your payment details",bg="white")
                    l=PhotoImage(file="netflix1.png")
                    Q1=Label(cur0,image=l,height=51,width=177,bg="white")
                    y=Button(cur0,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                    x=Label(cur0,text="NAME ON CARD     :",bg="white")
                    a=Label(cur0,text="CARD NUMBER       :",bg="white")
                    b=Label(cur0,text="VALID UPTO            :",bg="white")
                    c=Label(cur0,text="CVV                          :",bg="white")
                    noc=StringVar()
                    cn=IntVar()
                    vu=IntVar()
                    cvv=IntVar()
                    na=Entry(cur0,textvariable=noc)
                    ph=Entry(cur0,textvariable=cn)
                    pas1=Entry(cur0,textvariable=vu)
                    pas2=Entry(cur0,textvariable=cvv)

                    Q1.place(x=0,y=0)
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

                    button=Button(cur0,text="PROCEED TO PAY Rs.799",bg="red",fg="white",font=("titan romans",10,"bold"),command=pay)
                    button.place(x=180,y=300)

                    button2=Button(cur0,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func)
                    button2.place(x=190,y=340)
                    cur0.mainloop()

            else:
                messagebox.showinfo("  ","  INCORRECT PASSWORD")
            con.commit()
        
    
    
    y=Button(cur,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
    x=Label(cur,text="EMAIL ID     :",bg="white")
    a=Label(cur,text="PHONE NO.       :",bg="white")
    b=Label(cur,text="ENTER PASSWORD                               :",bg="white")
    c=Label(cur,text="RE-ENTER PASSWORD            :",bg="white")

    

    x.place(x=100,y=100)
    a.place(x=100,y=150)
    na.place(x=300,y=100)
    b.place(x=100,y=200)
    ph.place(x=300,y=150)
    c.place(x=100,y=250)
    pas1.place(x=300,y=200)
    he.place(x=50,y=50)
    y.place(x=430,y=0)
    pas2.place(x=300,y=250)
    button=Button(cur,text="PROCEED AND PAY",bg="red",fg="white",font=("titan romans",10,"bold"),command=signup)
    button.place(x=200,y=300)
    cur.mainloop()


def func():
    cur1=Toplevel()
    
    cur1.geometry("650x500")
    cur1.configure(bg="white")

    l=PhotoImage(file="netflix1.png")
    Q1=Label(cur1,image=l,height=51,width=177,bg="white")

    Q1.place(x=0,y=0)
        
    y=Button(cur1,text="Sign In",font=("bebas neue",(10),"bold"),fg="white",bg="red",command=sign)
    z=Label(cur1,text="STEP 1 OF 3",bg="white")
    q=Label(cur1,text="CHOOSE YOUR PLAN.",bg="white",font=("bebas neue",20))
    photo=PhotoImage(file="plans final5.png")
    image=Label(cur1,image=photo).place(x=60,y=120)
    mo=Button(cur1,text="MOBILE",font=("bebas neue",(9),"bold"),bg="red",fg="white",command=lambda:Signup("Mobile"))
    ba=Button(cur1,text="BASIC",font=("bebas neue",(9),"bold"),bg="red",fg="white",command=lambda:Signup("Basic"))
    st=Button(cur1,text="STANDARD",font=("bebas neue",(9),"bold"),bg="red",fg="white",command=lambda:Signup("Standard"))
    pr=Button(cur1,text="PREMIMUM",font=("bebas neue",(9),"bold"),bg="red",fg="white",command=lambda:Signup("Premium"))

    q.place(x=50,y=83)
    z.place(x=51,y=60)
    y.place(x=590,y=0)
    
                
    mo.place(x=268,y=410)
    ba.place(x=365,y=410)
    st.place(x=442,y=410)
    pr.place(x=542,y=410)
   

    cur1.mainloop()


def sign():
  name=StringVar()
  passwd=StringVar()
  curs=Toplevel()
  curs.geometry("400x400")
  curs.configure(bg="White")
  photo=PhotoImage(file="netflix1.png")
  label=Label(curs,image=photo,height=51,width=177,bg="white")
  label.place(x=0,y=0)
                              
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
    
  use=Label(curs,text="USERNAME",font=("bebas neue",10,"bold"),bg="white")

  pas=Label(curs,text="PASSWORD",font=("bebas neue",10,"bold"),bg="white")

  q=Label(curs,text="WELCOME BACK.",font=("bebas neue",20),bg="white")

  username=Entry(curs,textvariable=name,font=("titan romans",16),bg="white")

  passwd=Entry(curs,textvariable=passwd,font=("titan romans",16),bg="white")

  y=Button(curs,text="Sign In",font=(20),bg="white",fg="red",command=new)
 
  use.place(x=150,y=100)
  q.place(x=75,y=62)
  username.place(x=85,y=130)
  pas.place(x=150,y=160)
  passwd.place(x=85,y=190)
  y.place(x=150,y=230)
  curs.mainloop()

m.configure(bg="white")
p=PhotoImage(file="screen1.png")
Q=Label(m,image=p,height=420,width=360,bg="white")
l=PhotoImage(file="netflix1.png")
Q1=Label(m,image=l,height=51,width=177,bg="white")
b=Button(m,text="Sign IN",font=("bebas neue",(10),"bold"),command=sign,bg="red",fg="white")
b1=Button(m,text="SEE THE PLANS",font=(20),bg="red",fg="White",command=func)

Q.place(x=70,y=0)
b1.place(x=175,y=430)
Q1.place(x=0,y=0)
b.place(x=430,y=0)
m.mainloop()

