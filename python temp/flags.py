#Drawing flags usiong Python Turtle - www.101computing.net/drawing-flags-using-python-turtle
import turtle as t 
import turtle
import time
myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.speed(10)
window = turtle.Screen()
window.bgcolor("#DDDDDD")
#Position the pen in the bottom left corner
#chad
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
#Draw the frame for the flag
myPen.color("gold")
myPen.pensize(2)
myPen.fillcolor("gold")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()    
#Draw the blue stripe
myPen.color("blue")
myPen.pensize(2)
myPen.fillcolor("blue")
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(120)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill() 
#Draw the red stripe
myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")
myPen.penup()
myPen.goto(60, -120)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(120)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill() 
myPen.hideturtle()
time.sleep(0.5)

#Luxembourg
myPen.showturtle()
myPen.shape("arrow")
#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
#Draw the frame for the flag
myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()    
#Draw the blue stripe
myPen.color("blue")
myPen.pensize(2)
myPen.fillcolor("blue")
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(120)
  myPen.left(90)
myPen.end_fill() 
#Draw the white stripe
myPen.color("white")
myPen.pensize(2)
myPen.fillcolor("white")
myPen.penup()
myPen.goto(-180, 40)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.right(90)
  myPen.forward(80)
  myPen.right(90)
myPen.end_fill() 
myPen.end_fill() 
myPen.hideturtle()
time.sleep(0.5)

#Iceland
myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.speed(10)
window = turtle.Screen()
window.bgcolor("#DDDDDD")
#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
#Draw the frame for the flag
myPen.color("#307DC1")
myPen.pensize(2)
myPen.fillcolor("#307DC1")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()   
#Draw the White horizontal stripe
myPen.color("white")
myPen.pensize(2)
myPen.fillcolor("white")
myPen.penup()
myPen.goto(-180, -20)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(40)
  myPen.left(90)
myPen.end_fill()  
#Draw the White vertical stripe
myPen.penup()
myPen.goto(-70, -120)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(40)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()


#Draw the red horizontal stripe
myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")
myPen.penup()
myPen.goto(-180, -10)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(20)
  myPen.left(90)
myPen.end_fill() 
#Draw the red vertical stripe
myPen.penup()
myPen.goto(-60,-120)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(20)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill() 
myPen.hideturtle()
time.sleep(0.5) 



#Luxembourg
myPen.showturtle()
myPen.shape("arrow")
#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
#Draw the frame for the flag
myPen.color("blue")
myPen.pensize(2)
myPen.fillcolor("blue")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()    
#Draw the blue stripe
myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(60)
  myPen.left(90)
myPen.end_fill() 
#Draw the white stripe
myPen.color("gold")
myPen.pensize(2)
myPen.fillcolor("gold")
myPen.penup()
myPen.goto(-180,0)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(120)
  myPen.left(90)
myPen.end_fill() 
myPen.end_fill() 
myPen.hideturtle()
time.sleep(0.5)


#Ghana
myPen.showturtle()
myPen.shape("arrow")
#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
#Draw the frame for the flag
myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()    
#Draw the blue stripe
myPen.color("green")
myPen.pensize(2)
myPen.fillcolor("green")
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(120)
  myPen.left(90)
myPen.end_fill() 
#Draw the white stripe
myPen.color("gold")
myPen.pensize(2)
myPen.fillcolor("gold")
myPen.penup()
myPen.goto(-180, 40)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.right(90)
  myPen.forward(80)
  myPen.right(90)
myPen.end_fill() 
myPen.end_fill() 
def draw_star():
    t.penup()
    t.goto(-30,10)
    t.pendown()
    angle = 180 - (180 / 5)
    t.color("black")
    t.begin_fill()
    for i in range(5):
        t.forward(70)
        t.right(angle)
    t.end_fill()
draw_star()
myPen.hideturtle()
time.sleep(0.5)
#cuba
#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()

#Draw the frame for the flag
myPen.color("blue")
myPen.pensize(2)
myPen.fillcolor("blue")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()  

#Draw the red horizontal stripe
myPen.color("blue")
myPen.pensize(2)
myPen.fillcolor("blue")

myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()

myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(120)
  myPen.left(90)
myPen.end_fill()


#white stripe low
myPen.color("white")
myPen.pensize(2)
myPen.fillcolor("white")
myPen.penup()
myPen.goto(-180, -50)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(30)
  myPen.left(90)
myPen.end_fill() 
#Draw the White horizontal stripe high
myPen.color("white")
myPen.pensize(2)
myPen.fillcolor("white")
myPen.penup()
myPen.goto(-180, 40)
myPen.pendown()
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(30)
  myPen.left(90)
myPen.end_fill() 
myPen.hideturtle()


#Draw the blue triangle
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()

myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")

myPen.begin_fill()
myPen.goto(0,0)
myPen.goto(-180,120)
myPen.goto(-180,-120)
myPen.end_fill()  

def draw_star1():
    t.penup()
    t.goto(-150,10)
    t.pendown()
    angle = 180 - (180 / 5)
    t.color("white")
    t.begin_fill()
    for i in range(5):
        t.forward(40)
        t.right(angle)
    t.end_fill()
draw_star1()

#turkey
#Draw the frame for the flag
myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()  

#draw circle
def draw_circle2():
    t.penup()
    t.goto(-110,5)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
draw_circle2()
myPen.hideturtle()
#draw circle
def draw_circle3():
    t.penup()
    t.goto(-95,5)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
draw_circle3()
myPen.hideturtle()
myPen.showturtle()
def draw_star2():
    t.penup()
    t.goto(-90,30)
    t.pendown()
    angle = 180 - (180 / 5)
    t.color("white")
    t.begin_fill()
    for i in range(5):
        t.forward(20)
        t.right(angle)
    t.end_fill()
draw_star2()
myPen.hideturtle() 


#jamaca



# tansinia
myPen.showturtle()
myPen.shape("arrow")
#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
#Draw the frame for the flag
myPen.color("green")
myPen.pensize(2)
myPen.fillcolor("green")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()    


#Draw the blue triangle
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()

myPen.color("yellow")
myPen.pensize(2)
myPen.fillcolor("yellow")

myPen.begin_fill()
myPen.goto(0,0)
myPen.goto(-180,120)
myPen.goto(-180,-120)
myPen.end_fill() 



#Draw the blue triangle
myPen.penup()
myPen.goto(180, 120)
myPen.pendown()

myPen.color("yellow")
myPen.pensize(2)
myPen.fillcolor("yellow")

myPen.begin_fill()
myPen.goto(0,0)
myPen.goto(180,-120)
myPen.goto(180,120)
myPen.end_fill()


#Draw the blue triangle
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()

myPen.color("black")
myPen.pensize(1)
myPen.fillcolor("black")

myPen.begin_fill()
myPen.goto(0,0)
myPen.goto(-180,120)
myPen.goto(-180,-120)
myPen.end_fill()






turtle.mainloop()
