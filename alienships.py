from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'blue', 'pink']
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Aliens:
    def __init__(self):
        self.all_aliens = []
        self.alien_missiles = []
        self.x_move = 0
        self.y_move = -10
        self.alien_speed = 3
        self.wall_hit = 0

    def create_aliens(self):
        ycor = 100
        while ycor < 280:
            xcor = -200
            while xcor < -180 or xcor < 180:
                alien = Turtle('turtle')
                alien.shapesize(stretch_wid=1, stretch_len=1)
                alien.penup()
                alien.color(random.choice(COLORS))
                alien.goto(xcor, ycor)
                alien.setheading(DOWN)
                xcor = xcor + 40
                self.all_aliens.append(alien)
            ycor = ycor + 50

    def move(self):
        self.wall_hit = 0
        for alien in self.all_aliens:
            x = alien.xcor()
            x += self.alien_speed
            alien.setx(x)

            if alien.xcor() > 320:
                self.wall_hit = 1
                y = alien.ycor()
                self.alien_speed *= -1
                alien.sety(y)

            if alien.xcor() < -320:
                self.wall_hit = 1
                y = alien.ycor()
                self.alien_speed *= -1
                alien.sety(y)

    def move_down(self):
        if self.wall_hit:
            for alien in self.all_aliens:
                y = alien.ycor()
                y -= 20
                alien.sety(y)

    def fire_missiles(self):
        for alien in self.all_aliens:
            if random.randint(1, 200) == 6:
                missile = Turtle('circle')
                missile.shapesize(stretch_wid=0.25, stretch_len=0.25)
                missile.penup()
                missile.color('blue')
                missile.goto(alien.xcor(), alien.ycor())
                self.alien_missiles.append(missile)

    def move_alien_missiles(self):
        for missile in self.alien_missiles:
            missile.goto(missile.xcor() + self.x_move, missile.ycor() + self.y_move)

    def check_missile_range(self):
        for missile in self.alien_missiles:
            if missile.ycor() < -250:
                missile.hideturtle()
                self.alien_missiles.remove(missile)
