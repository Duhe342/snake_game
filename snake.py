from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]
        self.counter = 0

    def create_snakes(self):
        for snake in STARTING_POSITIONS:
            self.add_snake_part(snake)

    def add_snake_part(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def expand(self):
        self.add_snake_part(self.snakes[-1].position())

    def move_snakes(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):

        if self.head.heading() != DOWN and self.counter == 0:
            self.head.seth(UP)
            self.counter = 1

    def snake_down(self):
        if self.head.heading() != UP and self.counter == 0:
            self.head.seth(DOWN)
            self.counter = 1

    def snake_left(self):
        if self.head.heading() != RIGHT and self.counter == 0:
            self.head.seth(LEFT)
            self.counter = 1

    def snake_right(self):
        if self.head.heading() != LEFT and self.counter == 0:
            self.head.seth(RIGHT)
            self.counter = 1
