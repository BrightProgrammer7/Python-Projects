import turtle
t = turtle.Turtle()
t.color("red")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number * number

for n in range(360):
    angle = square(2)
    t.right(angle + .5)
    t.forward(5)
def bead_color(num):
    if num % 3 == 0:
        return "red"
    else:
        if num % 3 == 1:
            return "green"
        else:
            return "blue"

import random

def card():
   my_cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king"]
   my_card = random.choice(my_cards)
   return my_card
card()
die_roll = random.randint(1, 6)

