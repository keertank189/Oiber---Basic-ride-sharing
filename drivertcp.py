import time
import socket
dSockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
dSockTCP.connect(('127.0.0.1', 6739))

# send some data (in this case a HTTP GET request)

# receive the response data (4096 is recommended buffer size)
req = dSockTCP.recv(4096)
req = str(req.decode('utf-8'))
if(req == 'Request!'):
	print("Would you like to take this trip?")
	#this trip is x minutes away, then navigate
	ans = str(input())
	if(ans == 'y'):
		dSockTCP.send('y'.encode('utf-8'))
		cdetails = dSockTCP.recv(4096)
		cdetails = str(cdetails.decode('utf-8'))
		print(cdetails)
		print("Waiting 10 seconds")
		time.sleep(10)
		print("Have you arrived?")
		arriv = str(input())
		if(arriv == 'y'):
			dSockTCP.send('y'.encode('utf-8'))
		print("Can the trip be started?")
		start = str(input())
		if(start == 'y'):
			dSockTCP.send('y'.encode('utf-8'))
		#navigate from origin to dest, open google maps
		print("Have you reached?")
		end = str(input())
		if(end == 'y'):
			dSockTCP.send('y'.encode('utf-8'))
dSockTCP.close()