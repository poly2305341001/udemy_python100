# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("orange")
#
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# screen = Screen()
# screen.exitonclick()

'''
# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()

# from turtle import *
# from random import *
# forward(100)
# choice([1, 2, 3])
# # 코드가 길어지면 해당 메소드가 어느 모듈에서 튀어나온 건지 알 수가 없어서 이 방식은 비추

# import turtle as t
# tim = t.Turtle()

# import heroes
# print(heroes.gen())
#
# import villians
'''

import turtle as t
import random as r

tim = t.Turtle()
screen = t.Screen()

tim.shape("turtle")

# for _ in range(30):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         tim.color(c)
#         tim.forward(steps)
#         tim.right(30)

# while True:
#     tim.forward(200)
#     tim.left(170)
#     if abs(tim.pos()) < 1:
#         break


# def random_hex_color():
#     color_code = "#"
#     for _ in range(6):
#         hex_num = r.randint(0, 15)
#         color_code += format(hex_num, 'x')
#     return color_code


# def draw_polygon(angles):
#     for _ in range(angles):
#         tim.forward(100)
#         tim.right(360/angles)
#
# for angles in range(3, 11):
#     tim.color(random_hex_color())
#     draw_polygon(angles)


# def random_shut_down():
#     point = 500
#     lotto = r.randint(1, 500)
#     if point == lotto:
#         return True


def random_rgb_color():
    t.colormode(255)
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


def draw_spirograph(angle):
    for i in range(int(360/angle)):
        tim.color(random_rgb_color())
        tim.circle(100)
        tim.left(angle)


# tim.pensize(10)
# tim.speed(0)
# # while not random_shut_down():
# for _ in range(300):
#     tim.color(random_rgb_color())
#     tim.forward(40)
#     tim.setheading(90*r.randint(0, 3))
tim.speed("fastest")
total = 0
draw_spirograph(3)

screen.exitonclick()
