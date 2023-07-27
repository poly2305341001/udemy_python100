from turtle import Screen
from player import Paddle
from ball import Ball
import time
from frame import Frame
from scoreboard import Scoreboard


scr = Screen()


scr.bgcolor("black")
# scr.screensize(800, 600)
scr.setup(800, 600)
scr.title("핑퐁핑퐁")
scr.tracer(0)

frame = Frame()
sb = Scoreboard()

pd_r = Paddle((350, 0))
pd_l = Paddle((-350, 0))
ball = Ball()


scr.listen()
scr.onkey(pd_r.up, "Up")
scr.onkey(pd_r.down, "Down")
scr.onkey(pd_l.up, "w")
scr.onkey(pd_l.down, "s")
scr.update()
time.sleep(1)

game_is_on = True
while game_is_on:
    time.sleep(0.06)
    scr.update()
    # ball.direction()
    # while ball.xcor() < 320:
    #     ball.forward(20)
    # ball.seth(180-ball.direction())
    # while ball.xcor() > -320:
    #     ball.forward(20)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with pd_r
    if ball.xcor() > 320:
        if ball.distance(pd_r) < 60:
            ball.bounce_x()
            ball.speed_up()

        # pd_r miss the ball
        elif ball.xcor() > 420:
            sb.get_score("l")
            sb.show_score()
            ball.respawn()
            scr.update()
            time.sleep(1)
            ball.bounce_x()

    # Detect collision with pd_l
    if ball.xcor() < -320:
        if ball.distance(pd_l) < 60:
            ball.bounce_x()
            ball.speed_up()

        # pd_l miss the ball
        elif ball.xcor() < -420:
            sb.get_score("r")
            sb.show_score()
            ball.respawn()
            scr.update()
            time.sleep(2)


    if sb.l_score >= 5:
        game_is_on = False
        sb.show_winner("l")
    if sb.r_score >= 5:
        game_is_on = False
        sb.show_winner("r")


scr.exitonclick()
