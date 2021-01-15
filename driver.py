import socket 
import requests
import webbrowser
from tkinter import *
def fun6():
    global tripans
    tripans = 'y'
    four.destroy()
def fun7():
    global arriv
    arriv = 'y'
    four.destroy()
def fun8():
    global tripst
    tripst = 'y'
    four.destroy()
def fun9():
    global tripend
    tripend = 'y'
    four.destroy()
 
# local host IP '127.0.0.1' 
host = '127.0.0.1'

# Define the port on which you want to connect 
port = 12366

driSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# connect to server on local computer 
driSock.connect((host,port)) 

# message you send to server 
req = driSock.recv(4096)
req = str(req.decode('utf-8'))
if(req == 'Request!'):
    global tripans
    tripans = 'n'
    four = Tk()
    four.title('OIBER_DRIVER')
    Label(four, text='New Trip Available').grid(row=0) 
    book = Button(four, text='Accept', width=25, command=fun6)
    book.grid(row=2)
    four.mainloop()
    if(tripans == 'y'):
        global arriv
        driSock.send("y".encode('utf-8'))
        cdetails = driSock.recv(4096)
        cdetails = str(cdetails.decode('utf-8'))
        cab_loc = driSock.recv(4096)
        cab_loc = str(cab_loc.decode('utf-8'))[1:-1]
        cab_loc = cab_loc.split(",")
        pick_loc = driSock.recv(4096)
        pick_loc = str(pick_loc.decode('utf-8'))[1:-1]
        pick_loc = pick_loc.split(",")
        print(cab_loc[0])
        print(cab_loc[1])
        print(pick_loc[0])
        print(pick_loc[1])
        path = 'https://www.google.com/maps/dir/?api=1&origin=' + cab_loc[0]+"," + cab_loc[1] + \
                "&destination=" + pick_loc[0] + "," + pick_loc[1]+"&travelmode=driving&dir_action=navigate"
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

        # Windows
        # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        # Linux
        # chrome_path = '/usr/bin/google-chrome %s'

        webbrowser.get(chrome_path).open(path)
        #print(cab_loc)
        #print(pick_loc)
        arriv = 'n'
        four = Tk()
        four.title('OIBER_DRIVER')
        Label(four, text=cdetails +'\n').grid(row=0) 
        Button(four, text='I Have Arrived', width=25, command=fun7).grid(row=1)
        four.mainloop()
        if(arriv == 'y'):
            global tripst
            driSock.send("y".encode('utf-8'))
            tripst = driSock.recv(4096)
            four = Tk()
            four.title('OIBER_DRIVER')
            Label(four, text='Has the Trip Started?').grid(row=0) 
            start = Button(four, text='Trip Started', width=25, command=fun8).grid(row=2)
            four.mainloop()
            if(tripst == 'y'):
                global tripend
                driSock.send("y".encode('utf-8'))
                tripend = driSock.recv(4096)
                four = Tk()
                four.title('OIBER_DRIVER')
                Label(four, text='Has the Trip Ended?').grid(row=0) 
                Button(four, text='Trip Ended', width=25, command=fun9).grid(row=2)
                four.mainloop()
                if(tripend == 'y'):
                    driSock.send("y".encode('utf-8'))
                    """money = driSock.recv(4096)
                                                                                money = str(money.decode('utf-8'))
                                                                                print("Fare Collected:")"""
                    #print(money)


# close the connection 
driSock.close() 
