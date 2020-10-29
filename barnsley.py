from p5 import *
import random


x = 0
y = 0


def setup():
    size(600, 600)
    background("black")
    no_stroke()


def draw():
    for i in range(50):
        draw_point()
        next_point()


def draw_point():
    stroke("green")
    stroke_weight(2)
    source_x = (-2.182, 2.6558)
    target_x = (0, 600)
    px = remap(x, source_x, target_x)
    source_y = (0, 9.9983)
    target_y = (600, 0)
    py = remap(y, source_y, target_y)

    point(px, py)


def next_point():
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


run()

