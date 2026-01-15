import turtle as tim
import random

timmi = tim.Turtle()
tim.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# timmi.shape("turtle")
timmi.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmi.color(random_color())
        timmi.circle(100)
        timmi.setheading(timmi.heading() + size_of_gap)

draw_spirograph(5)

screen = tim.Screen()
screen.exitonclick()