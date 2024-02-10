import os
import platform
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password='',
                             database="securitydbms")
mycursor=mydb.cursor()
def Add_Record_VIP():
    L=[]
    vip_id=int(input("Enter the vip id : "))
    L.append(vip_id)
    name=input("Enter the VIP Name: ")
    L.append(name)
    dob=input("Enter the dob of vip: ")
    L.append(dob)
    gender=input("enter the gender m/f:")
    L.append(gender)
    address=input("Enter the address: ")
    L.append(address)
    phone=int(input("Enter the 10 digit phone no.:"))
    L.append(phone)
    stud=(L)
    sql='insert into VIP(vip_id,name,dob,gender,address,phone) values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql,stud)
    mydb.commit()
def Add_Record_SECURITY():
    L=[]
    vip_id=int(input("Enter the vip id : "))
    L.append(vip_id)
    bid=input("Enter the bodyguard id: ")
    L.append(bid)
    aid=input("Enter the assignment id:")
    L.append(aid)
    sdate=input("enter the start date")
    L.append(sdate)
    edate=input("Enter the end date: ")
    L.append(edate)
    stud=(L)
    sql='insert into SECURITY(vip_id,bodyguard_id,assignment_id,startdate,enddate) values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql,stud)
    mydb.commit()
def Add_Record_BODYGUARD():
    L=[]
    bid=int(input("Enter the bodyguard id : "))
    L.append(bid)
    name=input("Enter the bodyguard Name: ")
    L.append(name)
    gender=input("enter the gender m/f:")
    L.append(gender)
    dob=input("Enter the dob of bodyguard: ")
    L.append(dob)
    address=input("Enter the address: ")
    L.append(address)
    phone=int(input("Enter the 10 digit phone no.:"))
    L.append(phone)
    stud=(L)
    sql='insert into BODYGUARD(bodyguard_id,name,gender,dob,address,phone) values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql,stud)
    mydb.commit()
def Add_Record_GUN():
    L=[]
    gid=int(input("Enter the gun id : "))
    L.append(gid)
    model=input("Enter the model of gun: ")
    L.append(model)
    type=input("enter the gun type:")
    L.append(type)
    sno=input("Enter the serial no. of gun :")
    L.append(sno)
    stud=(L)
    sql='insert into GUN(gun_id,model,type,serial_number) values(%s,%s,%s,%s)'
    mycursor.execute(sql,stud)
    mydb.commit()
def Add_Record_RESOURCES():
    L=[]
    rid=int(input("Enter the resource id : "))
    L.append(rid)
    bid=input("Enter the bodyguard id: ")
    L.append(bid)
    gid=input("enter the gun id:")
    L.append(gid)
    resources=input("Enter the resources used by guard ")
    L.append(resources)
    stud=(L)
    sql='insert into RESOURCES(resource_id,bodyguard_id,gun_id,resources) values(%s,%s,%s,%s)'
    mycursor.execute(sql,stud)
    mydb.commit()
def Rec_View_VIP():
    print("Select the search criteria : ")
    print("1. vip_id")
    print("2. vip name")
    print("3. dob")
    print("4. gender(m/f)")
    print("5. address")
    print("6. phone")
    print("7. all")
    ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter vip_id : "))
       rl=(s,)
       sql="select * from VIP where vip_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==2:
       s=input("Enter VIP Name : ")
       rl=(s,)
       sql="select * from VIP where name=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==3:
       s=int(input("Enter dob : "))
       rl=(s,)
       sql="select * from VIP where dob=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==4:
       s=int(input("Enter gender(m/f): "))
       rl=(s,)
       sql="select * from VIP where gender=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==5:
       s=int(input("Enter address: "))
       rl=(s,)
       sql="select * from VIP where address=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==6:
       s=int(input("Enter phone number: "))
       rl=(s,)
       sql="select * from VIP where phone=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==7:
       sql="select * from VIP"
       mycursor.execute(sql)
       res=mycursor.fetchall()
    
       print("Details about VIP are as follows : ")
       print("(VIP Id,vip name,dob,gender,address,phone)")
    for x in res:
        print(x)
    print('Task completed')
def Rec_View_SECURITY():
    print("Select the search criteria : ")
    print("1. vip_id")
    print("2. bodyguard_id")
    print("3. assignment_id")
    print("4. start date")
    print("5. end date")
    print("6. all")
    ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter vip_id : "))
       rl=(s,)
       sql="select * from SECURITY where vip_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==2:
       s=input("Enter bodyguard_id : ")
       rl=(s,)
       sql="select * from SECURITY where bodyguard_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==3:
       s=int(input("Enter assignment_id: "))
       rl=(s,)
       sql="select * from SECURITY where assignment_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==4:
       s=int(input("Enter start date: "))
       rl=(s,)
       sql="select * from SECURITY where startdate=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==5:
       s=int(input("Enter end date: "))
       rl=(s,)
       sql="select * from SECURITY where enddate=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==6:
       sql="select * from SECURITY"
       mycursor.execute(sql)
       res=mycursor.fetchall()
    
       print("Details about SECURITY are as follows : ")
       print("(VIP Id,bodyguard_id,assignment id ,startdate,enddate)")
    for x in res:
        print(x)
    print('Task completed')
def Rec_View_BODYGUARD():
    print("Select the search criteria : ")
    print("1. bodyguard_id")
    print("2. bodyguard name")
    print("3. dob")
    print("4. gender(m/f)")
    print("5. address")
    print("6. phone")
    print("7. all")
    ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter bodyguard_id : "))
       rl=(s,)
       sql="select * from BODYGUARD where bodyguard_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==2:
       s=input("Enter bodyguard Name : ")
       rl=(s,)
       sql="select * from BODYGUARD where name=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==3:
       s=int(input("Enter dob : "))
       rl=(s,)
       sql="select * from BODYGUARD where dob=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==4:
       s=int(input("Enter gender(m/f): "))
       rl=(s,)
       sql="select * from BODYGUARD where gender=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==5:
       s=int(input("Enter address: "))
       rl=(s,)
       sql="select * from BODYGUARD where address=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==6:
       s=int(input("Enter phone number: "))
       rl=(s,)
       sql="select * from BODYGUARD where phone=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==7:
       sql="select * from BODYGUARD"
       mycursor.execute(sql)
       res=mycursor.fetchall()
    
       print("Details about BODYGUARD are as follows : ")
       print("(bodyguard Id,bodyguard name,dob,gender,address,phone)")
    for x in res:
        print(x)
    print('Task completed')
def Rec_View_RESOURCES():
    print("Select the search criteria : ")
    print("1. resource_id")
    print("2. bodyguard_id")
    print("3. gun_id")
    print("4. resources")
    print("5. all")
    ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter resource_id : "))
       rl=(s,)
       sql="select * from RESOURCES where resource_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==2:
       s=input("Enter BODYGUARD id : ")
       rl=(s,)
       sql="select * from RESOURCES where bodyguard_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==3:
       s=int(input("Enter gun id:"))
       rl=(s,)
       sql="select * from RESOURCES where gun_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==4:
       s=int(input("Enter resources used "))
       rl=(s,)
       sql="select * from RESOURCES where resources=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==5:
       sql="select * from RESOURCES"
       mycursor.execute(sql)
       res=mycursor.fetchall()
    
       print("Details about RESOURCES are as follows : ")
       print("(resource Id,bodyguard id,gun id,resources)")
    for x in res:
        print(x)
    print('Task completed')
def Rec_View_GUN():
    print("Select the search criteria : ")
    print("1. gun_id")
    print("2. model")
    print("3. type")
    print("4. serial number")
    print("5. all")
    ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter gun id : "))
       rl=(s,)
       sql="select * from GUN where gun_id=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==2:
       s=input("Enter model Name : ")
       rl=(s,)
       sql="select * from GUN where model=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==3:
       s=int(input("Enter type : "))
       rl=(s,)
       sql="select * from GUN where type=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==4:
       s=int(input("Enter serial number: "))
       rl=(s,)
       sql="select * from GUN where serial_number=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==5:
       sql="select * from GUN"
       mycursor.execute(sql)
       res=mycursor.fetchall()
    
       print("Details about GUN are as follows : ")
       print("(GUN Id,model ,type,serial number)")
    for x in res:
        print(x)
    print('Task completed')
def remove_VIP():
    vid1=int(input("Enter the vip id of the vip to be deleted : "))
    rl=(vid1,)
    sql="Delete from VIP where vip_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def remove_SECURITY():
    vid1=int(input("Enter the assignment id of the record to be deleted : "))
    rl=(vid1,)
    sql="Delete from SECURITY where assignment_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def remove_BODYGUARD():
    vid1=int(input("Enter the bodyguard id of the bodyguard to be deleted : "))
    rl=(vid1,)
    sql="Delete from BODYGUARD where bodyguard_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def remove_RESOURCES():
    vid1=int(input("Enter the resource_id of the resource to be deleted : "))
    rl=(vid1,)
    sql="Delete from RESOURCES where resource_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def remove_GUN():
    vid1=int(input("Enter the gun id of the gun record to be deleted : "))
    rl=(vid1,)
    sql="Delete from GUN where gun_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def update_VIP_phone():
    vid1=int(input("Enter the vip id of the vip record to be updated : "))
    vid2=int(input("Enter new phone no.: "))
    rl=(vid2,vid1,)
    sql="update VIP set phone=%s where vip_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def update_VIP_address():
    vid1=int(input("Enter the vip id of the vip record to be updated : "))
    vid2=int(input("Enter new address: "))
    rl=(vid2,vid1,)
    sql="update VIP set address=%s where vip_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def update_BODYGUARD_phone():
    vid1=int(input("Enter the Bodyguard id of the bodyguard record to be updated : "))
    vid2=int(input("Enter new phone: "))
    rl=(vid2,vid1,)
    sql="update BODYGUARD set phone=%s where bodyguard_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def update_BODYGUARD_address():
    vid1=int(input("Enter the Bodyguard id of the bodyguard record to be updated : "))
    vid2=int(input("Enter new address: "))
    rl=(vid2,vid1,)
    sql="update BODYGUARD set address=%s where bodyguard_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def update_SECURITY_bodyguardid():
    vid1=int(input("Enter the assignment id of the security record to be updated : "))
    vid2=int(input("Enter new bodyguard id of the new bodyguard assigned: "))
    rl=(vid2,vid1,)
    sql="update SECURITY set bodyguard_id=%s where assignment_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def update_SECURITY_startdate():
    vid1=int(input("Enter the assignment id of the security record to be updated : "))
    vid2=int(input("Enter new start date: "))
    rl=(vid2,vid1,)
    sql="update SECURITY set startdate=%s where assignment_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def update_SECURITY_enddate():
    vid1=int(input("Enter the assignment id of the security record to be updated : "))
    vid2=int(input("Enter new end date: "))
    rl=(vid2,vid1,)
    sql="update SECURITY set enddate=%s where assignment_id=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
def menu():
    print("WELCOME TO OUR SECURITY COMPANY")
    print("1.insert details")
    print("2.view details")
    print("3.update details")
    print("4.delete details")
    input_dt = int(input("Please Select An Above Option: "))
    if(input_dt== 1):
        print("choose the table where you want to insert details ")
        print("1.VIP 2.BODYGUARD 3.SECURITY 4.GUN 5.RESOURCES")
        a=int(input("Please Select An Above Option: "))
        if(a==1):
            Add_Record_VIP()
        elif(a==2):
            Add_Record_BODYGUARD()
        elif(a==3):
            Add_Record_SECURITY()
        elif(a==4):
            Add_Record_GUN()
        elif(a==5):
            Add_Record_RESOURCES()
    elif (input_dt==2):
        print("choose the table from which you want to view details ")
        print("1.VIP 2.BODYGUARD 3.SECURITY 4.RESOURCES 5.GUN")
        a=int(input("Please Select An Above Option: "))
        if(a==1):
            Rec_View_VIP()
        elif(a==2):
            Rec_View_BODYGUARD()
        elif(a==3):
            Rec_View_SECURITY()
        elif(a==4):
            Rec_View_RESOURCES()
        elif(a==5):
            Rec_View_GUN()
    elif (input_dt==3):
        print("choose the table in which you want to update details ")
        print("1.VIP 2.BODYGUARD 3.SECURITY")
        a=int(input("Please Select An Above Option: "))
        if(a==1):
            print("choose the column you want to update")
            print("1.phone 2.address")
            b=int(input("Please Select An Above Option: "))
            if(b==1):
                update_VIP_phone()
            elif(b==2):
                update_VIP_address()
        elif(a==2):
            print("choose the record you want to update")
            print("1.phone 2.address")
            b=int(input("Please Select An Above Option: "))
            if(b==1):
                update_BODYGUARD_phone()
            elif(b==2):
                update_BODYGUARD_address()
        elif(a==3):
            print("choose the record you want to update")
            print("1.bodyguard id 2.start date 3. end date")
            b=int(input("Please Select An Above Option: "))
            if(b==1):
                update_SECURITY_bodyguardid()
            elif(b==2):
                update_SECURITY_startdate()
            elif(b==3):
                update_SECURITY_enddate()
    elif(input_dt==4):
        print("choose the table in which you want to delete details ")
        print("1.VIP 2.BODYGUARD 3.SECURITY 4.RESOURCES 5. GUN")
        a=int(input("Please Select An Above Option: "))
        if(a==1):
            remove_VIP()
        elif(a==2):
            remove_BODYGUARD()
        elif(a==3):
            remove_SECURITY()
        elif(a==4):
            remove_RESOURCES()
        elif(a==5):
            remove_GUN()
menu()
def runAgain():
    runAgn=input('\nwant to run Again Y/N:')
    while(runAgn.lower()=='y'):
        if(platform.system()=='Windows'):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        menu()
        runAgain()
runAgain()
        
        
        
        
        
        
    
        
        
        
    
    



    
