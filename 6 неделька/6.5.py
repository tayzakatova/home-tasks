#!/usr/bin/env python
# coding: utf-8

from random import randint
from random import uniform
from tkinter import *

colors = ['aqua', 'black', 'blueviolet', 'chocolate', 'red', 'blue', 'pink', 'yellow', 'orange']

WIDTH = 900
HEIGHT = 600

class Ball:
    def __init__(self, color='green', x=None, y=None):
        self.R = randint(10, 50) 
        if x is None:
            self.x = randint(self.R, WIDTH - self.R)
        else:
            self.x = x
        if y is None:
            self.y = randint(self.R, HEIGHT - self.R)
        else:
            self.y = y
        self.dx = uniform(-10, 10)
        self.dy = uniform(-10, 10)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill=color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

def click_handler(event):
    balls.append(Ball(color=colors[randint(0, len(colors) - 1)], x=event.x, y=event.y))

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)

root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for _ in range(5)]
tick()
root.mainloop()
