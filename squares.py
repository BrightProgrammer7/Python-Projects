import turtle
amy = turtle.Turtle()
side = int
face = int

import turtle
jack = turtle.Turtle()
jack.color("yellow")
jack.speed(0)

def draw_square(length):
    for side in range(4):
        jack.forward(length)
        jack.right(90)

def draw_thingy(n):
    for side in range(20):
        jack.forward(n)
        jack.right(n)

jack.penup()
jack.back(150)
jack.pendown()

draw_thingy(100)
draw_square(100)
draw_square(50)
draw_square(25)

for square in range(80):
       draw_square(5)
       jack.forward(5)
       jack.left(5)        


amy.width(5)
amy.penup()
amy.back(140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    for side in [1, 2, 3, 4]:
        amy.forward(50)
        amy.right(90)
    amy.penup()
    amy.forward(100)
    amy.pendown()

amy = turtle.Turtle()
amy.color("red")
amy.forward(100)
amy.right(90)
amy.color("orange")
amy.forward(100)
amy.right(90)
amy.color("yellow")
amy.forward(100)
amy.right(90)
amy.color("green")
amy.forward(100)    