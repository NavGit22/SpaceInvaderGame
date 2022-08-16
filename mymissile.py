from turtle import Turtle


class Mymissile:
    def __init__(self):
        self.my_missiles = []
        self.x_move = 0
        self.y_move = 10

    def create_missile(self, position):
        missile = Turtle()
        missile.shape('circle')
        missile.color('red')
        missile.penup()
        missile.shapesize(stretch_wid=0.25, stretch_len=0.25)
        missile.goto(position[0], position[1])
        self.my_missiles.append(missile)

    def move(self):
        for missile in self.my_missiles:
            missile.goto(missile.xcor() + self.x_move, missile.ycor() + self.y_move)














