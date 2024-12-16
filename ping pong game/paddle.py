from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
# Shape of paddle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

# Move ball up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

# Move ball down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


