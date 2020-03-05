import sys
import socket
import selectors
import traceback
import libclient
import time
from performance import Performance


sel = selectors.DefaultSelector() #created a selector object asynchronous signaling

my_comp_perf = Performance()



''' start_connection (host, port, request) used to start a connection with server.'''

if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port> ")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
data = my_comp_perf.performance_info()
addr = (host, port)
print("starting connection to", addr)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # A TCP socket(socket.SOCK_STREAM) in IPV4(AF_INET)
sock.setblocking(False) # set the socket in non blocking mode
sock.connect_ex(addr) #for connecting with the server without raising exception
events = selectors.EVENT_WRITE # mask is set for both read and write -changed only to write
message = libclient.Message(sel, sock, addr, data) #class instance creation
sel.register(sock, events, data=message) #select register for asynchronous signaling

try:
    while True:
        events = sel.select(timeout=1)
        time.sleep(1.0)
        message.request = my_comp_perf.performance_info()
        for key, mask in events:
            message = key.data
            try:
                message.process_events(mask)
            except Exception:
                print(
                    "main: error: exception for",
                    f"{message.addr}:\n{traceback.format_exc()}",
                )
                message.close()
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
