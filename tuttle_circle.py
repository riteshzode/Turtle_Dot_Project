import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
colormode(255)
timmy.speed("fastest")


# angle = [0, 90, 180, 270, 360]


#This function will generate random color tuple

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    result = (r, b, g)
    return result

# This function will create circle as per gap size we need in circle

def circle_space(gap_size):
    for i in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)  # we can use + or -
        timmy.circle(100)

        
circle_space(5)

screen = Screen()

screen.exitonclick()
