 #import library
import random
import turtle as t #given nick name
t.Screen().bgcolor("light green")


#create the caterpiller turtle
caterpillar = t.Turtle()
caterpillar.shape("square")
caterpillar.color("pink")
caterpillar.speed(0)
caterpillar.penup()
#caterpillar.ht()

#creating the leaf
leaf = t.Turtle()
leaf_shape = ((0,0), (14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color("dark green")
leaf.speed(0)
leaf.penup()
#leaf.ht()

#create the  Press space text turtle
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press the space key to start', align='center', font=('arial',16,'bold'))
# create the score
score_turtle = t.Turtle()
score_turtle.ht()
score_turtle.speed(0)
# this defines the grid
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width () / 2
    top_wall = t.window_height () / 2
    bottom_wall = -t.window_height () /2
    (x,y) = caterpillar.pos()

    outside = \
        x < left_wall or \
        x > right_wall or \
        y < bottom_wall or \
        y> top_wall
    return outside

# game over
def game_over():
    caterpillar.color('light green')
    leaf.color('light green')
    t.penup()
    t.hideturtle()
    t.write("Game over!!!" , align='center', font=('Arial',30,'bold'))

#display the score
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) -50
    y= (t.window_height() / 2) -50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align="right", \
        font=('Arial', 40,'bold'))
#place a leaf in random postition on grid
def place_leaf():
    leaf.ht
    leaf.setx(random.randint(-190,190))
    leaf.sety(random.randint(-185,185))
    leaf.st()
# get the game started
def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

#caterpillar is moving...    
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)< 20:
            place_leaf()
            caterpillar_length +=1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed +=1

            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break
#arrow keys
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading() ==0 or caterpillar.heading()== 180:
        caterpillar.setheading(270)
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading()==270:
        caterpillar.setheading(0)
def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading()==270:
        caterpillar.setheading(180)

#listen for key press
t.onkey(start_game,"space")
t.onkey(move_up, "Up")
t.onkey(move_down,'Down')
t.onkey(move_right, 'Right')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()