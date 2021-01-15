from tkinter import *
global pickup, drop
def funfinal():
	three.destroy()
	global final
	final = Tk()
	final.title('OIBER')
	Label(final, text='THANK YOU FOR CHOOSING OIBER').grid(row=0) 

def fun5():
	Label(three, text='Your Trip has been ended').grid(row=6)
	pay = Button(three, text='Please pay the Driver', width=25, command=funfinal)
	pay.grid(row=7)

def fun4():
	Label(three, text='Your Trip has Started the Trip').grid(row=4)

def fun3():
	Label(three, text='Your Driver has arrived').grid(row=2)

def fun2():

	two.destroy()
	#This function should also run the driver script in a new terminal
	#If the Driver accepts ride, the following code will be executed.
	global three
	three = Tk()
	three.title('OIBER')
	Label(three, text='Driver Details:\nName:\nContact Info:\n').grid(row=0) 
	#If the driver says they have arrived, execute this:
	fun3()
	#If the driver says they have started the trip, execute this:
	fun4()
	#If the driver says they have reached and are ending trip, execute this:
	fun5()
	
	#three.mainloop()


def fun():
	"""global startloc,endloc
				pickup=p.get()	#pickup stored here
				drop=d.get()	#drop stored here
				print(pickup)
				print(drop)"""
	one.destroy()
	#calculate Estimated fare
	"""global two
				two = Tk()
				two.title('OIBER')
				Label(two, text='Estimated Fare is:').grid(row=0) 
				conf = Button(two, text='Confirm', width=25, command=fun2)
				conf.grid(row=1)
				#two.mainloop()"""

one = Tk()
one.title('OIBER')
Label(one, text='Pickup:').grid(row=0) 
Label(one, text='Drop:').grid(row=1) 
p = Entry(one) 
d = Entry(one)
p.grid(row=0, column=1) 
d.grid(row=1, column=1)

book = Button(one, text='Book My Oiber', width=25, command=fun)
book.grid(row=2)
one.mainloop()

print("after looping")
print("this is great")
