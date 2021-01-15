name = str()
def printtext():
    global e
    global f
    global name
    fn = e.get() 
    ln = f.get()
    name = str(fn + " " + ln)

from tkinter import *
root = Tk()

root.title('Name')
Label(root, text='First Name')
e = Entry(root)
e.pack()
e.focus_set()
Label(root, text='Last Name')
f = Entry(root)
f.pack()
f.focus_set()


b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')
root.mainloop()
print(name)
