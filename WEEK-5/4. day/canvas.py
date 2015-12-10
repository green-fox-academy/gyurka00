from tkinter import *

master = Tk()

w = Canvas(master, width=400,height=400)
w.pack()

w.create_rectangle(0,0,160,160,fill='#ff0000',)
w.create_rectangle(0,160,160,320,fill='#f0f000',)
w.create_rectangle(160,160,320,320,fill='#00f0f0',)
w.create_rectangle(160,0,320,160,fill='#e07a9f',)
i = 1
x = 0
y = 0
while i < 17:
    j=i/2
    if i%2 ==0:
        x = 20
    else:
        x=0
    while j < 8:
        w.create_rectangle(x,y,x+20,y+20,fill='#00ff00',)
        x += 40
        j += 1
    y += 20
    x += 20
    i += 1

mainloop()
