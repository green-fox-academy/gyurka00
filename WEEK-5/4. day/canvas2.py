from tkinter import *

master = Tk()

w = Canvas(master, width=605,height=605)
w.pack()

for i in range(1,601,10):
    a = i
    b = 600-i
    w.create_line(a,0,0,b,fill='#e07a9f',)


mainloop()
