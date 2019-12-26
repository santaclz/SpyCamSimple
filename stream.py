import sys
import socket
import time
import cv2

try:
    HOST = str(sys.argv[1])
except:
    print("Usage: python3 stream.py <IP-Address> <camera-id>")
    print("Example: python3 stream.py 192.168.1.8 1")
    sys.exit()

PORT = 5000
try:
    capture = cv2.VideoCapture(int(sys.argv[2]))
except:
    print("Enter camera id (usually 0, 1 or 2...)")
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    ret,frame = capture.read()
    frame = cv2.resize(frame, (500,500))

#    print(len(data))    # send data length

    data = cv2.imencode('.jpg', frame)[1].tostring()
    sock.sendall(data)
    time.sleep(2)

    print(len(data))
