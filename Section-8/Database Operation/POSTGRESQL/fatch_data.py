import psycopg2

conn = psycopg2.connect(host="127.0.0.1",port="5432",database="employeedb",user="test",password="password")

print("Connected to employeedb")

cursor = conn.cursor()

cursor.execute("select * from employee")

rows = cursor.fetchall()
print("Total Numbers of records",cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()