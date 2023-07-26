from turtle import Turtle
POSITION = (0, 250)
ALIGN = "center"
FONT = ("Fixedsys", 23, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.color("white")
        self.show_score()

    def get_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("- GAME OVER -", align=ALIGN, font=FONT)