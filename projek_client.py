import socket
import cv2
import numpy
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5555))

def recv_data():
    data = b''
    while True:
        try:
            recvRequest = sock.recv(90456)
            if len(recvRequest) == 0:
                exit(0)
            a = recvRequest.find(b'END!')
            if a != -1:
                data += recvRequest[:a]
                break
            data += recvRequest
        except Exception as e:
            print(e)
            break

    nparr = numpy.frombuffer(data, numpy.ubyte)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    try:
        cv2.imshow('Video Streaming', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit(0)
    except:
        sock.close()
        exit(0)

while True:
    recv_data()

# camera.release()
# cv2.destroyAllWindows()