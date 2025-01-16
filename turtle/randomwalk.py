import turtle as t
import random

t.colormode(255) # set color mode to 255 (RGB)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy = t.Turtle()

timmy.shape("turtle")

directions = [0, 90, 180, 270]

timmy.pensize(15)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()