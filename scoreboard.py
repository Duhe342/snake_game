from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.01, stretch_len=0.01)
        self.penup()
        self.hideturtle()
        self.goto((0, 270))
        self.color("White")
        self.number = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.number}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.number += 1
        self.clear()
        self.update_scoreboard()

    def set_game_over(self):
        self.goto((0, 0))
        self.write("Game Over", align=ALIGNMENT, font=FONT)

