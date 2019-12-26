import sys
import socket
import cv2
import numpy as np
import time

try:
    HOST = str(sys.argv[1])
except:
    print("Usage: python3 receiver.py <Your-IP-Address>")
    sys.exit()

PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

s.bind((HOST, PORT))
print("socket bind complete")

s.listen(10)
print("socket now listening")

conn,addr = s.accept()

while True:
    img_len = 1000000       # received by sender.py
    data = conn.recv(img_len)

    nparr = np.fromstring(data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    try:
        cv2.imshow('frame', frame)
    except Exception:
        pass
    time.sleep(2)           # time delay between packets

    print(len(data))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

