import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from frame import Frame

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("내가 만든 뱀 게임쓰 와우")


scr.tracer(0)
frame = Frame()

snake = Snake()
food = Food()
sb = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

scr.update()

game_is_over = False
while not game_is_over:
    scr.update()
    time.sleep(0.1)

    snake.move_snake()

    # Detect collision with food.
    if snake.head.distance(food) < 10:
        food.refresh()
        sb.get_score()
        snake.extend_snake()

    # Detect collision with wall.
    if abs(snake.head.xcor()) > 295:
        # game_is_over = True
        # sb.game_over()
        sb.replay()
        snake.replay()
    elif abs(snake.head.ycor()) > 295:
        # game_is_over = True
        # sb.game_over()
        sb.replay()
        snake.replay()
    for n in snake.snake[1:]:
        if snake.head.distance(n) < 10:
            # game_is_over = True
            # sb.game_over()
            sb.replay()
            snake.replay()


scr.exitonclick()
