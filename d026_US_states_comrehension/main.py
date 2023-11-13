from turtle import Turtle, Screen
import pandas as pd

scr = Screen()
map_tt = Turtle()

img = "blank_states_img.gif"
scr.addshape(img)
map_tt.shape(img)

data = pd.read_csv("50_states.csv")

scr.title("U.S. States Game")


def check_answer(string):
    check = data[data.state == string].size
    if check >= 1:
        return True


def is_existed_already(list, string):
    for factor in list:
        if factor == string:
            return True


def write_on_map(string):
    state_tt = Turtle()
    state_tt.penup()
    state_tt.hideturtle()
    # state_x = int(data[data.state == string].x)
    # state_y = int(data[data.state == string].y-10)
    # state_tt.setpos(state_x, state_y)
    state_data = data[data.state == string]
    state_tt.setpos(int(state_data.x), int(state_data.y-7))
    state_tt.write(string, align="center")


correct_answers = []
all_states = data.state
answer_state = scr.textinput(title="Guess the State", prompt="What's another state's name?").title()

while len(correct_answers) < all_states.size:
    if answer_state == "Exit":
        break
    elif check_answer(answer_state):
        if is_existed_already(correct_answers, answer_state):
            answer_state = scr.textinput(title=f"{len(correct_answers)}/{all_states.size} States Correct",
                                         prompt="You've already checked the state.\nWhat's another state's name?").title()
        else:
            write_on_map(answer_state)
            correct_answers.append(answer_state)
            answer_state = scr.textinput(title=f"{len(correct_answers)}/{all_states.size} States Correct",
                                         prompt="What's another state's name?").title()
    else:
        answer_state = scr.textinput(title=f"{len(correct_answers)}/{all_states.size} States Correct",
                                     prompt="That's wrong.\nWhat's another state's name?").title()

all_states_list = all_states.to_list()
# for state in all_states_list:
#     if state in correct_answers:
#         all_states_list.remove(state)
# states_to_learn = pd.Series(all_states_list)
states_to_learn = pd.Series([state for state in all_states_list if state not in correct_answers])
states_to_learn.to_csv("states_to_learn.csv")
