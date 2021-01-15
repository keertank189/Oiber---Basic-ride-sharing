import socket
cSockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
cSockTCP.connect(('127.0.0.1', 6738))

# send some data (in this case a HTTP GET request)
drivdet = cSockTCP.recv(4096)
drivdet = str(drivdet.decode('utf-8'))
print("Driver Details :")
print(drivdet)
# receive the response data (4096 is recommended buffer size)
drivarr = cSockTCP.recv(4096)
drivarr = str(drivarr.decode('utf-8'))
print(drivarr)
tripstart = cSockTCP.recv(4096)
tripstart = str(tripstart.decode('utf-8'))
print(tripstart)

tripend = cSockTCP.recv(4096)
tripend = str(tripend.decode('utf-8'))
print(tripend)

cSockTCP.close()