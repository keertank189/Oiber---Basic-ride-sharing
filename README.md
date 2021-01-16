# Oiber - Ride Sharing 
## Execution Sequence :
1. run server.py on host 1, with the UDP_IP,host, port and UDP_PORT_NO fields configured appropriately. {127.0.0.1 is local host}
2. run client.py on host 2, with the UDP_IP, host, port and UDP_PORT_NO fields configured appropriately. {127.0.0.1 is local host}
3. On host 2, specify Pick Up and Drop Locations. While specifying the pick up and drop locations, leave a space after every comma Ex. 'PES University, Bangalore', not 'PES University,Bangalore'. This is done as the HTTP requests take this field as a parameter.
4. Fare details, and nearest cab details are shared. After requesting a cab from the client, run driver.py on host 3
5. The driver side, now shows the request for the cab. If driver accepts, the client is informed. Responses of driver host will be shown in client host, to keep the client informed. 

## NOTE : 

1. This code was developed exclusively on Mac OS X. The code contains Mac OS X commands to open chrome, so if the code is being executed on a Linux/Windows machine, uncomment the section meant for Linux/Windows to open chrome in client.py, and driver.py, and comment the section meant for Mac OS X
2. Once the driver arrives, the dialog boxes cannot be closed by client. Due to alternating response mechanism between the driver and the client, once a dialog box opens in client, click 'Okay', after which the driver can proceed with his responses. 


### Prerequisites :
1. Internet Connection
2. Valid API key (supplied with the code)
3. Python 3.x+

### Modules needed :
1. sockets
2. requests
3. gmplot
4. webbrowser
5. json
6. os
7. time
8. random
9. Tkinter
10. Threading
