from turtle import Turtle, Screen
from myship import Myship
from mymissile import Mymissile
from alienships import Aliens
import time


# Shoot the Alien Spaceship
def shoot():
    my_missile.create_missile(my_ship.get_ship_loc())
    my_missile.move()


# Display a Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Space Invader Game")
screen.tracer(0)

# Display my spaceship
my_ship = Myship((0, -250))

# Display the missile
my_missile = Mymissile()

# Create Alien Ships bricks
aliens = Aliens()
aliens.create_aliens()

screen.listen()

# Move your spaceship left and right and Up to shoot the alien spaceship
screen.onkey(key="a", fun=my_ship.go_left)
screen.onkey(key="d", fun=my_ship.go_right)
screen.onkey(key="Left", fun=my_ship.go_left)
screen.onkey(key="Right", fun=my_ship.go_right)
screen.onkey(key='Up', fun=shoot)

game_is_on = True
sleep_timer = 0.1

while game_is_on:
    screen.update()
    if sleep_timer < 0:
        sleep_timer = 0.1
    time.sleep(sleep_timer)

    # Move my missile up to hit Alien Spaceship
    my_missile.move()

    # Move aliens spaceship right to left and left to right
    aliens.move()

    # Move aliens spaceship one row down when it hit the wall
    aliens.move_down()

    # Fire missiles from alien spaceship
    aliens.fire_missiles()
    aliens.move_alien_missiles()
    aliens.check_missile_range()

    # Detect Collision of your missile with alien spaceship
    for missile in my_missile.my_missiles:
        for alien in aliens.all_aliens:
            if alien.distance(missile) < 10:
                alien.hideturtle()
                aliens.all_aliens.remove(alien)

    # Detect Collision of alien spaceship missile with your missile
    for a_missile in aliens.alien_missiles:
        for o_missile in my_missile.my_missiles:
            if a_missile.distance(o_missile) < 10:
                a_missile.hideturtle()
                o_missile.hideturtle()
                aliens.alien_missiles.remove(a_missile)
                my_missile.my_missiles.remove(o_missile)

    # Detect Collision of alien spaceship missile with your spaceship
    for a_missile in aliens.alien_missiles:
        if my_ship.distance(a_missile) < 10:
            my_ship.game_over()
            game_is_on = False

    # Detect Collision of alien spaceship with your spaceship
    for alien in aliens.all_aliens:
        if my_ship.distance(alien) < 10:
            my_ship.game_over()
            game_is_on = False



screen.exitonclick()