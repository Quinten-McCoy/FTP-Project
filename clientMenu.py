import socket
import os

SEPARATOR = "<SEPARATOR>"
HEADER = 4096
PORT = 5050
DISCONNECT_MESSEGE = '!DISCONNECT'
SERVER = "172.24.109.142"
ADDR = (SERVER, PORT)

def get_creds():
    #cn = input('Enter CN')
    cn = 'userone'
    password = 'pass'
    #password = input('Enter Password')

    serverConnect(cn, password)


def serverConnect(cn, password):

    #Finding server and connecting
    print(f"[CLIENT] Finding server on {ADDR}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDR)
    print(f'[CLIENT] Found server on {ADDR}')

    msg = (f'{cn}<SEPERATOR>{password}')
    msg_byt = msg.encode()

    server.send(msg_byt)

    selection = ('1: Download File\n2: Upload File\n3:View Files\n4: Quit')
    while selection != '4':
        if selection == '1':
            down_file(server)
        elif selection == '2':
            send_file(server)
        elif selection == '3':
            view_files(server)
    


    
def down_file(client):
    pass


def send_file(client):
    #Collecting data to be sent (name and size)
    filename = "C:\\Users\\qmcc\\Documents\\Transfer\\text.txt"
    filesize = os.path.getsize(filename)

    msg = (f'{filename}<SEPERATOR>{filesize}')
    msg_byt = msg.encode()
    #Sending name and size
    client.send(msg_byt)

    with open(filename, 'rb') as f:
        content  = f.readlines()
    print(content)

    content_byt = content.encode()
    client.send(content_byt)

def view_files(client):
    pass

    
get_creds()

