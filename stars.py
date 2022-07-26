import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

terry = turtle.Turtle()
terry.width(5)
terry.speed(78)
terry.hideturtle()

for color in rainbow:
    terry.color(color)
    for star in range(5):
        terry.forward(50)
        terry.right(144)
    terry.right(60)    
    terry.penup()
    terry.forward(50)
    terry.pendown()
  
