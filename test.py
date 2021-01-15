from tkinter import *
global startloc,destloc,one
def fun():
	global startloc, destloc
	startloc = p.get()
	destloc = d.get()
	one.destroy()
	


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
print(startloc)
print(destloc)