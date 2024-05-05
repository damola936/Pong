from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.draw_square()
        self.penup()
        self.goto(10, -290)
        self.draw_game_line()
        self.speed("fastest")

    def draw_square(self):
        for _ in range(4):
            self.forward(20)
            self.left(90)

    def game_line(self):
        self.width(5)
        self.forward(10)
        self.penup()
        self.forward(10)
        self.pendown()
        self.forward(10)

    def draw_game_line(self):
        self.left(90)
        self.hideturtle()
        for _ in range(9):
            self.game_line()
        self.penup()
        self.goto(10, 40)
        self.pendown()
        for _ in range(8):
            self.game_line()
