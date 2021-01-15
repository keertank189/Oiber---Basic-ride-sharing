import socket 
  
 
# local host IP '127.0.0.1' 
host = '127.0.0.1'

# Define the port on which you want to connect 
port = 12357

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# connect to server on local computer 
s.connect((host,port)) 

# message you send to server 
req = s.recv(4096)
req = str(req.decode('utf-8'))
if(req == 'Request!'):
    print("Would you like to take this trip?")
    tripans = str(input())
    if(tripans == 'y'):
        s.send("y".encode('utf-8'))
        arriv = s.recv(4096)
        print("Have you arrived?")
        arriv = str(input())
        if(arriv == 'y'):
            s.send("y".encode('utf-8'))
            tripst = s.recv(4096)
            print("Have you started trip?")
            tripst = str(input())
            if(tripst == 'y'):
                s.send("y".encode('utf-8'))
                tripend = s.recv(4096)
                print("Have you ended trip?")
                tripend = str(input())
                if(tripend == 'y'):
                    s.send("y".encode('utf-8'))


# close the connection 
s.close() 
