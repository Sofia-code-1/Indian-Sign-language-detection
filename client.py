import cv2
import numpy as np
import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))  # Replace with the server's IP address

cap = cv2.VideoCapture(0)  # 0 for the default camera

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))  # Resize the frame to a standard size
    encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
    client.send(encoded_frame)

    