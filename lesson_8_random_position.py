# from https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun
import random

WIDTH = 300
HEIGHT = 300


alien = Actor('alien')
alien.pos = 100, 56
alien.topright = 0, 10


WIDTH = 500
HEIGHT = 1000

def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()

def update():
    alien.left += 20
    if alien.left > WIDTH:
        alien.pos = (0, random.randint(1,1000))

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")


# last line
pgzrun.go()# Write your code here :-)
