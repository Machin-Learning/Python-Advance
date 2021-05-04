import mysql.connector
def update(id,name,sal):
    conn = mysql.connector.connect(host = "localhost",user="root",database="mydb")
    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()
        s = "update emp set name='%s',sal ='%d' where id ='%d'"
        args=(name,sal,id)

        try:
            cursor.execute(s % args)
            conn.commit()
            print("Employee Updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empId = int(input("Enter the id:"))

update(4, "Alis", 65000)