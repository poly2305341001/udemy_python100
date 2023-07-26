from turtle import Turtle, Screen
LINE_LENGTH = 290
POSITION = (-LINE_LENGTH, -LINE_LENGTH)
scr = Screen()


class Frame(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(POSITION)
        self.color("white")
        for _ in range(4):
            self.forward(LINE_LENGTH*2)
            self.left(90)
        scr.update()
