import socket
import time
import pickle
import cv2
from HuffmanTree import *


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5555))
s.listen(5)




while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    url = "Frames/adorable-puppy.jpg"
    image = cv2.imread(url)
    msg = pickle.dumps(image)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)