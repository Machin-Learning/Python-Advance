import socket


s = socket.socket()

s.connect(("localhost",6767))

fileName = input("Enter a File Name")

s.send(fileName.encode())

contant = s.recv(1024)

print(contant.decode())
s.close()