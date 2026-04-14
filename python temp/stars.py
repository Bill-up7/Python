import turtle as t 
from random import randint, random
#function to draw
def draw_star(points, size,col,x,y):
    t.speed(50)
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()
def draw_circle(x,y,col):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    r=randSize
    t.circle(r)
    t.end_fill()

def draw_alternating_background(color):
    if ranx % 2 == 0:
            t.bgcolor("purple")
    else:
         if ranx % 2 == 1:
             t.Screen().bgcolor("pink")
while True:
    ranx= randint(-500,500)
    rany = randint(-300,300)
    randSize = randint(10,80)
    randPoints= randint(5,10)
    rancolor = (random(),random(), random())
    draw_star(randPoints, randSize,rancolor,ranx,rany)
    ranX= randint(-500,500)
    ranY = randint(-300,300)
    randSize = randint(10,80)
    randPoints= randint(5,10)
    rancolor = (random(),random(), random())
    draw_circle(ranX + 3,ranY - 40,rancolor)
    draw_alternating_background(rancolor,)