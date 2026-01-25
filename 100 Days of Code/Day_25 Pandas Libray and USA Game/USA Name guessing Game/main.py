import turtle

import pandas

#import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game")
image =  "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)
#we can get the coordinate data from the map using this. but we have already this data in to a list in
#another csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50Guess The State", prompt="What another States name?").title()
    if answer_state == "Exit":
        unused_states = []
        for state in all_states:
            if state not in guessed_state:
                unused_states.append(state)
        new_data = pandas.DataFrame(unused_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state, font=("Arial", 7, "bold"))


