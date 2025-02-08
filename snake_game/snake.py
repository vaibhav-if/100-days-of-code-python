from turtle import Turtle
MOVE_DISTANCE = 20
POSITION = -20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            self.add_snake((POSITION * i, 0))

    def add_snake(self, position):
        t = Turtle()
        t.shape("square")
        t.penup()
        t.goto(position)
        t.color("white")
        self.snake.append(t)

    def extend(self):
        self.add_snake(self.snake[-1].position())

    def move(self):
        for t in range(len(self.snake) - 1, 0, -1):
            self.snake[t].goto(self.snake[t-1].xcor(), self.snake[t-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)