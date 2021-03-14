from turtle import Turtle
FONT = ("Arial",24,"normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        try:
            with open("highscore.txt", "r") as saved:
                self.highscore = int(saved.read())

        except FileNotFoundError:
            self.highscore = 0


        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.color("white")
        self.updateScore()
    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align= ALIGNMENT,font=FONT)

    def increaseScore(self):
        self.score +=1
        self.updateScore()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            try:
                with open("highscore.txt", "w+") as saved:
                    saved.write(f"{self.highscore}")


            except FileNotFoundError:
                with open("highscore.txt", "w+") as saved:
                    saved.write(f"{self.highscore}")

            else:

                with open("highscore.txt", "w+") as saved:
                    saved.write(f"{self.highscore}")

            finally:
                self.score = 0
                self.updateScore()

