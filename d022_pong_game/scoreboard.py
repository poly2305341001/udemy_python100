from turtle import Turtle

SCORE_FONT = ("Fixedsys", 25, "normal")
RESULT_FONT = ("Fixedsys", 50, "normal")
WIN = "YOU WIN"
LOSE = "YOU LOSE"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setpos(0, 260)
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(f"{self.l_score}\t{self.r_score}",
                   align="center", font=SCORE_FONT)

    def get_score(self, who):
        if who == "r":
            self.r_score += 1
        if who == "l":
            self.l_score += 1

    def show_winner(self, who):
        self.setpos(0,-25)
        if who == "r":
            self.write(f"{LOSE}   {WIN}",
                       align="center", font=RESULT_FONT)
        if who == "l":
            self.write(f"{WIN}    {LOSE}",
                       align="center", font=RESULT_FONT)
