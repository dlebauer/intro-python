# from https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((128, 0, 0))


alien = Actor('alien')
alien.pos = 100, 56
alien.topright = 0, 10


WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")


# last line
pgzrun.go()
