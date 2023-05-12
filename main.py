import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").capitalize()
# print(answer_state)

import pandas
data = pandas.read_csv("50_states.csv")
print(data[data.state == answer_state])




