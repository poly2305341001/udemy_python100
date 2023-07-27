import time
from turtle import Turtle
# import random as rd
# import math
#
# MAX_ANGLE = math.acos(4 / 5) * 180 / math.pi



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(0)
        # self.shapesize(1, 1)
        self.x_move = 10
        self.y_move = 10

    # def direction(self):
    #     pm = rd.choice(PLUS_MINUS)
    #     # rn = random.random()
    #     # self.setpos(400 * pm,  rn * 300 * pm)
    #     angle = rd.random()*MAX_ANGLE*pm
    #     self.seth(angle)
    #     return angle

    # def accident(self, paddle):
    #     if self.meet_paddle(paddle):
    #         return True
    #
    # def meet_paddle(self, paddle):
    #     if self.distance(paddle) < 10:
    #         return True
    #

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    # def ping(self):
    #     if self.xcor
    #     if self.ycor() > 290:
    #         new_x = self.xcor() + 5
    #         new_y = self.ycor() - 5
    #     elif self.ycor() < 290:
    #         new_x = self.xcor() + 5
    #         new_y = self.ycor() + 5

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def respawn(self):
        self.clear()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def speed_up(self):
        self.x_move *= 1.1
        self.y_move *= 1.1
