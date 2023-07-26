from color_list import color_list
import turtle
import random as rd


def dot_row(pen_size, distance, number_of_dots):
    for _ in range(number_of_dots):
        random_color = rd.choice(color_list)
        # tt.color(random_color)
        # tt.pendown()
        # tt.circle(distance)
        tt.dot(pen_size, random_color)
        tt.setheading(0)
        # tt.penup()
        tt.forward(distance)

#
# def dot_matrix(function, distance, number_of_rows):
#     for i in range(number_of_rows):
#         function
#         tt.setpos(-250, -250 + distance * i)

tt = turtle.Turtle()
scr = turtle.Screen()

turtle.colormode(255)
tt.speed(0)
tt.penup()
tt.hideturtle()

for i in range(10):
    tt.setpos(-225, -225 + i*50)
    dot_row(20, 50, 10)

scr.exitonclick()
