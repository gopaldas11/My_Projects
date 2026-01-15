# from turtle import Turtle, Screen
# import random
# timmi = Turtle()
#
# timmi.shape("turtle")
# # timmi.forward(100)
# # timmi.right(90)
# # timmi.forward(100)
# # timmi.right(90)
# # timmi.forward(100)
# # timmi.right(90)
# # timmi.forward(100)
# # timmi.right(90)
# # for _ in range(5):
# #     timmi.forward(20)
# #     timmi.penup()
# #     timmi.forward(20)
# #     timmi.pendown()
# # colors = ["red", "green", "blue", "cyan", "magenta", "CornflowerBlue", "DarkOrchid",
# #           "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "Black"]
#
# # def dwar_shape(num_side):
# #     angle = 360 / num_side
# #     for _ in range(num_side):
# #         timmi.forward(100)
# #         timmi.right(angle)
# # for n_shape_side in range(3, 11):
# #     timmi.color(random.choice(colors))
# #     dwar_shape(n_shape_side)
# # def screen_set():
# #     screen_hight = 600
# #     screen_width = 600
# #     screen.setup(height=screen_hight,width=screen_width)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_rong = (r, g, b)
#     return random_rong
#
# timmi.speed("fastest")
# timmi.pensize(15)
# direction = 0, 90, 180, 270
# for _ in range(200):
#     timmi.pencolor(random.choice(random_color()))
#     timmi.forward(30)
#     timmi.setheading(random.choice(direction))
# random_color()
# screen = Screen()
# screen.exitonclick()

from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmi = Turtle()
timmi.shape("turtle")
timmi.speed("fastest")
timmi.pensize(15)
screen = Screen()
screen.colormode(255)
directions = [0, 90, 180, 270]
for _ in range(200):
    timmi.pencolor(random_color())
    timmi.forward(20)
    timmi.setheading(random.choice(directions))

screen.exitonclick()
