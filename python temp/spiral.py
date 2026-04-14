import turtle as t
from itertools import cycle

colors = cycle(['red','orange', 'yellow', 'green', 'blue', 'purple', 'pink'])
bglist = cycle(['black'])

def draw_shape(size,angle,shift,shape):
    t.bgcolor(next(bglist))
    t.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        
        for i in range(4):
            t.forward(size *2)
            t.left(90)
        next_shape = 'star'
    elif shape == 'star':
        next_shape = 'circle'
        def draw_star(points, size):
            angle = 180 - (180 / points)
            for i in range(points):
                t.forward(size)
                t.right(angle)
        draw_star
    t.right(angle)
    t.forward(shift)
    draw_shape(size + 1 , angle + 1, shift + 1,next_shape )
t.bgcolor('black')
t.speed(0)
t.pensize(2)
draw_shape(1,2,3,'star')