import socket

#client.py - UDP 

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto('msg',(UDP_IP,UDP_PORTNO))
msg,serverip = clientSock.recvfrom(4096)

#server.py - UDP

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DRAM)
serverSock.bind((UDP_IP,UDP_PORTNO))
serverSock.sendto('msg',c_address)
msg,caddr = serverSock.recvfrom(4096)

#client.py - TCP

clientSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSock.connect((TCP_IP,TCP_ADDR))
clientSock.send('msg')
msg = clientSock.recv(4096)

#server.py - TCP

serverSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSock.bind((TCP_IP,TCP_ADDR))
serverSock.listen(5)
sSockcli, ip = serverSock.accept()
sSockcli.send('msg')
msg = sSockcli.recv(4096)