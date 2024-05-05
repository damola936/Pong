from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player:
    """Player Class."""

    def __init__(self):
        self.pong_parts = []
        self.increment = 0

    def get_pad(self, increment, x_position, y_position, heading):
        """Initializes the pad."""
        for _ in range(3):
            pong_part = Turtle(shape="square")
            pong_part.width(60)
            pong_part.color("white")
            pong_part.penup()
            pong_part.setheading(heading)
            pong_part.goto(x=x_position, y=y_position + self.increment)
            self.increment += increment
            self.pong_parts.append(pong_part)

    def move(self):
        """Moves the player's pad."""
        for part in range(len(self.pong_parts) - 1, 0, -1):
            new_x = self.pong_parts[part - 1].xcor()
            new_y = self.pong_parts[part - 1].ycor()
            self.pong_parts[part].goto(new_x, new_y)
        self.pong_parts[0].forward(MOVE_DISTANCE)

    def is_at_wall(self):
        """Checks if the pad is at the wall, if True it turns it the other way."""
        if abs(self.pong_parts[0].ycor()) >= 300:
            if self.pong_parts[0].heading() == 90:
                for parts in self.pong_parts:
                    parts.setheading(270)
                    return True
            elif self.pong_parts[0].heading() == 270:
                for parts in self.pong_parts:
                    parts.setheading(90)
                    return True

    def move_up(self):
        """Moves the snake up"""
        self.pong_parts[0].setheading(UP)

    def move_down(self):
        """Moves the snake down"""
        self.pong_parts[0].setheading(DOWN)
