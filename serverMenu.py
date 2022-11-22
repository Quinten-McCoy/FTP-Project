import socket
import os

HEADER = 4096
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSEGE = '!DISCONNECT'
SEPARATOR = "<SEPARATOR>"

#Creating users
admin_dict = {
    #'dn': 'cn=admin,dc=filetransfer,dc=com',
    'cn': 'admin',
    'description': 'LDAP Admin',
    'objectClass': 'simpleSecurityObject',
    'pass': 'Access123',
}

userone_dict = {
    #'dn': 'user one,dc=filetransfer,dc=com',
    'cn': 'userone',
    'description': 'Example user',
    'objectclass': 'inetOrgPerson',
    'pass': 'pass'
}

#Creating Server
print(f"[SERVER] Starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def connectUser():
    #Listening on...
    print(f"[SERVER] Listening on {ADDR}")
    server.listen(5)

    #connect users
    client_socket, addr = server.accept()
    print(f"[NEW CONNECTION {addr} connected")
    clientHandling(client_socket, addr)

def clientHandling(client_socket, addr):
    
    msg = client_socket.recv(HEADER).decode()
    cn, password  = msg.split('<SEPERATOR>')

    user_level, can_logon = verify_creds(cn, password) 
    
    if can_logon == True:
        selection = '1'

        while selection != DISCONNECT_MESSEGE:
            connected = True
            while connected == True:
                if selection == '1':
                    #FILE UPLOAD
                    #Preparing to write data to file
                    print("[SERVER] Recieving Data")

                    #Getting name and size of file
                    msg = client_socket.recv(HEADER).decode()
                    fileName, fileSize = msg.split('<SEPERATOR>')
                    print(fileName, fileSize)


                    with open('Recieved', 'wb') as f:
                        contents = client_socket.recv(HEADER).decode()   
                        f.write(contents)

                    selection = DISCONNECT_MESSEGE            

                elif selection == '2':
                    print("Sending File (Unfinished")

                    connected = False

        print(f"[SERVER] Client {addr} has disconnected")
        client_socket.close()


def verify_creds(cn, password):
    new_dict = {
        'cn': cn,
        'pass': password,
    }

    if new_dict['cn'] == userone_dict['cn'] and new_dict['pass'] == userone_dict['pass']:
        print('Logged in as Userone')
        level, logon = 'user', True
        return(level, logon)
    elif new_dict['cn'] == admin_dict['cn'] and new_dict['pass'] == admin_dict['pass']:
        print('Logged in as Admin')
        level, logon = 'admin', True
        return(level, logon)
    else:
        level, logon = 'none', False
        return(level, logon)

    

connectUser()

