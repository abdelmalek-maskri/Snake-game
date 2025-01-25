from food import Food
from turtle import Turtle

FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle): 
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScore()
        self.hideturtle()


    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.updateScore()

    def reset(self):
        if self.score > self.highScore:
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            self.highScore = self.score
        self.score = 0
        self.updateScore()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=FONT)
        