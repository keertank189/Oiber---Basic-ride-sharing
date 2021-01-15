import socket
import random
import json
import requests
import threading
from _thread import *
#server
"""
to do
authenticate user
take user loc, user destination, user pick up
plot route
return cost to client
driver side on separate port
user details 
"""
api_key = "AIzaSyA59IygFBd6PVd_IGDS6VXH8w7rTfkRyr4"
UDP_IP = "49.206.11.64"
UDP_PORT_NO = 6792
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSock.bind((UDP_IP,UDP_PORT_NO))
recvd_usr_coord = 0
c_address = str()
while recvd_usr_coord == 0: 
	usr_coords,addr = serverSock.recvfrom(1024)
	c_address = addr
	usr_coords = str(usr_coords.decode('utf-8'))
	usr_coords = usr_coords.split(",")
	#data = tuple(data)
	#print(data)
	recvd_usr_coord = 1


recvd_usr_locdetails = 0
while recvd_usr_locdetails == 0: 
	usr_locdetails,addr = serverSock.recvfrom(1024)
	usr_locdetails = str(usr_locdetails.decode('utf-8'))
	usr_locdetails = usr_locdetails.split("$$$$")
	#data = tuple(data)
	#print(data)
	recvd_usr_locdetails = 1
cpickstr = usr_locdetails[0].split(" ")
cpickstr = ("+").join(cpickstr)
#print(cpickstr)
cpick_URL = "https://maps.googleapis.com/maps/api/geocode/json?address=" +\
			cpickstr +"&key=" + api_key
cpick_details = requests.post(url = cpick_URL)
cpick_details = cpick_details.json()
cpick_lat = (cpick_details['results'][0])['geometry']['location']['lat']
cpick_lng = (cpick_details['results'][0])['geometry']['location']['lng']


cabs_loc = []
random.seed()
for i in range(10):
	ls = []
	n = random.random()/100
	s = random.random()/100
	x = random.randint(0,3)
	if(x == 0):
		ls.append(float(cpick_lat)+n)
		ls.append(float(cpick_lng)+s)
	if(x == 1):
		ls.append(float(cpick_lat)-n)
		ls.append(float(cpick_lng)-s)
	if(x == 2):
		ls.append(float(cpick_lat)+n)
		ls.append(float(cpick_lng)-s)
	if(x == 3):
		ls.append(float(cpick_lat)-n)
		ls.append(float(cpick_lng)+s)
	cabs_loc.append(ls)
rand_cab_no = random.randint(0,9)
rand_cab_loc = cabs_loc[rand_cab_no]
cabs_loc = json.dumps(cabs_loc)
serverSock.sendto(cabs_loc.encode('utf-8'),c_address)


cdropstr = usr_locdetails[1].split(" ")
cdropstr = ("+").join(cdropstr)
cdrop_URL = "https://maps.googleapis.com/maps/api/geocode/json?address=" +\
			cdropstr +"&key=" + api_key
cdrop_details = requests.post(url = cdrop_URL)
cdrop_details = cdrop_details.json()
cdrop_lat = (cdrop_details['results'][0])['geometry']['location']['lat']
cdrop_lng = (cdrop_details['results'][0])['geometry']['location']['lng']
cdroppick = []
cdroppick.append([cpick_lat,cpick_lng])
cdroppick.append([cdrop_lat,cdrop_lng])
cdroppick = json.dumps(cdroppick)
serverSock.sendto(cdroppick.encode('utf-8'),c_address)

dirurl = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(cpick_lat) + "," + \
		str(cpick_lng) + "&destination=" + str(cdrop_lat) + "," + str(cdrop_lng) + "&mode=driving&key=" + api_key

nearcabdirurl = "https://maps.googleapis.com/maps/api/directions/json?origin=" + str(cpick_lat) + "," + \
		str(cpick_lng) + "&destination=" + str(rand_cab_loc[0]) + "," + str(rand_cab_loc[1]) + "&mode=driving&key=" + api_key		
#print(dirurl)
dirres = requests.post(url = dirurl)
dirres = dirres.json()
waypoints = ((dirres['routes'][0])['legs'][0])['steps']
waypoints = json.dumps(waypoints)
serverSock.sendto(waypoints.encode('utf-8'),c_address)

calc_fare = ((dirres['routes'][0])['legs'][0])['duration']['value'] / 8
calc_fare = json.dumps(calc_fare)
serverSock.sendto(calc_fare.encode('utf-8'),c_address)

nearcabtime = requests.post(url = nearcabdirurl)
nearcabtime = nearcabtime.json()
#print(((nearcabtime['routes'][0])['legs'][0])['duration'])
nearcabtime = ((nearcabtime['routes'][0])['legs'][0])['duration']['text']
serverSock.sendto(nearcabtime.encode('utf-8'),c_address)


res,addr = serverSock.recvfrom(30)
res =str(res.decode('utf-8'))

if(res =='y'):
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
	        sSockdri.send(str(rand_cab_loc).encode('utf-8'))
	        sSockdri.send(str([cpick_lat,cpick_lng]).encode('utf-8'))
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
	        #sSockdri.send(str(calc_fare).encode('utf-8'))
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
	            #sSockcli.send((str(rand_cab_loc[0])+","+str(rand_cab_loc[1])).encode('utf-8'))
	            #sSockcli.send((str(cpick_lat)+","+str(cpick_lng)).encode('utf-8'))
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

	  
	 
	host = "49.206.11.64" 

	# reverse a port on your computer 
	# in our case it is 12345 but it 
	# can be anything 
	port = 12366
	servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	servSock.bind((host, port)) 
	print("socket binded to post", port) 

	# put the socket into listening mode 
	servSock.listen(5) 
	print("socket is listening") 
	serverSock.sendto('server up'.encode('utf-8'),c_address);
	

	# a forever loop until client wants to exit  

	    # establish connection with client 


	sSockdri, addr = servSock.accept() 
	# lock acquired by client 
	#print_lock.acquire() 
	print('Connected to :', addr[0], ':', addr[1]) 
	resp[0] = 1
	    # Start a new thread and return its identifier 
	start_new_thread(threadeddri, (sSockdri,)) 
	serverSock.sendto('driver up'.encode('utf-8'),c_address);
	serverSock.close()
	sSockcli, addr = servSock.accept() 
	    # lock acquired by client 
	    #print_lock.acquire() 
	print('Connected to :', addr[0], ':', addr[1]) 

	    # Start a new thread and return its identifier 
	start_new_thread(threadedcli, (sSockcli,))
	while(flag != 0):
	    continue


	servSock.close()