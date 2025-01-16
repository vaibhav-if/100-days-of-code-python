from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

# ten colors list
color = ["red", "blue", "green", "yellow", "purple", "orange", "black", "brown", "pink", "gray"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3, 11):
    timmy.color(color[sides - 3])
    draw_shape(sides)

screen = Screen()
screen.exitonclick()