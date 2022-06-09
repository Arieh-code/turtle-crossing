from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.level = 1
        self.start_game()

    def start_game(self):
        self.write(f"level: {self.level}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)
