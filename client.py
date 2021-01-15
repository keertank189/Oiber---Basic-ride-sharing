import socket
import requests
from gmplot import gmplot
import webbrowser
import json
import os
import time
import random
api_key = "AIzaSyA59IygFBd6PVd_IGDS6VXH8w7rTfkRyr4"
UDP_IP = "49.206.11.64"
UDP_PORT_NO = 6792
cloc_URL = "https://www.googleapis.com/geolocation/v1/geolocate?considerIp=true&key=" + api_key
r = requests.post(url = cloc_URL)
r = r.json()
print(r)
usr_lat = r['location']['lat']
usr_lng = r['location']['lng']
user_coordinates = str(usr_lat) +","+ str(usr_lng)
clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto(user_coordinates.encode('utf-8'),(UDP_IP,UDP_PORT_NO))


gmap = gmplot.GoogleMapPlotter(usr_lat, usr_lng,13,api_key )
gmap.marker(usr_lat, usr_lng, 'red')



from tkinter import *
global startloc, destloc,drop,one,two,three
def funfinal():
	three.destroy()
	global final
	final = Tk()
	final.title('OIBER')
	Label(final, text='THANK YOU FOR CHOOSING OIBER').grid(row=0) 

def fun3():
	three.destroy()
	

def fun2():
	global ans 
	ans = 'y'
	two.destroy()
	#This function should also run the driver script in a new terminal
	#If the Driver accepts ride, the following code will be executed.
	


def fun():
	global startloc, destloc
	startloc = str(p.get())
	destloc = str(d.get())
	one.destroy()
	
	


one = Tk()
one.title('OIBER')
Label(one, text='Pickup:').grid(row=0) 
Label(one, text='Drop:').grid(row=1) 
p = Entry(one) 
d = Entry(one)
p.grid(row=0, column=1) 
d.grid(row=1, column=1)

book = Button(one, text='Book My Oiber', width=25, command=fun).grid(row=2)
one.mainloop()



#os.system("killall -9 'Google Chrome'")




locdetails = startloc + "$$$$" + destloc
print(locdetails)
clientSock.sendto(locdetails.encode('utf-8'),(UDP_IP,UDP_PORT_NO))

msg,serverip = clientSock.recvfrom(4096)
msg = json.loads(msg)
for i in msg : 
	gmap.marker(i[0], i[1], 'blue')


msg,serverip = clientSock.recvfrom(4096)
msg = json.loads(msg)
#print(msg)
gmap.marker(msg[0][0], msg[0][1], 'black')
gmap.marker(msg[1][0], msg[1][1], 'green')

pathpntsjson,serverip = clientSock.recvfrom(32768)
pathpntsjson = json.loads(pathpntsjson.decode('utf-8'))
pathpntscoord= []
#print(pathpntsjson)
#print(type(pathpntsjson))
for i in pathpntsjson:
	pathpntscoord.append(tuple((float(i['start_location']['lat']),float(i['start_location']['lng']))))
	pathpntscoord.append(tuple((float(i['end_location']['lat']),float(i['end_location']['lng']))))
#print(pathpntscoord)
path_lats, path_lngs = zip(*pathpntscoord)

"""golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347),
    (37.771269, -122.511015)
    ])"""
"""pathurl = "https://roads.googleapis.com/v1/snapToRoads?path=" \
			+ str(msg[0][0]) + "," + str(msg[0][1]) + "|" + str(msg[1][0]) + "," + str(msg[1][1]) +"&interpolate=true&key=" + api_key
path = requests.post(url = pathurl)
path = path.json()
points = path['snappedPoints']"""
#print(points) 
gmap.plot(path_lats, path_lngs, 'cornflowerblue', edge_width=3)

gmap.draw("my_map.html")
path = 'my_map.html'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(path)

fare,serverip = clientSock.recvfrom(1024)
fare = json.loads(fare)

ans = 'n'
cabtime,serverip = clientSock.recvfrom(1024)
cabtime = str(cabtime.decode('utf-8'))
print()
two = Tk()
two.title('OIBER')
Label(two, text='Estimated Fare is:' + str(fare)).grid(row=0) 
Label(two, text = "Nearest cab is " + cabtime[:2] +"minutes away. ").grid(row=1)
conf = Button(two, text='Confirm?', width=25, command=fun2)
conf.grid(row=2)
two.mainloop()


clientSock.sendto(ans.encode('utf-8'),(UDP_IP,UDP_PORT_NO))

if(ans =='y'):
	ser,ip = clientSock.recvfrom(4096)
	ser = str(ser.decode('utf-8'))
	if(ser != 'server up'):
		print("PRoblem : Server Not Up!")
	dri,ip = clientSock.recvfrom(4096)
	dri = str(dri.decode('utf-8'))
	if(dri != 'driver up'):
		print("PRoblem : driver Not Up!")
	clientSock.close()
	host = '127.0.0.1'

	# Define the port on which you want to connect 
	port = 12366

	cliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	# connect to server on local computer 

	cliSock.connect((host,port)) 
	drivdet = cliSock.recv(4096)
	drivdet = str(drivdet.decode('utf-8'))
	if(drivdet == 'Driver rejected trip'):
		cliSock.close()
	else:
		global three
		three = Tk()
		three.title('OIBER')
		Label(three, text='Driver Details:' + str(drivdet)).grid(row=0) 
		#If the driver says they have arrived, execute this:
		#If the driver says they have started the trip, execute this:

		#If the driver says they have reached and are ending trip, execute this:
		new = Button(three, text='Okay', width=25, command=fun3).grid(row=2)
		three.mainloop()
		print(drivdet)
		arrinfo = cliSock.recv(4096)
		arrinfo = str(arrinfo.decode('utf-8'))
		three = Tk()
		three.title('OIBER')
		Label(three, text='Driver Details: ' + str(drivdet)).grid(row=0) 
		Label(three, text =str(arrinfo)).grid(row=2)
		Button(three, text='Okay', width=25, command=fun3).grid(row=3)
		three.mainloop()
		stinfo = cliSock.recv(4096)
		stinfo = str(stinfo.decode('utf-8'))
		three = Tk()
		three.title('OIBER')
		Label(three, text='Driver Details: ' + str(drivdet)).grid(row=0) 
		Label(three, text =str(stinfo)).grid(row=2)
		Button(three, text='Okay', width=25, command=fun3).grid(row=3)
		three.mainloop()
		endinfo = cliSock.recv(4096)
		endinfo = str(endinfo.decode('utf-8'))
		three = Tk()
		three.title('OIBER')
		Label(three, text =str(endinfo)).grid(row=0)
		Button(three, text='Okay', width=25, command=fun3).grid(row=2)
		three.mainloop()
		three = Tk()
		three.title('OIBER')
		pay = Button(three, text='Please pay the Driver' + str(fare) + " rupees", width=35, command=funfinal)
		pay.grid(row=0)
		three.mainloop()
		cliSock.close()

