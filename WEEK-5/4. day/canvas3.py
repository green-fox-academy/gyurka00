from tkinter import *

master = Tk()

w = Canvas(master, width=605,height=605)
w.pack()

w.create_line(300, 0, 300, 600,fill='#e07a9f',)
w.create_line(40.2, 150, 559.8, 450,fill='#e07a9f',)
w.create_line(40.2, 450, 559.8, 150,fill='#e07a9f',)


n = 10
for i in range(30):
    # w.create_line(300,0 + i*n,300-i*((0.75*n**2)**0.5), 300-i*(n/2),fill='#e07fff')  original
    w.create_line(300,0 + i*n,300-i*((0.75*n**2)**0.5), 300+i*(n/2),fill='#e07fff')
    w.create_line(300,0 + i*n,300+i*((0.75*n**2)**0.5), 300+i*(n/2),fill='#e07fff')
    w.create_line(300,600 - i*n,300-i*((0.75*n**2)**0.5), 300-i*(n/2),fill='#e07fff')
    w.create_line(300,600 - i*n,300+i*((0.75*n**2)**0.5), 300-i*(n/2),fill='#e07fff')


mainloop()
