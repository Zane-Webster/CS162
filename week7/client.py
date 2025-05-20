import socket

# create client socket
client_socket = socket.socket()

# connect to localhost:9999
client_socket.connect(('localhost',9999))

# input name and send to server
name = input("Enter your name: ")
client_socket.send(bytes(name, "utf-8"))

# print message from server
print(client_socket.recv(1024).decode())

while True:
    pass