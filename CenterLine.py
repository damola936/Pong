from turtle import Turtle


class CenterLine(Turtle):
    """Initializes the center line"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.draw_square()
        self.penup()
        self.goto(10, -390)
        self.draw_game_line()
        self.speed("fastest")

    def draw_square(self):
        """Draws the center line square"""
        for _ in range(4):
            self.forward(20)
            self.left(90)

    def game_line(self):
        """The game line"""
        self.width(5)
        self.forward(10)
        self.penup()
        self.forward(10)
        self.pendown()
        self.forward(10)

    def draw_game_line(self):
        """Draws the game line"""
        self.left(90)
        self.hideturtle()
        for _ in range(15):
            self.game_line()
        self.penup()
        self.goto(10, 50)
        self.pendown()
        for _ in range(11):
            self.game_line()
