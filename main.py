import turtle
import pandas
FONT = ("Arial", 14, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    guess_state = data[data.state == answer_state]
    guess_x = data[data.x == answer_state]
    guess_y = data[data.y == answer_state]

    # Creates CSV file with missing states
    if answer_state == "Exit":

        #new List Comprehension method
        missing_states = [state for state in all_states if state not in guessed_states]

        #original method
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        #below "iloc" stands for "integer locate", uses row number (index) and 1 for the X column and 2 for the Y column
        t.goto(data.iloc[state_data.index[0],1], data.iloc[state_data.index[0],2])
        t.write(answer_state)
        print(guessed_states)
    else:
        print("false")

screen.exitonclick()