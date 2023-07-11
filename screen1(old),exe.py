
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

Pac=StringVar()

import mysql.connector
con=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="tiger",
            database="system35")

cursor1=con.cursor()

def Signup(a):
    Pac.set(a)
    
    cur0=Toplevel()
    cur0.geometry("500x500")
    cur0.configure(bg="white")
    he=Label(cur0,text="Step 2 of 3",font=("bebas neue",15),bg="white")
    de=Label(cur0,text="ENTER YOUR DETAILS")
    photo=PhotoImage(file="netflix1.png")
    label=Label(cur0,image=photo,height=51,width=177,bg="white")
    label.place(x=0,y=0)
    
    y=Button(cur0,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
    x=Label(cur0,text="EMAIL ID     :",bg="white")
    a=Label(cur0,text="PHONE NO.       :",bg="white")
    b=Label(cur0,text="ENTER PASSWORD                               :",bg="white")
    c=Label(cur0,text="RE-ENTER PASSWORD            :",bg="white")

    email=StringVar()
    phone=IntVar()
    passwd1=StringVar()
    passwd2=StringVar()

    na=Entry(cur0,textvariable=email)
    ph=Entry(cur0,textvariable=phone)
    pas1=Entry(cur0,textvariable=passwd1,show='*')
    pas2=Entry(cur0,textvariable=passwd2,show='*')

    email1=na.get()
    ph1=ph.get()
    pass1=pas1.get()
    pass2=pas2.get()

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


    def signup():
        
        
        email1=email.get()
        ph1=phone.get()
        pass1=passwd1.get()
        pass2=passwd2.get()

        
        a=Pac.get()

        if pass1==pass2:

            sql="insert into subscriber values('"+str(email1)+"',"+str(ph1)+",'"+str(pass1)+"')"
            cursor1.execute(sql)
            con.commit()

            if a=="Basic":
                
                cur=Toplevel()
                def pay():
                        
                        a="Basic"
                        noc1=noc.get()
                        cn1=cn.get()
                        vu1=vu.get()
                        
                        import mysql.connector
                        con=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="tiger",
                        database="system35")
                        cursor1=con.cursor()
                        print(noc1,",",cn1)
                        sql="insert into pay values('"+str(noc1)+"','"+str(cn1)+"','"+str(a)+"');"    
                        cursor1.execute(sql)
                        messagebox.showinfo("  ","Rs.499 has been debited")
                        con.commit()
                        
                cur.geometry("500x500")
                cur.configure(bg="white")
                he=Label(cur,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                de=Label(cur,text="ENTER your payment details",bg="white")
                l=PhotoImage(file="netflix1.png")
                Q1=Label(cur,image=l,height=51,width=177,bg="white")
                y=Button(cur,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                x=Label(cur,text="Email         :",bg="white")
                the=Label(cur,text="(SHOURD BE  SAME AS PREVIOUS)",font=("bebas neue",6),fg='red',bg="white").place(x=100,y=140)
                a=Label(cur,text="CARD NUMBER       :",bg="white")
                b=Label(cur,text="VALID UPTO            :",bg="white")
                c=Label(cur,text="CVV                          :",bg="white")

                noc=StringVar()
                cn=StringVar()
                vu=StringVar()
                cvv=StringVar()

                na=Entry(cur,textvariable=noc)
                ph=Entry(cur,textvariable=cn)
                pas1=Entry(cur,textvariable=vu)
                pas2=Entry(cur,textvariable=cvv)

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
                a="Basic"
                button=Button(cur,text="PROCEED TO PAY Rs.499",bg="red",fg="white",font=("titan romans",10,"bold"),command=lambda:pay())
                button.place(x=180,y=300)

                button2=Button(cur,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func())
                button2.place(x=190,y=340)
                cur.mainloop()
            elif a=="Mobile":
                
                def pay():
                        a="Mobile"
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
                        sql="insert into pay values('"+str(noc1)+"','"+str(cn1)+"','"+str(a)+"');"    
                        cursor1.execute(sql)
                        messagebox.showinfo("  ","Rs.199 has been debited")
                        
                        con.commit()
                       
                cur=Toplevel()
                cur.geometry("500x500")
                cur.configure(bg="white")
                he=Label(cur,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                de=Label(cur,text="ENTER your payment details",bg="white")
                l=PhotoImage(file="netflix1.png")
                Q1=Label(cur,image=l,height=51,width=177,bg="white")
                y=Button(cur,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                x=Label(cur,text="Email        :",bg="white")
                the=Label(cur,text="(SHOURD BE  SAME AS PREVIOUS)",font=("bebas neue",6),fg='red',bg="white").place(x=100,y=140)
                a=Label(cur,text="CARD NUMBER       :",bg="white")
                b=Label(cur,text="VALID UPTO            :",bg="white")
                c=Label(cur,text="CVV                          :",bg="white")

                noc=StringVar()
                cn=StringVar()
                vu=StringVar()
                cvv=StringVar()

                na=Entry(cur,textvariable=noc)
                ph=Entry(cur,textvariable=cn)
                pas1=Entry(cur,textvariable=vu)
                pas2=Entry(cur,textvariable=cvv)

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



                button=Button(cur,text="PROCEED TO PAY Rs.199",bg="red",fg="white",font=("titan romans",10,"bold"),command=lambda:pay())
                button.place(x=180,y=300)
                button2=Button(cur,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func)
                button2.place(x=190,y=340)
                cur.mainloop()
            elif a=="Standard":
                    
                    def pay():
                            a="Standard"
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
                            sql="insert into pay values('"+str(noc1)+"','"+str(cn1)+"','"+str(a)+"');"    
                            cursor1.execute(sql)
                            messagebox.showinfo("  ","Rs.649 has been debited")
                            con.commit()
                            
                            
                    cur=Toplevel()
                    cur.geometry("500x500")
                    cur.configure(bg="white")
                    he=Label(cur,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                    de=Label(cur,text="ENTER your payment details",bg="white")
                    l=PhotoImage(file="netflix1.png")
                    Q1=Label(cur,image=l,height=51,width=177,bg="white")
                    y=Button(cur,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                    x=Label(cur,text="Email     :",bg="white")
                    the=Label(cur,text="(SHOURD BE  SAME AS PREVIOUS)",font=("bebas neue",6),fg='red',bg="white").place(x=100,y=140)
                    a=Label(cur,text="CARD NUMBER       :",bg="white")
                    b=Label(cur,text="VALID UPTO            :",bg="white")
                    c=Label(cur,text="CVV                          :",bg="white")
                    
                    noc=StringVar()
                    cn=StringVar()
                    vu=StringVar()
                    cvv=StringVar()
                    
                    na=Entry(cur,textvariable=noc)
                    ph=Entry(cur,textvariable=cn)
                    pas1=Entry(cur,textvariable=vu)
                    pas2=Entry(cur,textvariable=cvv)
                    
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
                    button=Button(cur,text="PROCEED TO PAY Rs.649",bg="red",fg="white",font=("titan romans",10,"bold"),command=lambda:pay())
                    button.place(x=180,y=300)
                    button2=Button(cur,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func)
                    button2.place(x=190,y=340)
                    cur.mainloop()
            elif a=="Premium":
                    
                    cur=Toplevel()
                    def pay():
                            a="Premium"
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
                            sql="insert into pay values('"+str(noc1)+"','"+str(cn1)+"','"+str(a)+"');"    
                            cursor1.execute(sql)
                            messagebox.showinfo("  ","Rs.799 has been debited")
                            con.commit()    
                            
                            
                    cur.geometry("500x500")
                    cur.configure(bg="white")
                    he=Label(cur,text="Step 3 of 3",font=("bebas neue",15),bg="white")
                    de=Label(cur,text="ENTER your payment details",bg="white")
                    l=PhotoImage(file="netflix1.png")
                    Q1=Label(cur,image=l,height=51,width=177,bg="white")
                    y=Button(cur,text="Sign In",font=("bebas neue",(10),"bold"),bg="red",fg="white",command=sign)
                    the=Label(cur,text="(SHOURD BE  SAME AS PREVIOUS)",font=("bebas neue",6),fg='red',bg="white").place(x=100,y=140)
                    x=Label(cur,text="Email           :",bg="white")
                    
                    a=Label(cur,text="CARD NUMBER       :",bg="white")
                    b=Label(cur,text="VALID UPTO            :",bg="white")
                    c=Label(cur,text="CVV                          :",bg="white")
                    noc=StringVar()
                    cn=StringVar()
                    vu=StringVar()
                    cvv=StringVar()
                    na=Entry(cur,textvariable=noc)
                    ph=Entry(cur,textvariable=cn)
                    pas1=Entry(cur,textvariable=vu)
                    pas2=Entry(cur,textvariable=cvv)

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

                    button=Button(cur,text="PROCEED TO PAY Rs.799",bg="red",fg="white",font=("titan romans",10,"bold"),command=lambda:pay())
                    button.place(x=180,y=300)

                    button2=Button(cur,text="CHOOSE DIFFERENT PLAN",bg="red",fg="white",font=("titan romans",8,"bold"),command=func)
                    button2.place(x=190,y=340)
                    cur.mainloop()

        else:
            messagebox.showinfo("  ","  INCORRECT PASSWORD")
        con.commit()

    button=Button(cur0,text="PROCEED AND PAY",bg="red",fg="white",font=("titan romans",10,"bold"),command=signup)
    button.place(x=200,y=300)
    cur0.mainloop()
    





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
  
  cur2=Toplevel()
  cur2.geometry("400x400")
  cur2.configure(bg="White")
  photo=PhotoImage(file="netflix1.png")
  label=Label(cur2,image=photo,height=51,width=177,bg="white")
  label.place(x=0,y=0)
                              
  def new():
    name1=name.get()
    passwd1=passwd.get()                            
    
    
    sql="select Email_id,password from subscriber"
    c=0
    cursor1.execute(sql)
    data=cursor1.fetchall()
    
    for i in data:
        
        if i[0]==name1 and i[1]==passwd1:
            messagebox.showinfo("  ","LOGIN COMPLETE")
            def bill():
                sql1="select * from subscriber where email_id = '"+str(name1)+"'"
    
                cursor1.execute(sql1)
                data1=cursor1.fetchall()
                sql2="select * from pay where name = '"+str(name1)+"'"
                cursor1.execute(sql2)
                data2=cursor1.fetchall()
                print("\t","*"*45)
                print("\t\t           DETAILS")
                print("\t","*"*45)
                print("\t\tEmail       :"+str(name1))
                print("\t\tPhone number:"+str(data1[0][1]))
                print("\t\tCard number :"+str(data2[0][1]))
                print("\t\tPack        :"+str(data2[0][2]))
    
            def fav():  
                lfav=[]
                cont="y"
                while cont=="y":
                    print("\t","*"*45)
                    print("\t\t         LIST OF GENRE")
                    print("\t","*"*45)
                    print("\t\t         1.HORROR")
                    print("\t\t         2.COMEDY")
                    print("\t\t         3.ACTION")
                    print("\t\t         4.KIDS")
                    print("\t\t         5.SI-FI")
                    print("\t","*"*45)
                    horr=["it chapter 2","hereditary","a quiet place","get out","it chapter one","it follows","the babadook","the conjuring","sinister","paranormal activity","the evil dead","tatiya bichu"]
                    com=["deadpool","21 jump street","the hangover","super bad","shaun of the dead","ghost busters","dumb and dumber","animal house","jhonny english reborn","best in show"]
                    act=["gladiator","rocky","the matrix","the killer","man on fire","heat","collateral","the fifth element","fast and furious 8","the expendables 3","rambo","predator"]
                    kid=["toy story 4","the lego movie 2","the lion king","incredibles 2","wonder park","dora and the lost city","frozen 2","small foot","inside out","despicable me","tangled","toy story 3"]
                    si=["arrival","childern of men","interstellar","the martian","inception","avengers:endgame","ad astra","blade runner 2049","star wars","chappie","gravity","attack the block","avtar","serenity"]
                    con1=int(input("\t\t        Enter your choice:"))
                    add=""
                    temp=""
                    print("\t","*"*45)
                    F=open(str(name1)+".txt",'a')
                    if con1==1:
                        print("\t\t          HORROR MOVIES")
                        print("\t","*"*45)
                        for i in range(0,len(horr)):
                            print("\t\t     ",i+1,".",horr[i])
                        print("\t","*"*45)
                        add="y"
                        while add=="y":
                    
                            con=int(input("\t     Enter your favourite movie number:"))
                            temp=horr.pop(con-1)
                            F.writelines(str(temp)+"\n")
                            temp=""
                            add=input("\t     Do you want to add more horror movies :")
                        print("\t","*"*45)
                    
                
            
                    elif con1==2:
                        print("\t\t          COMEDY MOVIES")
                        print("\t","*"*45)
                        for i in range(0,len(com)):
                            print("\t\t     ",i+1,".",com[i])
                            add="y"
                        print("\t","*"*45)
                        while add=="y":
                            con=int(input("\t     Enter movie no . to add to favorates:"))
                            temp=com.pop(con-1)
                            F.writelines(str(temp)+"\n")
                            temp=""
                            add=input("\t     Do you want to add more comdey movies :")
                        print("\t","*"*45)

            
                    elif con1==3:
                        print("\t\t          ACTION MOVIES")
                        print("\t","*"*45)
                        for i in range(0,len(act)):
                            print("\t\t     ",i+1,".",act[i])
                        add="y"
                        print("\t","*"*45)
                        while add=="y":
                            con=int(input("\t     Enter movie no . to add to favorates:"))
                            temp=act.pop(con-1)
                            F.writelines(str(temp)+"\n")
                            temp=""
                            add=input("\t     Do you want to add more action movies:")
                        print("\t","*"*45)
        
                    elif con1==4:
                        print("\t\t          KIDS MOVIES")
                        print("\t","*"*45)
                        for i in range(0,len(act)):
                            print("\t\t     ",i+1,".",kid[i])
                        add="y"
                        print("\t","*"*45)
                        while add=="y":
                            con=int(input("\t     Enter movie no . to add to favorates:"))
                            temp=kid.pop(con-1)
                            F.writelines(str(temp)+"\n")
                            temp=""
                            add=input("\t     Do you want to add more kid movies:")
                        print("\t","*"*45)
                    elif con1==5:
                
                        print("\t\t          SCI-FI MOVIES")
                        print("\t","*"*45)
                        for i in range(0,len(si)):
                            print("\t\t     ",i+1,".",si[i])
                        add="y"
                        print("\t","*"*45)
                        while add=="y":
                    
                            con=int(input("\t     Enter movie no . to add to favorates:"))
                            temp=si.pop(con-1)
                    
                            F.writelines(str(temp)+"\n")
                    
                            temp=""
                            add=input("\t     Do you want to add more sci-fi:")
                        print("\t","*"*45)
            
                    cont=input("\t\t Do you want to add movies:")
                    F.close()
                
            
            def show():
                c=0
                print("\t","*"*45)
                print("\t\t    YOUR FAVOURITE MOVIES")
                Z=open(name1+".txt",'r')
                z=Z.readlines()
                print("\t","*"*45)
                for i in range(len(z)):
                    c+=1
                    print("\t\t     ",c,".",z[i])
                Z.close()
            def change():
                print("\t","*"*45)
                print("\t\t          CHANGE PLAN")
                print("\t","*"*45)
                print("\t\t          1. Mobile")
                print("\t\t          2. Basic")
                print("\t\t          3. Standard")
                print("\t\t          4. Premium")
                print("\t","*"*45)
                ch=int(input("\t\t       Enter your choice:"))
                if ch==1:
                    sql="update pay set pack = 'Mobile' Where Name = '"+str(name1)+"'"
                    print("\t\t => Plan Changed Successfully<=")
                    cursor1.execute(sql)
                elif ch==2:
                    sql="update pay set pack = 'Basic' Where Name = '"+str(name1)+"'"
                    print("\t\t => Plan Changed Successfully<=")
                    cursor1.execute(sql)
                elif ch==3:
                    sql="update pay set pack = 'Standard' Where Name = '"+str(name1)+"'"
                    print("\t\t => Plan Changed Successfully<=")
                    cursor1.execute(sql)
                elif ch==4:
                    sql="update pay set pack = 'Premium' Where Name = '"+str(name1)+"'"
                    print("\t\t => Plan Changed Successfully<=")
                    cursor1.execute(sql)
                else:
                    print("Invalid")
            
            cont="y"
            while cont=="y":
                print("\t","*"*45)
                print("\t\t       WELCOME TO REDFLIX")
                print("\t","*"*45)
                print("\t\t       1.ADD TO FAVOURITE")
                print("\t\t       2.SHOW FAVOURITES")
                print("\t\t       3.SHOW DETAILS")
                print("\t\t       4.CHANGE PLAN")
                print("\t\t       5.CANCEL SUBSCRIPTION")
                print("\t","*"*45)
                cho=int(input("\t\t       Enter your choice:"))
       
                if cho==1:
                    fav()
                elif cho==2:
                    show()
                elif cho==3:
                    bill()
                elif cho==4:
                    change()
                elif cho==5:
                    print("\t","*"*45)
                    print("\t\tCANCEL SUBSCRIPTION")
                    print("\t","*"*45)
                    a=input("\t\tDo you really want to cancel ?")
                    if a in "yY":
                        sql="delete from pay where name = '"+str(name1)+"'"
                        cursor1.execute(sql)
                        sql="delete from subscriber where email_id = '"+str(name1)+"'"
                        cursor1.execute(sql)
                        print("\t\t =>Your subscription is successfully canceled<=")
                    else:
                        print("\t\t         =>Subscription not canceled<=")
        
            
                print("\t","*"*45)
        
                
                cont=input("\t\t  Do you wan to continue(y/n):")
            break
            
    else:
        messagebox.showinfo("  ","username or password is invalid")
    
     
    

  use=Label(cur2,text="USERNAME",font=("bebas neue",10,"bold"),bg="white")

  pas=Label(cur2,text="PASSWORD",font=("bebas neue",10,"bold"),bg="white")

  q=Label(cur2,text="WELCOME BACK.",font=("bebas neue",20),bg="white")

  username=Entry(cur2,textvariable=name,font=("titan romans",16),bg="white")

  passwd=Entry(cur2,textvariable=passwd,show="*",font=("titan romans",16),bg="white")

  y=Button(cur2,text="Sign In",font=(20),bg="white",fg="red",command=new)

 
  use.place(x=150,y=100)
  q.place(x=75,y=62)
  username.place(x=85,y=130)
  pas.place(x=150,y=160)
  passwd.place(x=85,y=190)
  y.place(x=150,y=230)
  cur2.mainloop()
  



  

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


