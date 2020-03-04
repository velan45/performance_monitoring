import socket
import psutil as perf
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8080
client.connect((host, port))
'''msg = client.recv(1024)
print(msg.decode())
var = 'a'
for i in range(10):
    print(f"in loop {i}")
    my_tuple = perf.cpu_stats()
    client.send(str(my_tuple).encode())
client.send(str(var).encode())
'''
client.close()
