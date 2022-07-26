import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t = turtle.Turtle()
t.width(20)

for step in range(100):
    # Change this to use a random number.
    angle = random.randint(-90,90)
    # Change this to use a random color.
    color = random.choice(colors)

    t.color(color)
    t.right(angle)
    t.forward(10)


riley = turtle.Turtle()
riley.width(5)

mood = random.choice(["happy", "sad", "angry", "party"])

if mood == "happy":
    riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
elif mood == "angry":
    riley.color("red")
elif mood == "party":
    riley.color("magenta")
else:
    riley.color("gray")

for side in range(5):
    riley.forward(100)
    riley.right(144)   