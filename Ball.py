from turtle import Turtle
import random

ANGLES = []


class Ball(Turtle):
    """Initializes the Ball object"""
    def __init__(self):
        super().__init__()
        for i in range(0, 270):
            # removing buggy angles
            if 90 <= i <= 115 or 70 <= i <= 90 or 245 <= i <= 270:
                pass
            else:
                ANGLES.append(i)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("coral")
        self.speed("fastest")
        self.angle = random.choice(ANGLES)
        self.setheading(self.angle)

    def start(self):
        """Moves the ball at a different angle every iteration and game start"""
        if abs(self.xcor()) >= 400:
            self.goto(0, 0)
            self.setheading(random.choice(ANGLES))
            print(self.heading())
            self.start()
        else:
            self.forward(20)

        if abs(self.ycor()) >= 400:
            self.setheading(90 + self.heading())
            self.start()
