import random
from turtle import Turtle, colormode, Screen

list_color = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53),
              (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53),
              (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159),
              (212, 183, 177),
              (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

timmy = Turtle()
colormode(255)
timmy.penup()
timmy.speed("fastest")

timmy.setheading(135)
timmy.forward(300)
timmy.setheading(0)

for i in range(1, 101):
    timmy.dot(20, random.choice(list_color))
    timmy.forward(50)

    if i % 10 == 0:
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
