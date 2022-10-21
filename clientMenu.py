import socket

HEADER = 1024
PORT = 5050
DISCONNECT_MESSEGE = '!DISCONNECT'
SERVER = "172.24.110.243"
ADDR = (SERVER, PORT)

def serverConnect():
    print(f"[CLIENT] Finding server on {ADDR}")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

serverConnect()

