# from https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun
#import random

WIDTH = 500
HEIGHT = 1000

alien = Actor('alien')
alien.pos = WIDTH/2, 0
alien.vy = 0
GRAVITY = 0.1

def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()

def update():
    update_alien()
    
def update_alien():
    alien.vy += GRAVITY
    alien.y += alien.vy
    if keyboard.left:
        alien.x -= 5
    elif keyboard.right:
        alien.x += 5    
    if keyboard.up:
        alien.y -= 10    
    elif keyboard.down:
        alien.y += 5   
    if alien.y > HEIGHT:
        alien.y = 0
        alien.vy = 0

# last line
pgzrun.go()
