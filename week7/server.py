import socket

# set address and port constants
ADDRESS = 'localhost'
PORT = 9999

# create socket
s = socket.socket()

# bind socket to localhost:9999
s.bind((ADDRESS, PORT))
print(f"SERVER OPENED TO {ADDRESS}:{PORT}")

# wait for client to connect
s.listen(3)
print(f"AWAITING CONNECTIONS...\n")

# open server loop
while True:
    # accept client connection
    client_socket, client_address = s.accept()
    # get client name and print client info
    client_name = client_socket.recv(1024).decode()
    print(f"{client_name} CONNECTED WITH ADDRESS {client_address}")

    # send client message
    client_socket.send(bytes(f"CONNECTED TO {ADDRESS}:{PORT}","utf-8"))
    # close client socket
    client_socket.close()