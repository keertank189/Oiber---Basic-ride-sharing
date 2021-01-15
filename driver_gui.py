from tkinter import *

def fun9():
	seven.destroy()
	global eight
	eight = Tk()
	eight.title('OIBER_DRIVER')
	Label(eight, text='Has the Fare Been Collected?').grid(row=0) 
	fare_clt = Button(eight, text='Fare Collected', width=25, command=eight.destroy)
	fare_clt.grid(row=2)
	eight.mainloop()

def fun8():
	six.destroy()
	global seven
	seven = Tk()
	seven.title('OIBER_DRIVER')
	Label(seven, text='Has the Trip Ended?').grid(row=0) 
	end = Button(seven, text='Trip Ended', width=25, command=fun9)
	end.grid(row=2)
	seven.mainloop()

def fun7():
	five.destroy()
	global six
	six = Tk()
	six.title('OIBER_DRIVER')
	Label(six, text='Has the Trip Started?').grid(row=0) 
	start = Button(six, text='Trip Started', width=25, command=fun8)
	start.grid(row=2)
	six.mainloop()

def fun6():
	four.destroy()
	global five
	five = Tk()
	five.title('OIBER_DRIVER')
	Label(five, text='Customer Details:\nName:\nContact Info:\n').grid(row=0) 
	
	arr = Button(five, text='I Have Arrived', width=25, command=fun7)
	arr.grid(row=1)
	five.mainloop()

four = Tk()
four.title('OIBER_DRIVER')
Label(four, text='New Trip Available').grid(row=0) 
book = Button(four, text='Accept', width=25, command=fun6)
book.grid(row=2)
four.mainloop()