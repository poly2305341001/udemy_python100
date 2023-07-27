from turtle import Turtle

class Frame(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")

        self.penup()
        self.setpos(-400, -300)
        self.pendown()

        self.forward(800)
        self.left(90)
        self.forward(600)
        self.left(90)
        self.forward(800)
        self.left(90)
        self.forward(600)

        self.penup()
        self.setpos(0, -300)
        self.setheading(90)
        for i in range(20):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(5)
