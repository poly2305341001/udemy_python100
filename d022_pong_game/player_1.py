from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(350, 0)
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(1, 5)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


