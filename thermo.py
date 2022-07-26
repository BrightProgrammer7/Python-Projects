import turtle

def temperature_color(temp):
    # Change this code!
    if temp < 20:
        return "blue"
    elif temp < 100:
        return "purple"
    elif temp >= 100:
        return "red"         
    return "green"

def draw_temperature(temp):
    t = turtle.Turtle()
    t.penup()
    t.back(100)
    t.width(20)
    t.pendown()
    for n in range(temp):
        while temp == int(my_temp):     
            t.color("black") 
            t.forward(5) 
        t.color(temperature_color(n))
        t.forward(1)
    

def draw_therm_box():
    t = turtle.Turtle()
    t.speed(0)
    t.color("gray")
    t.penup()
    t.back(120)
    t.pendown()
    t.left(90)
    for side in [20, 240, 40, 240, 20]:
        t.forward(side)
        t.right(90)
    t.hideturtle()

print("Enter your temperature:")
my_temp = input()
draw_therm_box()
draw_temperature(200)
