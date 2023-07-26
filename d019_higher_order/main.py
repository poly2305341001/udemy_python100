from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")        # 시작할 때부터 인수 넣어서 객체 생성 가능!
scr = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_counter_clockwise():
#     tim.left(10)
#     tim.forward(10)
#
# def move_clockwise():
#     tim.right(10)
#     tim.forward(10)
#
# def clear_the_screen():
#     tim.home()
#     tim.clear()
#
# scr.listen()
# scr.onkey(key="w", fun=move_forwards) #함수를 매개변수로 쓸 때는 () 붙이면 안 됨!
# scr.onkey(key="s", fun=move_backwards)
# scr.onkey(key="a", fun=move_counter_clockwise)
# scr.onkey(key="d", fun=move_clockwise)
# scr.onkey(key="space", fun=clear_the_screen)
scr.setup(width=500, height=400)        # 코드 가독성을 위해 키워드 형식으로 인수 지정해주는 게 좋음
colors = ["red", "orange", "gold", "green", "blue", "purple"]

# tim = Turtle(shape="turtle")
# tim.color(colors[0])
# tim.penup()
# tim.goto(x=-230, y=-100)

is_race_on = False

turtles = []
for i in range(len(colors)):
    # turtles += str(i)     # 각 터틀에 이름 붙여주려고 이렇게 했는데 print(turtles) 하면 걍 Turtle 객체라고만 쭉 나옴 ㅠㅠㅠ
    # turtles[i] = Turtle(shape="turtle")
    # turtles[i].penup()
    # turtles[i].color(colors[i])
    # turtles[i].goto(x=-230, y=-100 + i*int(200/5))
    new_turtle = Turtle(shape="turtle")     # 모든 터틀이 같은 이름으로 선언될 수 있다니..... ㄷㄷ
    new_turtle.penup()      # 걍 객체가 생성될 때마다 다른 애고 그거 하나하나를 인스턴스라 한대 약간 테이블/릴레이션 개념에 얹어서 이해해봐도 될 듯?
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=-100 + i*int(200/5))      # 터틀이 너비 40짜리라 그럼
    turtles.append(new_turtle)
# print(turtles)

user_bet = scr.textinput(title="Make your bet", prompt=f"Which turtle will win the race? \n{colors}\nEnter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:

    for t in turtles:
        if t.xcor() >= 230:
            is_race_on = False
            winner = t
            if winner.pencolor() == user_bet:
                print(f"You've won! The {winner.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost. The {winner.pencolor()} turtle is the winner.")
        # rand_speed = random.random()*10
        # t.speed(rand_speed)
        rand_distance = random.random()*10
        t.forward(rand_distance)


scr.exitonclick()
