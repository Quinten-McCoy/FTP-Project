import threading
import socket
from unittest import skip

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSEGE = '!DISCONNECT'

#Creating Server
print(f"[SERVER] Starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def main():
    #selection = input('1: Connect User\n2: Exit\n')
    selection = '1'
    while selection != '2':
        if selection == '1':
            connectUser()
            #selection = input('1: Connect User\n2: Exit\n')
    return 0


def authenticateUser():
    pass

def createUser():
    pass

def connectUser():
    print(f"[SERVER] Listening on {ADDR}")
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION {addr} connected")
        clientThread = threading.Thread(target=clientHandling, args = (conn, addr))
        clientThread.start()
        #Displaying number of connections to server
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1 }")

def clientHandling(conn, addr):
    #Deals with clients
    selection = conn.recv(HEADER).decode()
    print(selection)

    while selection != DISCONNECT_MESSEGE:
        connected = True
        while connected == True:
            if selection == '1':
                #Preparing to write data to file
                print("[SERVER] Recieving Data")

                #Opening file/recieving & writing data
                file = open("incommingFile", 'w')
                fileData = conn.recv(HEADER).decode()
                file.write(fileData)
                file.close()

                #Disconnecting client
                connected = False

            elif selection == '2':
                print("Sending File (Unfinished")

            connected = False
        print(f"[SERVER] Client {addr} has disconnected")

    conn.close()






    

    

main()

