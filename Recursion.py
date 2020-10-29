# Мамедова Лейла ПИ19-2
# Задание номер 12

from tkinter import *

root = Tk()
size = 600
c = Canvas(root, width=size, height=size, bg='black')
c.pack()


def draw(x, y, xx, yy):
    c.create_oval(x, y, xx, yy, outline='white')
    d = xx - x
    if d > 2:
        nd = d * 0.25
        p = d * 0.125
        draw(x + p, y + 3 * p, x + p + nd, y + 3 * p + nd)
        draw(x + p * 5, y + p * 3, x + p * 5 + nd, y + p * 3 + nd)


draw(50, 50, 550, 550)
root.mainloop()



import turtle
import random

pen = turtle.Turtle()
pen.screen.setup(600, 600)
pen.speed(20)
pen.color("black")
pen.penup()

x = 0
y = 0


def map5(x, start1, stop1, start2, stop2):
    return ((x - start1) / (stop1 - start1)) * (stop2 - start2) + start2

def draw():
    for i in range(100000):
        point()
        next()


def point():
    global x
    global y
    px = map5(x, -2.182, 2.6558, 0, 300)
    py = map5(y, 0, 9.9983, 300, 0)

    pen.goto(px, py)
    pen.pendown()
    pen.dot()
    pen.penup()


def next():
    global x, y
    r = random.uniform(0, 100)
    if r < 1:
        xn = 0
        yn = 0.16 * y
    elif r < 86:
        xn = 0.85 * x + 0.04 * y
        yn = -0.04 * x + 0.85 * y + 1.6
    elif r < 93:
        xn = 0.20 * x - 0.26 * y
        yn = 0.23 * x + 0.22 * y + 1.6
    else:
        xn = -0.15 * x + 0.28 * y
        yn = 0.26 * x + 0.24 * y + 0.44

    x = xn
    y = yn


draw()
