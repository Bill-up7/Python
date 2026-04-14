import turtle as t
#rectangle
def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
#circle
def draw_circle(x,y,col,):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    r=70
    t.circle(r)
    t.end_fill()
    t.penup





#main code starts heren(end of function)
t.penup()
t.bgcolor("Dodger Blue")

#feet
t.goto(-90,-130)
rectangle(50,20,"Light pink")
t.goto(0,-130)
rectangle(50,20,"Light pink")
t.goto( 90,-130)
rectangle(50,20,"Light pink")
t.goto( 180,-130)
rectangle(50,20,"Light pink")
t.goto( 270,-130)
rectangle(50,20,"Light pink")
t.goto( 360,-130)
rectangle(50,20,"Light pink")
# legs
t.goto(-60,-60)
rectangle(20,70,"hot pink")
t.goto(30,-60)
rectangle(20,70,"hot pink")
t.goto(120,-60)
rectangle(20,70,"hot pink")
t.goto(210,-60)
rectangle(20,70,"hot pink")
t.goto(300,-60)
rectangle(20,70,"hot pink")
t.goto(390,-60)
rectangle(20,70,"hot pink")
#body
t.goto(-60,0)
rectangle(498,70,"hot pink")
# head
draw_circle(-60,0,"pink")

#eyes
t.goto(-80,100)
rectangle(10,10,"black")
t.goto(-60,100)
rectangle(10,10,"black")
t.goto(-80,70)
rectangle(60,10,"black")


t.ht()
t.mainloop()