from tkinter import *

wn = Tk()
wn.title('tk')
wn.geometry('300x300')

def test():
    l1.configure(text = 'Today study: '+e1.get())

def test2():
    l2.configure(text='Today play: '+e2.get())

l1 = Label(wn, text = 'Today study: ')
l2 = Label(wn, text = 'Today play: ')
e1 = Entry(wn, textvariable = int)
e2 = Entry(wn)
b1 = Button(wn, text = 'study', command = test)
b2 = Button(wn, text = 'play', command = test2)

l1.pack()
l2.pack()
e1.pack()
e2.pack()
b1.pack()
b2.pack()


wn.mainloop()