import turtle
import pandas

d = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guest = []
all_states = d.state.to_list()

while len(correct_guest) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guest)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in all_states:
        correct_guest.append(answer_state)

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = d[d.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guest]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
