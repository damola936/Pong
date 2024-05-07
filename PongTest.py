from turtle import Screen
from CenterLine import CenterLine
from Player import Player
from Ball import Ball
import time
from Scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True
center_line = CenterLine()
screen.listen()

player_1 = Player()
player_1.get_pad(increment=20, x_position=-380, y_position=-260, heading=90)

player_2 = Player()
player_2.get_pad(increment=-20, x_position=370, y_position=260, heading=270)

ball = Ball()

player_1_score = ScoreBoard(-30, 290)
player_2_score = ScoreBoard(50, 290)

screen.onkey(fun=player_1.move_up, key="w")
screen.onkey(fun=player_1.move_down, key="s")

screen.onkey(fun=player_2.move_up, key="Up")
screen.onkey(fun=player_2.move_down, key="Down")

player1_hit = False
player2_hit = False

while game_is_on:
    screen.update()
    time.sleep(0.1)

    player_1.move()
    player_2.move()
    ball.start()
    player_1.is_at_wall()
    player_2.is_at_wall()

    for pong_part in player_1.pong_parts:
        if pong_part.distance(ball) < 15:
            ball.setheading(ball.heading() + 90)
            player1_hit = True
        if ball.xcor() >= 400 and player1_hit:
            player_1_score.increase_score()
            player1_hit = False
        if player1_hit:
            if ball.xcor() <= -400:
                player1_hit = False

    for pong_part in player_2.pong_parts:
        if pong_part.distance(ball) < 15:
            ball.setheading(ball.heading() + 90)
            player2_hit = True
        if ball.xcor() <= -400 and player2_hit:
            player_2_score.increase_score()
            player2_hit = False
        if player2_hit:
            if ball.xcor() >= 400:
                player2_hit = False

screen.exitonclick()
