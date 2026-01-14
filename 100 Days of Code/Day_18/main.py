from turtle import Turtle, Screen
import random
timmi = Turtle()

timmi.shape("turtle")
timmi.color("black")
# timmi.forward(100)
# timmi.right(90)
# timmi.forward(100)
# timmi.right(90)
# timmi.forward(100)
# timmi.right(90)
# timmi.forward(100)
# timmi.right(90)
# for _ in range(5):
#     timmi.forward(20)
#     timmi.penup()
#     timmi.forward(20)
#     timmi.pendown()
colors = ["red", "green", "blue", "cyan", "magenta", "CornflowerBlue", "DarkOrchid",
          "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "Black"]

def dwar_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        timmi.forward(100)
        timmi.right(angle)

for n_shape_side in range(3, 11):
    timmi.color(random.choice(colors))
    dwar_shape(n_shape_side)























screen = Screen()
screen.exitonclick()