from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=2)
        self.speed("fastest")
        self.create_net()

    def create_net(self):
        y_pos = 300
        for _ in range(10):
            self.goto(x=0, y=y_pos)
            self.stamp()
            y_pos -= 70
