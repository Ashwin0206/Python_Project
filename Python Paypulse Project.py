
f=input('Enter your MySQL passward:')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME TO PAYPULSE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
import mysql.connector as ms
db=ms.connect(host='localhost',user='root',passwd=f)
mycursor=db.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS PAYPULSE')
db.commit()

def createaccount():
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    mycursor.execute('create table if not exists account(Name varchar(50),password varchar(20),card_number BIGINT,Balance BIGINT)')
    w='y'
    while w=='y':
        a=input('Enter your name:')
        a=a.title()
        q1="select*from account where name='{}'".format(a)
        mycursor.execute(q1)
        abc=mycursor.fetchone()
        if abc is None:
            w='n'
            b=input('Add a password:')
            print('ACCOUNT CREATED!!!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~LINK YOUR BANK ACCOUNT~~~~~~~~~~~~~~~~~~~~~~~~~~')
            q='y'
            while q=='y':
                no=int(input('Enter Your Card Number:'))
                if len(str(no))==16:
                    balance=int(input('Enter Your Account Balance:'))
                    mycursor.execute("insert into account (name,password,card_number,Balance)values ('{}','{}',{},{})".format(a,b,no,balance))
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~BANK ACCOUNT LINKED~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    q='n'
                    
                else:
                    print('\n')
                    print('Enter a valid 16 digit Card Number!!!')
                    q=input('Do you want to try again?(y/n):')
        elif a in abc:
            print('USER NAME ALREADY EXISTS!!!')
            w=input('Do you want to try again?(y/n):')
    db.commit()
    
    db.close()    
def verifyaccount():
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    mycursor.execute('create table if not exists account(Name varchar(50),password varchar(20),card_number char(16),Balance int)')
    z='y'
    while z=='y':
        a=input('Enter your name:')
        a=a.title()
        q1="select*from account where name='{}'".format(a)
        mycursor.execute(q1)
        abc=mycursor.fetchone()
        if abc is not None:
            b=input('Enter password:')
            q="select*from account where name='{}' and password='{}'".format(a,b)
            mycursor.execute(q)
            abc=mycursor.fetchone()
            if abc is not None:
                print('LOGIN SUCCESSFUL!!!')
                x=input("Press 'y' to check balance or 'n' to skip:")
                x=x.lower()
                if x=='y':
                    mycursor.execute("select Balance from account where name='{}'".format(a))
                    for x in mycursor:
                            print('YOUR BANK BALANCE IS:',x[0],'RUPEES')
                break
            else:
                print('INCOREECT PASSWORD')
                z=input('Do You Want To Try Again?(y/n):')
        else:
            print("User Name Doesn't Exists")
            z=input('Do You Want To Try Again?(y/n):')
    db.close()
print('\n')
s='y'
while s=='y':
    print('''1.Sign up new account 
2.login to existing account''')
    ch=input('Enter your choice:')
    if ch=='1':
        createaccount()
        break
    elif ch=='2':
        verifyaccount()
        break
    else:
        print('Enter a valid choice(1/2)')
        s=input('Do you want to try again?(y/n):')
input('PRESS ENTER TO SEE MAIN MENU')
#########################################################################################################
def recharge():
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    number=int(input('Enter Phone Number:'))
    choice=input('\n1. 1GB\n2. 2GB\n3. 3GB\nEnter your daily GB requirement:')
    if choice=='1':
        d='y'
        while d=='y':
            print('1GB/DAY PACKS')
            print('1. ₹199,30 Days\n2. ₹299,50 Days\n3. ₹599,84 Days\n4. ₹3499,365 Days')
            amt=int(input('Enter your choice:'))
            if amt==1:
                rs=199
                break
            elif amt==2:
                rs=299
                break
            elif amt==3:
                rs=599
                break
            elif amt==4:
                rs=3499
                break
            else:
                print('Enter a valid choice(1,2,3 or 4)')
                d=input('Do you want to try again?(y/n):')
    elif choice=='2':
        d='y'
        while d=='y':
            print('2GB/DAY PACKS')
            print('1. ₹399,30 Days\n2. ₹499,50 Days\n3. ₹799,84 Days\n4. ₹5499,365 Days')
            amt=int(input('Enter your choice:'))
            if amt==1:
                rs=399
                break
            elif amt==2:
                rs=499
                break
            elif amt==3:
                rs=799
                break
            elif amt==4:
                rs=5499
                break
            else:
                print('Enter a valid choice(1,2,3 or 4)')
                d=input('Do you want to try again?(y/n):')
    #choice3
    elif choice=='3':
        d='y'
        while d=='y':
            print('3GB/DAY PACKS')
            print('1. ₹599,30 Days\n2. ₹699,50 Days\n3. ₹899,84 Days\n4. ₹7499,365 Days')
            amt=int(input('Enter your choice:'))
            if amt==1:
                rs=599
                break
            elif amt==2:
                rs=699
                break
            elif amt==3:
                rs=899
                break
            elif amt==4:
                rs=7499
                break
            else:
                print('Enter a valid choice(1,2,3 or 4)')
                d=input('Do you want to try again?(y/n):')
    s='y'
    while s=='y':
        a=int(input('Enter your card number:'))
        b=input('Enter your password:')
        q1="select balance from account where card_number={} and password='{}'".format(a,b)
        mycursor.execute(q1)
        abc=mycursor.fetchone()
        if abc is not None:
            if int(abc[0])<rs:
                print('Insufficient Balance!!!')
                s=input('Do you want to change card number?(y/n):')
            else:
                print('Payment successful')
                q2="update account set balance=balance-{} where card_number={}".format(rs,a)
                mycursor.execute(q2)
                print('RUPEES', rs,'HAS BEEN DEBITED FROM YOUR ACCOUNT')
                output = f"Rupees {rs} has been recharged to {number}"
                mycursor.execute("create table if not exists transactions(S_No int auto_increment primary key ,history varchar(100))")
                q1="INSERT INTO transactions (history) VALUES ('{}')".format(output)
                mycursor.execute(q1)
                db.commit()
                break
        else:
            print('Ensure you have entered the correct card number and password')
            s=input('DO YOU WANT TO TRY AGAIN?(y/n):')
    db.close()
#######################################################################################
def electricity():
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    z='y'
    while z=='y':
        state=input('Enter your state:')
        state=state.title()
        if state not in india:
            print('Enter The Proper State Name')
            z=input('DO YOU WANT TO TRY AGAIN?(y/n):')
        else:
            number=int(input('Enter your consumer number:'))
            amt=int(input('Enter amount to be paid:'))
            s='y'
            while s=='y':
                a=int(input('Enter your card number:'))
                b=input('Enter your password:')
                q1="select balance from account where card_number={} and password='{}'".format(a,b)
                mycursor.execute(q1)
                abc=mycursor.fetchone()
                if abc is not None:
                    if int(abc[0])<amt:
                        print('Insufficient Balance!!!')
                        s=input('Do you want to change card number?(y/n):')
                    else:
                        print('Payment successful')
                        q2="update account set balance=balance-{} where card_number={}".format(amt,a)
                        mycursor.execute(q2)
                        db.commit()
                        print('RUPEES', amt,'HAS BEEN DEBITED FROM YOUR ACCOUNT')
                        mycursor.execute("create table if not exists transactions(S_No int auto_increment primary key ,history varchar(100))")
                        output = f"Rupees {amt} has been paid for electricity bill for {number}"
                        q1="INSERT INTO transactions (history) VALUES ('{}')".format(output)
                        mycursor.execute(q1)
                        db.commit()
                        z,s='n','n'
            
                else:
                    print('Ensure you have entered the correct card number and password')
                    s=input('DO YOU WANT TO TRY AGAIN?(y/n):')
            
    
    db.close()
########################################################################################################################################
def deposit():
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    s='y'
    while s=='y':
        a=int(input('Enter your card number:'))
        b=input('Enter your password:')
        q1="select balance from account where card_number={} and password='{}'".format(a,b)
        mycursor.execute(q1)
        abc=mycursor.fetchone()
        if abc is not None:
            amt=int(input('Enter amount to be deposited:'))
            print('Deposited successfully')
            q2="update account set balance=balance+{} where card_number={}".format(amt,a)
            mycursor.execute(q2)
            db.commit()
            s='n'
        else:
            print('Ensure you have entered the correct card number and password')
            s=input('DO YOU WANT TO TRY AGAIN?(y/n):')
    db.close()
######################################################################################
def broadband():
    import mysql.connector as ms
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    a=input('Enter your operator:')
    b=input('Enter your account number:')
    input('PRESS ENTER TO SEE YOUR BILL')
    import random
    n=random.randint(499,1500)
    print(' OPERATOR:',a,'\n','ACCOUNT NUMBER:',b,'\n','AMOUNT TO BE PAID:',n,'RUPEES')
    s='y'
    while s=='y':
        a=input('Enter your card number:')
        b=input('Enter your password:')
        q1="select balance from account where card_number='{}' and password='{}'".format(a,b)
        mycursor.execute(q1)
        abc=mycursor.fetchone()
        if abc is not None:
            if int(abc[0])<n:
                print('Insufficient Balance!!!')
                s=input('Do you want to change card number?(y/n):')
            else:
                print('Payment successful')
                q2="update account set balance=balance-{} where card_number='{}'".format(n,a)
                mycursor.execute(q2)
                db.commit()
                print('RUPEES', n,'HAS BEEN DEBITED FROM YOUR ACCOUNT')
                mycursor.execute("create table if not exists transactions(S_No int auto_increment primary key ,history varchar(100))")
                output = f'Rupees {n} has been recharged to {a} broadband connection'
                q1="INSERT INTO transactions (history) VALUES ('{}')".format(output)
                mycursor.execute(q1)
                db.commit()
                s='n'
        else:
            print('Ensure you have entered the correct card number and password')
            s=input('DO YOU WANT TO TRY AGAIN?(y/n):')
    for x in mycursor:
        print(x)
    db.close()
#########################################################################################################
def history():
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    p='y'
    while p=='y':
        a=int(input('Enter your card number:'))
        b=input('Enter your password:')
        mycursor.execute("select*from account where card_number={} and password='{}'".format(a,b))
        qwerty=mycursor.fetchone()
        if qwerty is None:
            print('ENSURE YOU HAVE ENTERED THE CORRECT CARD NUMBER AND PASSWORD')
            p=input('DO YOU WANT TO TRY AGAIN?(y/n):')
        else:
            mycursor.execute("select*from transactions")
            abc=mycursor.fetchall()
            print('T.NO                  HISTORY')
            for x in abc:
                print(' ',x[0],'  ',x[1])
            h=input('Do You Want To Delete the transaction?(y/n):')
            if h=='y':
                d=int(input('Enter the transaction number of the transaction to be deleted:'))
                mycursor.execute('delete from transactions where S_No={}'.format(d))
                db.commit()
                print('~~~~~~~~~~~~~~~~~TRANSACTION DELETED SUCCESSFULLY~~~~~~~~~~~~~~~~~~~~~')
                p='n'
            else:
                pass
                p='n'
    db.close()
def balance():
    db=ms.connect(host='localhost',user='root',passwd=f,database='PAYPULSE')
    mycursor=db.cursor()
    h='y'
    while h=='y':
        z=input('Enter you card number:')
        w=input('Enter you passward:')
        mycursor.execute("select card_number,password from account where card_number='{}' and password='{}'".format(z,w))
        abc=mycursor.fetchone()
        if abc is not None:
                mycursor.execute("select balance from account where card_number='{}' and password='{}'".format(z,w))
                for x in mycursor:
                        print('YOUR BANK BALANCE IS:',x[0],'RUPEES')
                break
        else:
            print('Ensure you have entered the correct card number and password!!!')
            h=input('Do You Want To Try Again?(y/n):')
#############################################################################################################
sdf='y'
while sdf=='y':
    print('\n1.RECHARGE PHONE BILL \t 2.PAY ELECTRICITY BILL \t 3.DEPOSIT MONEY\n4.PAY BROADBANDBILL\t 5.TRANSACTION HISTORY  \t 6.CHECK BALANCE\n')
    ch=int(input('Enter your choice:'))
    if ch==1:
        recharge()
    elif ch==2:
        electricity()
    elif ch==3:
        deposit()
    elif ch==4:
        broadband()
    elif ch==5:
        history()
    elif ch==6:
        balance()
    else:
        print('Enter a valid choice(1-6)')
    sdf=input('Do you want to go to main menu?(y/n):')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~THANK YOU FOR USING PAYPULSE~~~~~~~~~~~~~~~~~~~~~~~~~')   
    

