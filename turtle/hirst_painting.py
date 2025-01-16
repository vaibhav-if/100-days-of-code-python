# import colorgram

# computation code takes time, we extracted the colors and saved it in below list
# colors = colorgram.extract('turtle/hirst_spot_painting.webp', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

import turtle as t
import random

rgb_colors = [(253, 250, 247), (253, 247, 249), (250, 228, 16), (236, 251, 244), (212, 13, 9), (199, 12, 36), (230, 228, 6), (196, 70, 20), (32, 90, 188), (235, 148, 38), (43, 212, 70), (33, 30, 152), (16, 22, 54), (67, 9, 48), (244, 39, 150), (14, 206, 223), (238, 244, 249), (66, 202, 229), (62, 21, 10), (225, 19, 111), (15, 155, 21), (228, 166, 9), (248, 11, 9), (245, 58, 16), (98, 75, 9), (223, 140, 203), (68, 240, 160), (10, 97, 62), (6, 39, 33), (68, 219, 157)] # colors extracted from the image

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

dot_count = 100

for i in range(1, dot_count + 1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

    if i % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()