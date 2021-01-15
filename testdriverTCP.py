import socket 
  
 
# local host IP '127.0.0.1' 
host = '127.0.0.1'

# Define the port on which you want to connect 
port = 12364

driSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# connect to server on local computer 
driSock.connect((host,port)) 

# message you send to server 
req = driSock.recv(4096)
req = str(req.decode('utf-8'))
if(req == 'Request!'):
    print("Would you like to take this trip?")
    tripans = str(input())
    if(tripans == 'y'):
        driSock.send("y".encode('utf-8'))
        arriv = driSock.recv(4096)
        arriv = str(arriv.decode('utf-8'))
        print(arriv)
        print("Have you arrived?")
        arriv = str(input())
        if(arriv == 'y'):
            driSock.send("y".encode('utf-8'))
            tripst = driSock.recv(4096)
            print("Have you started trip?")
            tripst = str(input())
            if(tripst == 'y'):
                driSock.send("y".encode('utf-8'))
                tripend = driSock.recv(4096)
                print("Have you ended trip?")
                tripend = str(input())
                if(tripend == 'y'):
                    driSock.send("y".encode('utf-8'))


# close the connection 
driSock.close() 
