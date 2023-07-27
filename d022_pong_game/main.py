from turtle import Screen
from player_1 import Paddle

scr = Screen()


scr.bgcolor("black")
scr.screensize(800, 600)
# scr.setup(800, 600)
scr.title("핑퐁핑퐁")
scr.tracer(0)

pd_1 = Paddle()

scr.listen()
scr.onkey(pd_1.up, "Up")
scr.onkey(pd_1.down, "Down")

game_is_on = True
while game_is_on:
    scr.update()

scr.exitonclick()
