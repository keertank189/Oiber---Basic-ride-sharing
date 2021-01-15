import socket 
  
# import thread module 
from _thread import *
import threading 

resp = [0,0,0,0,0]
flag = -1
cli_done = 0 
# thread fuction 
def threadeddri(sSockdri): 
    global resp
    global flag 
    global cli_done
    while(1):
        if(resp[0] == 1):
        # data received from client 
            sSockdri.send('Request!'.encode('utf-8'))
        tripans = sSockdri.recv(4096)
        tripans = str(tripans.decode('utf-8'))
        if(tripans != 'y'):
            resp[1] = -1
            flag =0
            break
        resp[1] = 1
        sSockdri.send('Name : Ravana, Contact No. : 9368483493'.encode('utf-8'))
        arriv = sSockdri.recv(4096)
        arriv = str(arriv.decode('utf-8'))
        if(arriv != 'y'):
            resp[2] = -1
            flag =0
            break
        resp[2] = 1
        sSockdri.send("Trip Start?".encode('utf-8'))
        tripstart = sSockdri.recv(4096)
        tripstart = str(tripstart.decode('utf-8'))
        if(tripstart != 'y'):
            resp[3] = -1
            flag = 0
            break
        resp[3] = 1
        sSockdri.send("Trip End?".encode('utf-8'))
        reach = sSockdri.recv(4096)
        reach = str(reach.decode('utf-8'))
        if(reach != 'y'):
            resp[4] = -1
            flag =0
            break
        resp[4] = 1
        print(resp)
        while(cli_done == 0 ):
            continue
        break

  
    # connection closed 
    flag = 0
    sSockdri.close()

def threadedcli(sSockcli): 
    global resp
    global flag 
    global cli_done
    while(1):
        if(resp[1] == -1):
            sSockcli.send("Driver rejected trip".encode('utf-8'))
            break
        while(resp[1] == 0):
            continue
        if(resp[1] == 1):
            sSockcli.send("Name : Venkataiappah Mururuswamy, Contact No. 7877586833".encode('utf-8'))
            while(resp[2] == 0):
                continue
            if(resp[2] == 1):
                sSockcli.send("Driver Has Arrived!".encode('utf-8'))
                while(resp[3] == 0):
                    continue
                if(resp[3] == 1):
                    sSockcli.send("Driver Has started trip!".encode('utf-8'))
                    while(resp[4] == 0):
                        continue
                    if(resp[4] == 1):
                        sSockcli.send("Driver Has ended trip!".encode('utf-8'))
                        break
    print(resp)
    cli_done = 1
    sSockcli.close()

  
 
host = "127.0.0.1" 

# reverse a port on your computer 
# in our case it is 12345 but it 
# can be anything 
port = 12363
servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servSock.bind((host, port)) 
print("socket binded to post", port) 

# put the socket into listening mode 
servSock.listen(5) 
print("socket is listening") 

# a forever loop until client wants to exit  

    # establish connection with client 


sSockdri, addr = servSock.accept() 
# lock acquired by client 
#print_lock.acquire() 
print('Connected to :', addr[0], ':', addr[1]) 
resp[0] = 1
    # Start a new thread and return its identifier 
start_new_thread(threadeddri, (sSockdri,)) 
sSockcli, addr = servSock.accept() 
    # lock acquired by client 
    #print_lock.acquire() 
print('Connected to :', addr[0], ':', addr[1]) 

    # Start a new thread and return its identifier 
start_new_thread(threadedcli, (sSockcli,))
while(flag != 0):
    continue


servSock.close()
