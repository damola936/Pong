from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class ScoreBoard(Turtle):
    """Initializes the scoreboard"""

    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.score = 0
        self.goto(x_cord, y_cord)
        self.color("red")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """Updates the score board score"""
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score on the scoreboard"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
