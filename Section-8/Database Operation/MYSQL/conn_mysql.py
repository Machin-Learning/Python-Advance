import mysql.connector

conn = mysql.connector.connect(host = 'localhost',database='mydb',user='root')

if conn.is_connected():
    print("Connected to mysql db")


conn.close()