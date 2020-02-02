import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8080
server.bind((host,port))
server.listen(1)
print("server is listening for connection")
client, client_address = server.accept()
print(f"Got the connection from:{client_address}")
client.send("start sending the data".encode())
while True:
    try:
        msg = client.recv(1024)
        print(msg.decode())
    except:
        print("error occurred")
        break

server.close()