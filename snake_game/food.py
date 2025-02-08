from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # to halve its size
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-275, 275), random.randint(-275, 275))

    def refresh(self):
        self.goto(random.randint(-275, 275), random.randint(-275, 275))