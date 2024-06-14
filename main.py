from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from net import Net

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle()
player_1.player_1_paddle()
player_2 = Paddle()
player_2.player_2_paddle()
ball = Ball()
scoreboard = Scoreboard()
net = Net()


screen.listen()
screen.onkeypress(fun=player_1.move_paddle_up, key="Up")
screen.onkeypress(fun=player_1.move_paddle_down, key="Down")
screen.onkeypress(fun=player_2.move_paddle_up, key="w")
screen.onkeypress(fun=player_2.move_paddle_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect player_1 miss
    if ball.xcor() > 400:
        scoreboard.player2_point()
        ball.reset_ball()

    # Detect player_2 miss
    if ball.xcor() < -400:
        scoreboard.player1_point()
        ball.reset_ball()


screen.exitonclick()