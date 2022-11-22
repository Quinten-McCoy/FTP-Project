#Server side of file transfer using TLS
#Load Server Certificate to be shared via TLS handshake to client

import socket, ssl

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

#Set of constants establishing the connetion constants 
HEADER = 64
DISCONNECT_MESSEGE = '!DISCONNECT'

SERVER, PORT = socket.gethostbyname(socket.gethostname()), 555
ADDR = (SERVER, PORT)

#Creating context for secure connection
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain('serverCertificate/server.crt', 'serverCertificate/serverPriv.key')

#Creating socket object & setting host options
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def main():
    #Binding server and port together
    server.bind((ADDR))
    print(f'Accepting on {SERVER}')

    while True:
        #socket listening for up to 5 connections
        server.listen(5)
	    #accept connection
        csock, fromaddr = server.accept()
        
        #Wrap in context
        sClientConn = context.wrap_socket(csock, server_side= True)


	    #Prints IP address of Client
        print(f'Connection established from {str(fromaddr)}')
        level, logon = get_and_verify_creds(sClientConn)
        if logon == True:
            deal_with_client(sClientConn, level)
        else:
            print('Invalid Login')
            sClientConn.quit()


def get_and_verify_creds(sClientconn):
    
    msg = sClientconn.recv(HEADER).decode()
    cn, password  = msg.split('<SEPERATOR>')

    ldap_user_name = cn.strip()
    ldap_user_pwd = password.strip()
    
    new_dict = {
        'cn': ldap_user_name,
        'pass': ldap_user_pwd,
        
    }

    if new_dict['cn'] == userone_dict['cn'] and new_dict['pass'] == userone_dict['pass']:
        print('Logged in as Userone')
        level, logon = '1' , True
        return(level, logon)
    elif new_dict['cn'] == admin_dict['cn'] and new_dict['pass'] == admin_dict['pass']:
        print('Logged in as Admin')
        level, logon = '2', True
        return(level, logon)
    else:
        level, logon = '0', False
        return(level, logon)

   
def deal_with_client(sClientconn, f):
    #Recieve File
    while True:
 		#read from stream and store
        data = sClientconn.recv(HEADER).decode()
        if not data:
            print('End Of File received')
            break
        else:
			#write data from stream.recv(..) to file
            with open('Recieved', 'w') as f:
                f.write(data)
            sClientconn.close()


main()
    