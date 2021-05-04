import psycopg2

conn = psycopg2.connect(database="employeedb",user="test",password="password",host="127.0.0.1",port="5432")

print("Connected to employeedb")
cursor = conn.cursor()

cursor.execute("insert into employee (name,sal) values('Muzmmil',20000)")
conn.commit()
print("Employee Added")

cursor.close()
conn.close()