import cv2
import numpy as np
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))  # Bind to any available network interface
server.listen(5)
print("Server listening on port 12345")

while True:
    client_socket, _ = server.accept()
    data = b""
    
    while True:
        packet = client_socket.recv(1024)
        if not packet:
            break
        data += packet
        img_array = np.frombuffer(data, dtype=np.uint8)
        frame = cv2.imdecode(img_array, 1)
        cv2.imshow("Server Video", frame)
        if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
            break

cv2.destroyAllWindows()