from turtle import Turtle

PLAYER1_X_POS = 350
PLAYER2_X_POS = -350
Y_POS = 0
MOVE_DISTANCE = 20
STRETCH_LEN = 1
STRETCH_WID = 5


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)
        self.color("white")
        self.speed("fast")

    def move_paddle_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def player_1_paddle(self):
        self.goto(x=PLAYER1_X_POS, y=Y_POS)

    def player_2_paddle(self):
        self.goto(x=PLAYER2_X_POS, y=Y_POS)
