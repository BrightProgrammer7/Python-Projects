import turtle
mary = turtle.Turtle()

color = "purple"
sides = [1, 2, 3, 4, 5]
angle = 72
distance = 100
mary.color(color)

for side in sides:
    mary.forward(distance)
    mary.right(angle)