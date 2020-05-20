import socket
import threading
import time
import streaming_server
from streaming_server import videoStreaming, sendVideo

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("",5555))
sock.listen(5)

def handleThread(conn):
    try:
        while True:
            self = streaming_server
            data = videoStreaming(self,conn)
    except (socket.error, KeyboardInterrupt) :
        conn.close()
        print("Client menutup koneksi")

try:
    while True :
        conn, client_addr = sock.accept()
        clientThread = threading.Thread(target=handleThread, args=(conn,))
        clientThread.start()
except socket.timeout:
    conn.close()
except KeyboardInterrupt:
    conn.close()
    del connections
    exit(0)
    
