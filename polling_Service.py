import socket
import socketserver
from os import system

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
address = (IP, PORT)

class handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if data == b'ping':
                self.request.sendall(b"pong")
            if data == b'shutdown':
                system("shutdown /s /t 100")

try:
    creepy_server = socketserver.TCPServer(address, handler)
    creepy_server.allow_reuse_address = True
    creepy_server.serve_forever()
except Exception as e:
    with open("debug.txt") as f:
        f.write(e)
