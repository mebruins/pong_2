from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('P O N G')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'p')
screen.onkey(r_paddle.go_down, 'l')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 400: 
        ball.reset()
        scoreboard.l_point()
    
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()

    if scoreboard.l_score == 3:
        ball.goto(0,0)
        ball.write('GAME OVER\n LEFT WINS', align='center', font=('helvetica', 60, 'normal'))
        
    elif scoreboard.r_score == 3:
        ball.goto(0,0)
        ball.write('GAME OVER\n RIGHT WINS', align='center', font=('helvetica', 60, 'normal'))

screen.exitonclick()