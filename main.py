import turtle
from turtle import Turtle, Screen
import pandas


# Initialize the screen
screen = Screen()
state_count = 0
screen.title(f"U.S. States Game")

# Set the path to your GIF file (relative path is generally better)
gif_path = "blank_states_img.gif"

# Add the shape
try:
    screen.addshape(gif_path)
except Exception as e:
    print(f"Error adding shape: {e}")

# Optionally, set the background image if needed
try:
    screen.bgpic(gif_path)
except Exception as e:
    print(f"Error setting background picture: {e}")


tim = Turtle()
tim.hideturtle()
correct_guesses = []
game_is_on = True
data = pandas.read_csv("50_states.csv")
state_data = data.state.to_list()
state = ""
Not_guessed = []

while game_is_on:
    screen.update()
    answer = screen.textinput(f"States Guessing game{len(correct_guesses)}/50",
                              "Guess a State").title()  #Convert into title case
    state = data[data["state"] == answer]
    if not state.empty:
        state_count += 1
        new_x = int(state.x)
        new_y = int(state.y)
        tim.penup()
        tim.goto(new_x, new_y)
        tim.write(f"{state.state.item()}")
        correct_guesses.append(answer)
        print(correct_guesses)
    elif state_count == 50:
        game_is_on = False
    elif answer == "Exit":
        for states in state_data:
            if states not in correct_guesses:
                Not_guessed.append(states)
            else:
                pass

        break

not_dict = {"States": Not_guessed}
New_data = pandas.DataFrame(not_dict)
New_data.to_csv("new_data.csv")





# Keep the window open until clicked
# screen.exitonclick()
