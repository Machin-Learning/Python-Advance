import mysql.connector
def delete(id):
    conn = mysql.connector.connect(host = "localhost",user="root",database="mydb")
    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()
        s = "delete from emp where id ='%d'"
        args=(id)
        try:
            cursor.execute(s % args)
            conn.commit()
            print("Employee Deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empId = int(input("Enter the id:"))
delete(empId)