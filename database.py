import mysql.connector as a

cn=a.connect(host='localhost',username='root',password='Dhruv123',database='student')
def insert():
    f=input("Enter the first name: ")
    l=input("Enter the last name: ")
    r=int(input("Enter the roll number: "))
    d=(f,l,r)
    sql1="insert into st values (%s,%s,%s);"
    c=cn.cursor()
    c.execute(sql1,d)
    cn.commit()
    cn.close()
    print("Inserted successfully!")

def deleted():
    c4=cn.cursor()
    s1=int(input("Enter the roll number:"))
    d=(s1)
    sql1="DELETE FROM st WHERE roll_num=%s"
    c4.execute(sql1,d)
    cn.commit()
    cn.close()
    print("Deleted Successfully!")


def update():
    upd=input("""What do you want to update ?
                 1. For updating first name type fn
                 2. For updating last name type ln
                 3.  For updating roll number type rn\n""")
    if (upd=="fn"):
        c=cn.cursor()
        sql="SELECT first_name from st WHERE roll_num=%s;"
        id=int(input("Please enter the current roll_number: "))
        d=[id]
        e=c.execute(sql,d)
        results=c.fetchall()
        count=0
        e=""
        for rw in results:
            e=rw
            count+=1
        print("The name is:",e[0])
        if (count==1):
            name=input("Please enter the new first name : ")
            d=[name,id]
            sql1="UPDATE st SET first_name=%s WHERE roll_num=%s;"
            c.execute(sql1,d)
            cn.commit()
            c.close()
            cn.close()
            print("New first name updated successfully!")
    if (upd=="ln"):
        c=cn.cursor()
        sql="SELECT last_name from st WHERE roll_num=%s;"
        id=int(input("Please enter the current roll_number: "))
        d=[id]
        e=c.execute(sql,d)
        results=c.fetchone()
        e=results[0]
        print("The name is:",e)
        if (len(e)>0):
            name=input("Please enter the new last name : ")
            dt=[name,id]
            sql1="UPDATE st SET last_name=%s WHERE roll_num=%s;"
            c.execute(sql1,dt)
            cn.commit()
            c.close()
            cn.close()
            print("New last name updated successfully!")
    if (upd=="rn"):
        Rn=int(input("Please enter the current roll number: "))
        Rnum=int(input("Please enter the new roll number : "))
        data=(Rnum,Rn)
        sql3="UPDATE st SET roll_num=%s WHERE roll_num=%s;"
        c=cn.cursor()
        c.execute(sql3,data)
        cn.commit()
        cn.close()
        print("New roll number updated successfully!")

print("Welcome to the STUDENT MANAGEMENT")
print("1. TO INSERT DATA")
print("2. TO UPDATE DATA")
print("3. TO DELETE DATA")
print("4. EXIT")
print('***************')
ch=0
while (ch<=4):
    ch=int(input('Enter the choice number: '))
    if (ch==1):
        insert()
        break
    if (ch==2):
        update()
        break
    if (ch==3):
        deleted()
        break
    if (ch==4):
        exit()
else:
        print("Please enter appropriate number")



