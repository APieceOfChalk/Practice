from tkinter import *
from math import sin, cos

root = Tk()

size = 600
c = Canvas(root, width=size, height=size, bg='white')
c.pack()

d = 400
c.create_oval(100, 100, 100 + d, 100 + d)

r = 20
circle = c.create_oval(300 - r, 100 - r, 300 + r, 100 + r, fill='#8779ff')

e = 0


def circle_move():
    global c
    global e

    c.move(circle, cos(e), sin(e))
    e += 0.005

    root.after(10, circle_move)


circle_move()
root.mainloop()
