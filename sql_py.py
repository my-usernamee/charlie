from datetime import datetime
import mysql.connector
con=mysql.connector.connect(host="localhost", user="root",password="root",charset="utf8")
cur=con.cursor()
cur.execute("use charlie")

def add_pt():
    adddate=input("Enter Date to Add [yyyy-mm-dd]: ")
    ptname=input("Enter  PT Name: ")
    fallout_pt=input("Enter the Fallout 4D's with a comma: ")
    try:
        sql="insert into pt_conduct (PT_DATE,PT_NAME,FALLOUT) VALUES(%s,%s,%s);"
        val=(adddate,ptname,fallout_pt)
        cur.execute(sql,val)
        con.commit()
        cur.execute("SELECT * FROM pt_conduct")
        myresult = cur.fetchall()
        for x in myresult:
            print(x)
        sql2="ALTER TABLE pt_dates ADD `%s` varchar(255);" % (adddate)
        cur.execute(sql2)
        con.commit()


        """"sql3="select FALLOUT from pt_conduct ORDER BY Id DESC LIMIT 1;"
        cur.execute(sql3)
        myresult3 = cur.fetchone()
        txt=myresult3[0]
        x3=txt.split(",")

        #------------------------------Main Program Starts Here---------------------------
        for i in x3:
            sql5="UPDATE pt_dates SET `%s` = 0 WHERE 4D = %s;"
            val5=(adddate,i)
            cur.execute(sql5,val5)
            con.commit()

        sql7="UPDATE pt_dates SET `%s` = 1 WHERE `%s` IS NULL;"
        val7=(adddate,adddate)
        cur.execute(sql7,val7)
        con.commit"""""
        
    except:
        print("Error!")

def  del_pt():
    deldate=input("Enter Date to Delete [yyyy-mm-dd]: ")
    sql='select * FROM pt_conduct where PT_DATE=\"%s\";' % (deldate)
    cur.execute(sql)
    myres = cur.fetchall()
    for y in myres:
        print(y)

    try:
        a=int(input("Enter the s.no you wish to delete: "))
        temp_val=(a,)
        sql="delete from pt_conduct where Id=%s;"
        cur.execute(sql,temp_val)
        con.commit()
        cur.execute("SELECT * FROM pt_conduct")
        myresult = cur.fetchall()
        for x in myresult:
            print(x)
    except:
        print("Error!")

def show_pt():
    print("(DATE_OF_CONDUCT,PT_NAME,SERIAL_NUMBER, 4D'S FALLOUT)")
    cur.execute("SELECT * FROM pt_conduct")
    myresult = cur.fetchall()
    for x in myresult:
        print(x)

def link_fallout(): #adddate
    adddate=input("Enter Date to Add [yyyy-mm-dd]: ")
    sql="select FALLOUT from pt_conduct ORDER BY Id DESC LIMIT 1;"
    cur.execute(sql)
    myresult = cur.fetchone()
    txt=myresult[0]
    x=txt.split(",")
    print(x)
    #------------------------------Main Program Starts Here---------------------------
    for i in x:
        sql="UPDATE pt_dates SET `%s` = 0 WHERE 4D = %s;"
        val=(adddate,i)
        cur.execute(sql,val)
        con.commit()

    sql2="UPDATE pt_dates SET `%s` = 1 WHERE `%s` IS NULL;"
    val2=(adddate,adddate)
    cur.execute(sql2,val2)
    con.commit

def fetch_column_name():
    cur.execute("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'pt_dates';")
    myresult = cur.fetchall()
    a=[]
    for x in myresult:
        a.append(x[0])
    #print(a)

def ha_status():
    cur.execute("select 4D FROM pt_dates;")
    myresult = cur.fetchall()
    b=[]
    for xx in myresult:
        b.append(xx[0])
    print(b)
    for yy in b:
        sql="select * FROM pt_dates where 4D = %s;" % (yy)
        cur.execute(sql)
        res = cur.fetchone()
        print(res)

        if len(res)<6:
            print("bye bye")                   #look if less than 3 PT
        else:
            lastthreedates=[]
            zz=len(res)-1
            
            for zzz in range(zz,-1,-1):
                if res[zzz]=="1":
                    cur.execute("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'pt_dates';")
                    myresult = cur.fetchall()
                    a=[]
                    for x in myresult:
                        a.append(x[0])
                    
                    date=a[zzz]
                    lastthreedates.append(date)
                else:
                    continue


            dates_wanted=lastthreedates[0:3]
            a=lastthreedates[0]
            j,k,l=a.split("-")
            dateIs = datetime(int(j),int(k),int(l))
            z = dateIs.toordinal()

            b=lastthreedates[1]
            jj,kk,ll=b.split("-")
            dateIs = datetime(int(jj),int(kk),int(ll))
            y = dateIs.toordinal()

            c=lastthreedates[2]
            jjj,kkk,lll=c.split("-")
            dateIs = datetime(int(jjj),int(kkk),int(lll))
            x = dateIs.toordinal()

            ha = 1 #assuming HA=true at the start 
            ha1=x+14
            while True:
                if y>ha1:
                    print("ha lost(1)")
                    break
                elif y<ha1 and ha==1:
                    d=z-y #duration
                    if z>ha1:
                        print("ha lost(2)")
                        break
                    elif d<=7 and z<ha1:
                        print("ha true(1)")
                        ha1=z+14
                        y=z
                        break
                    elif d>7:
                        ha = 2 #means pending
                        print("ha pending")
                        break
                    print("ha lost(3)")
                    break

def show_last_three_pt():
    yy=input("ENTER THE 4D FOR WHICH YOU WANNA CHECK THE LAST 3 PT HISTORY: ")
    sql="select * FROM pt_dates where 4D = %s;" % (yy)
    cur.execute(sql)
    res = cur.fetchone()
    print(res)

    if len(res)<6:
        print("bye bye")                   #look if less than 3 PT
    else:
        lastthreedates=[]
        zz=len(res)-1
        
        for zzz in range(zz,-1,-1):
            if res[zzz]=="1":
                cur.execute("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'pt_dates';")
                myresult = cur.fetchall()
                a=[]
                for x in myresult:
                    a.append(x[0])
                
                date=a[zzz]
                lastthreedates.append(date)
            else:
                continue


        dates_wanted=lastthreedates[0:3]
        print(dates_wanted)
  
print("WELCOME TO CHARLIE SECURE SYSTEM ")
username=input("Enter your username : ")
password=input("Enter your password : ")
if username=="charlie" and password=="3SIR":
    print("\nLOGIN SUCCESSFUL\n")
    option=int(input("what do you want to check boss? \n 1.ADD PT CONDUCT \n 2. SHOW PT CONDUCTS \n 3.PREV 3D TAKEN BY PERSON \n 4.HA STATUS \n Kindly Type The Number : "))
    if option == 1:
        add_pt()
        #link_fallout()
    elif option ==2:
        show_pt()
    elif option ==3:
        show_last_three_pt()
    elif option ==4:
        ha_status()
    else:
        print("bro are u stupid?")



    




""""else:
    print(" GO AWAYYYYYYY!")"""""
               



"""cur.execute("select * FROM pt_dates where 4D = 1101;")
res = cur.fetchone()
print(res)

if res[3]=="0":
    print("hi")
"""

