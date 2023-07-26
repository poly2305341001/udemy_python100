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

# for n in range(3):
#     square = Turtle("square")
#     square.penup()
#     square.color("white")
#     square.goto(-20*n, 0)


# head = Turtle(shape="square")
# head.color("white")
# body = Turtle(shape="square")
# body.color("white")
# body.setpos(x=head.xcor()-20, y=head.ycor())
# tail = Turtle(shape="square")
# tail.color("white")
# tail.setpos(x=body.xcor()-20, y=head.ycor())

scr.tracer(0)
frame = Frame()

# starting_pos = [(0, 0), (-20, 0), (-40, 0)]
# snake = []
snake = Snake()
food = Food()
sb = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

# TODO: creates snake
# for pos in starting_pos:
#     square = Turtle("square")
#     square.penup()
#     square.color("white")
#     square.goto(pos)
#     snake.append(square)
# snake.create_snake()

scr.update()

game_is_over = False
while not game_is_over:
    scr.update()
    time.sleep(0.1)

    # if snake[0].xcor() > 590 or snake[0].xcor() <= -590:
    #     game_is_over = True
    # elif snake[0].ycor() > 590 or snake[0].ycor() <= -590:
    #     game_is_over = True
    #
    # else:
    #     for square in snake:
    #         square.forward(20)
    #
    #     for idx in range(2, 1, -1):
    #         print(snake[idx].pos())
    #         snake[idx].goto(snake[idx-1].pos())
    #         time.sleep(1)
    #     snake[0].forward(20)

    # TODO: moves snake
    # for idx in range(len(snake) - 1, 0, -1):
    #     new_x = snake[idx - 1].xcor()
    #     new_y = snake[idx - 1].ycor()
    #     snake[idx].goto(new_x, new_y)
    # snake[0].forward(20)
    # snake[0].left(90)
    snake.move_snake()

    # Detect collision with food.
    if snake.head.distance(food) < 10:
        food.refresh()
        sb.get_score()
        snake.extend_snake()

    # Detect collision with wall.
    if abs(snake.head.xcor()) > 295:
        game_is_over = True
        sb.game_over()
    elif abs(snake.head.ycor()) > 295:
        game_is_over = True
        sb.game_over()

    # Detect collision with tail.
    # for n in snake.snake:
    #     if n == snake.head:
    #         pass
    #     elif snake.head.distance(n) < 10:
    for n in snake.snake[1:]:
        if snake.head.distance(n) < 10:
            game_is_over = True
            sb.game_over()
    # if snake.twisted():
    #     game_is_over = True
    #     sb.game_over()

scr.exitonclick()
