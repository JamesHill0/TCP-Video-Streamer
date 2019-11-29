import socket
import pickle
import cv2

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5555))

while True:
    full_message = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_message += msg

        print(len(full_message))

        if len(full_message)-HEADERSIZE == msglen:
            print(full_message[HEADERSIZE:])
            image = pickle.loads(full_message[HEADERSIZE:])
            cv2.imshow("Yeet", image)
            cv2.waitKey()
            cv2.destroyAllWindows()
            new_msg = True
            full_message = b""