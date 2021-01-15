import socket
import time

bind_ip_client = '127.0.0.1'
bind_port_client = 6738

bind_ip_dri = '127.0.0.1'
bind_port_dri = 6739

sSockcli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSockcli.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSockcli.bind((bind_ip_client, bind_port_client))
sSockcli.listen(2)  # max backlog of connections

sSockdri = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSockcli.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSockdri.bind((bind_ip_dri, bind_port_dri))
sSockdri.listen(2)  # max backlog of connections


#print("Server")
client_sock, cliaddress = sSockcli.accept()
driver_sock, driaddress = sSockcli.accept()
#time.sleep(10)
driver_sock.send('Request!'.encode('UTF-8'))
print("request sent!")
driresp = driver.recv(1024)
driresp = str(driresp.decode('utf-8'))
if(driresp == 'y'):

    driver_sock.send('Name : Ravana, Contact No. : 9368483493'.encode('utf-8'))
    client_sock.send('Name : Venkataiappah Mururuswamy, Contact No. 7877586833'.encode('utf-8'))
    drivarrive = driver_sock.recv(1024)
    drivarrive = str(drivarrive.decode('utf-8'))
    if(drivarrive == 'y'):
        client_sock.send('Driver Arrived!'.encode('utf-8'))
        tripstart = driver_sock.recv(1024)
        tripstart = str(tripstart.decode('utf-8'))
        if(tripstart == 'y'):
            client_sock.send('Trip has started!'.encode('utf-8'))
            tripend = driver_sock.recv(1024)
            tripend = str(tripend.decode('utf-8'))
            if(tripend == 'y'):
                client_sock.send('Trip has ended!'.encode('utf-8'))


sSockcli.close()
sSockdri.close()