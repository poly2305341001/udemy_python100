import time
from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 # 상수는 위에다 적어놔 -> 개발시 뭘 변경해야 설정을 바꿀 수 있는지 한눈에 파악
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def create_snake(self):
        self.snake
        for pos in STARTING_POS:
            self.add_square(pos)

    def add_square(self, pos):
        square = Turtle("square")
        square.penup()
        square.color("white")
        square.goto(pos)
        self.snake.append(square)

    def extend_snake(self):
        self.add_square(self.tail.pos())

    def move_snake(self):
        for idx in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[idx - 1].xcor()
            new_y = self.snake[idx - 1].ycor()
            self.snake[idx].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            # game_is_over = True
            pass
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            # game_is_over = True
            pass
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            # game_is_over = True
            pass
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            # game_is_over = True
            pass
        else:
            self.head.setheading(RIGHT)

    def replay(self):
        for square in self.snake:
            square.hideturtle()
        self.snake.clear()
        self.create_snake()
        time.sleep(1)
        self.head = self.snake[0]
        self.tail = self.snake[-1]

