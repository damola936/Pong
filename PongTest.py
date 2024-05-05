from turtle import Screen
from CenterLine import CenterLine
from Player import Player
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True
center_line = CenterLine()
screen.listen()


player_1 = Player()
player_1.get_pad(increment=20, x_position=-380, y_position=-260, heading=90)

player_2 = Player()
player_2.get_pad(increment=-20, x_position=370, y_position=260, heading=270)

screen.onkey(fun=player_1.move_up, key="w")
screen.onkey(fun=player_1.move_down, key="s")

screen.onkey(fun=player_2.move_up, key="Up")
screen.onkey(fun=player_2.move_down, key="Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    player_1.move()
    player_2.move()
    player_1.is_at_wall()
    player_2.is_at_wall()

screen.exitonclick()
