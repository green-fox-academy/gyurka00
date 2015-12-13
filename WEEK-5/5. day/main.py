from tkinter import *
from ball import Ball
master = Tk()

canvas = Canvas(master, width = 400, height = 400)
canvas.pack()
canvas.create_rectangle(0,0,400,400,fill='#ffffff',)
ball = Ball((40, 50), (2, 2), 10)

while True:
    i = 0
    ball.velocity = (2, 2)
    while i < 100:
        ball.move()
        bbox = ball.get_bbox()
        canvas.create_rectangle(0 , 0, 400, 400, fill='#ffffff',)
        canvas.create_oval(bbox, fill='#000000')
        canvas.after(1000 // 60)
        canvas.update()
        i += 1
    ball.velocity = (-2, -2)
    j=0
    while j < 100:
        ball.move()
        bbox = ball.get_bbox()
        canvas.create_rectangle(0,0,400,400,fill='#ffffff',)
        canvas.create_oval(bbox, fill='#000000')
        canvas.after(1000 // 60)
        canvas.update()



mainloop()
