import socket

HEADER = 1024
PORT = 5050
DISCONNECT_MESSEGE = '!DISCONNECT'
SERVER = "172.24.110.184"
ADDR = (SERVER, PORT)

def serverConnect():
    print(f"[CLIENT] Finding server on {ADDR}")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    selection = '1'
    #selection = input("1: Upload\n2: Download\n3: Disconnect messege")
    client.send(selection.encode())
    if selection == '1':
        file = open('exe')
        fileData = file.read()
        print(fileData)
        file.close()
        client.send(fileData.encode())
    elif selection == '2':
        pass
    elif selection == '3':
        client.send('!DISCONNECT'.encode())


serverConnect()

