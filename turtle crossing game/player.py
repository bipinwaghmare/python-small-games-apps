from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Step 1
# Create a turtle player that starts at the bottom of the screen and listen for
# the "Up" keypress to move the turtle north.


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.player_start_position()

    def player_start_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        if self.heading() != 270:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return  False

