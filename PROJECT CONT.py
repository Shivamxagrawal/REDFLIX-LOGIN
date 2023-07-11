import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tiger",
    database="system35")















def fav():
    
    global lfav
    lfav=[]
    cont="y"
    while cont=="y":
        print("\t","*"*30)
        print("\t\t  LIST OF GENRE")
        print("\t","*"*30)
        print("\t  1.HORROR")
        print("\t  2.COMEDY")
        print("\t  3.ACTION")
        print("\t  4.KIDS")
        print("\t  5.SI-FI")
        print("\t","*"*30)
        horr=["it chapter 2","hereditary","a quiet place","get out","it chapter one","it follows","the babadook","the conjuring","sinister","paranormal activity","the evil dead","tatiya bichu"]
        com=["deadpool","21 jump street","the hangover","super bad","shaun of the dead","ghost busters","dumb and dumber","animal house","jhonny english reborn","best in show"]
        act=["gladiator","rocky","the matrix","the killer","man on fire","heat","collateral","the fifth element","fast and furious 8","the expendables 3","rambo","predator"]
        kid=["toy story 4","the lego movie 2","the lion king","incredibles 2","wonder park","dora and the lost city","frozen 2","small foot","inside out","despicable me","tangled","toy story 3"]
        si=["arrival","childern of men","interstellar","the martian","inception","avengers:endgame","ad astra","blade runner 2049","star wars","chappie","gravity","attack the block","avtar","serenity"]
        con1=int(input("\t\t enter your choice:"))
        add=""
        temp=""
    
    
    
        if con1==1:
            for i in range(0,len(horr)):
                print("\t  ",i+1,".",horr[i])
                add="y"
            while add=="y":
                con=int(input("\t\t enter movie no . to add to favorates:"))
                temp=horr.pop(con-1)
                lfav.append(temp)
                temp=""
                add=input("\t\t do you want to add more :")
                print("\t\t",lfav)
                
            
        elif con1==2:
            for i in range(0,len(com)):
                print("\t  ",i+1,".",com[i])
                add="y"
            while add=="y":
                con=int(input("\t\t enter movie no . to add to favorates:"))
                temp=com.pop(con-1)
                lfav.append(temp)
                temp=""
                add=input("\t\t do you want to add more :")
                print("\t\t",lfav)
        elif con1==3:
            for i in range(0,len(act)):
                print("\t  ",i+1,".",act[i])
                add="y"
            while add=="y":
                con=int(input("\t\t enter movie no . to add to favorates:"))
                temp=act.pop(con-1)
                lfav.append(temp)
                temp=""
                add=input("\t\t do you want to add more :")
                print("\t\t",lfav)
        
        elif con1==4:
            for i in range(0,len(act)):
                print("\t  ",i+1,".",kid[i])
            add="y"
            while add=="y":
                con=int(input("\t\t enter movie no . to add to favorates:"))
                temp=kid.pop(con-1)
                lfav.append(temp)
                temp=""
                add=input("\t\t do you want to add more :")
                print("\t\t",lfav)
        elif con1==5:
            for i in range(0,len(si)):
                print("\t  ",i+1,".",si[i])
                add="y"
            while add=="y":
                con=int(input("\t\t enter movie no . to add to favorates:"))
                temp=si.pop(con-1)
                lfav.append(temp)
                temp=""
                add=input("\t\t do you want to add more :")
                print("\t\t",lfav)
        cont=input("\t\t do you want to continue :")




cont="y"
while cont=="y":
    print("\t","*"*30)
    print("\t\t  WELCOME TO REDFLIX")
    print("\t  1.ADD TO FAVOURITE")
    #print("\t  2.SHOW FAVOURITE")
    print("\t  2.CHANGE PLAN")
    print("\t  3.CANCEL SUBSCRIPTION")
    print("\t","*"*30)
    cho=int(input("\t\t enter your choice:"))
    if cho==1:
        fav()
    #elif cho==2:
        
    

