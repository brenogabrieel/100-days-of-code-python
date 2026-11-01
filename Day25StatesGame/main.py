import turtle
import csv

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data from CSV using csv module
with open("50_states.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

all_states = [row['state'] for row in data]
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        with open("states_to_learn.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["state"])
            for state in missing_states:
                writer.writerow([state])
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = next(item for item in data if item["state"] == answer_state)
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)
