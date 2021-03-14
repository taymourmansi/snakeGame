from turtle import Turtle
import random
MAX = 250
MIN = -250
class Food(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomX = random.randint(MIN, MAX)
        randomY = random.randint(MIN, MAX)
        self.goto(x=randomX, y=randomY)