from turtle import Turtle
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-230, y=250)
        self.level = 1
        self.write(arg=f'Level {self.level}', align='center', font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f'Level {self.level}', align='center', font=FONT)