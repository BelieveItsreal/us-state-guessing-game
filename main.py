import turtle
import pandas

states = pandas.read_csv("E:\\python\\udemy_python\\us_state_guess\\50_states.csv")
states['state'] = states['state'].str.lower()

screen = turtle.Screen()


image = "E:\\python\\udemy_python\\us_state_guess\\blank_states_img.gif"
screen.addshape(image)
map_turtle = turtle.Turtle()  # Create a new turtle for the map
map_turtle.shape(image)
screen.title("US. State guess")

state_guessed = 0

while True:
    guess_state = screen.textinput(title=f"{state_guessed}/50 state guessed", prompt="What's another state name?")
    if guess_state is None:
        break
    guess_state = guess_state.lower()
    if guess_state in states.state.to_list():
        state_data = states[states.state == guess_state]
        writer_turtle = turtle.Turtle()  # Create a new turtle for writing
        writer_turtle.hideturtle()  # Hide the turtle
        writer_turtle.penup()
        writer_turtle.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        writer_turtle.write(guess_state)
        state_guessed += 1
