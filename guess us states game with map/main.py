import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Guess Game")

# Save image file in image variable.
# turtle only allows .gif format file to display.
image = "blank_states_img.gif"

# This adds the image on shape.
screen.addshape(image)

# This displays the turtle shape as a image.
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

state_list = data["state"].to_list()
# print(state_list)


game_is_on = True

guessed_states = []

score = 0

while game_is_on and len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{score}/50 - States Correct",
                                    prompt="What's another state name ?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        game_is_on = False

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# This is an alternative like exitonclick() but it keep the screen-
# even after clicking on screen
# turtle.mainloop()

# This exits the screen as soon as we clink anywhere on screen.
screen.exitonclick()
