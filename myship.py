from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Myship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(UP)
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 360:
           self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -380:
            self.goto(new_x, self.ycor())

    def get_ship_loc(self):
        return (self.xcor(), self.ycor())

    def game_over(self):
        gameover = Turtle()
        gameover.color('white')
        gameover.hideturtle()
        gameover.penup()
        gameover.clear()
        gameover.goto(0, -200)
        text = "!!!! GAME OVER !!!!!"
        gameover.write(text, align='center', font=('courier', 20, 'normal'))