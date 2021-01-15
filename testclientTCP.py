import socket 
  
 
# local host IP '127.0.0.1' 
host = '127.0.0.1'

# Define the port on which you want to connect 
port = 12363

cliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# connect to server on local computer 
cliSock.connect((host,port)) 
drivdet = cliSock.recv(4096)
drivdet = str(drivdet.decode('utf-8'))
if(drivdet == 'Driver rejected trip'):
	cliSock.close()
else:
	print(drivdet)
	info = cliSock.recv(4096)
	info = str(info.decode('utf-8'))
	print(info)
	info = cliSock.recv(4096)
	info = str(info.decode('utf-8'))
	print(info)
	info = cliSock.recv(4096)
	info = str(info.decode('utf-8'))
	print(info)
	cliSock.close()