import socket
import threading
import cv2
import numpy as np

def videoStreaming(self,conn):
    capture = cv2.VideoCapture(0)
    while True:
        try :
            ret, frame = capture.read()
            img_encode = cv2.imencode('.jpg', frame)[1]
            data_encode = np.array(img_encode)
            str_encode = data_encode.tostring()
            if str_encode != "":
                self.sendVideo(self,conn,str_encode)
            else:
                capture.release()
                cv2.destroyAllWindows()
                exit(0)
        except KeyboardInterrupt:
            conn.close()

def sendVideo(self, conn, data):
    try:
        conn.send(data)
        conn.send(b"END!")
    except socket.error:
        exit(0)