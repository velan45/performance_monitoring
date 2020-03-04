import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8080
server.bind((host,port))
server.listen(1)
print("server is listening for connection")
while True:
    try:
        client, client_address = server.accept()
        print(f"Got the connection from:{client_address}")
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
        break
'''client.send("start sending the data".encode())
while True:
    try:
        msg = client.recv(1024)
        if msg.decode() =='a':
            break
        print(msg.decode())
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
        break
'''
server.close()