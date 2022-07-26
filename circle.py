import turtle

c = turtle.Turtle()
c.color("magenta")
c.width(5)

c.penup()
c.back(70)
c.right(-90)
c.forward(50)
c.pendown()
c.hideturtle() 

for side in range(100):
    c.forward(5)
    c.right(360 / 100)

   