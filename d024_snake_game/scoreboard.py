from turtle import Turtle
POSITION = (0, 250)
ALIGN = "center"
FONT = ("Fixedsys", 23, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.color("white")
        self.show_score()

    def get_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        if self.score > self.highscore:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
            self.highscore = self.score
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("- GAME OVER -", align=ALIGN, font=FONT)

    def replay(self):
        # if self.score > self.highscore:
        #     with open("data.txt", mode="w") as data:
        #         data.write(f"{self.score}")
        #     self.highscore = self.score
        self.score = 0
        self.show_score()
