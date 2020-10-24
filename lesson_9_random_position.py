import pgzrun
import random

WIDTH = 800
HEIGHT = 600

alien = Actor("alien")
alien.pos = WIDTH / 2, HEIGHT / 2


def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    # screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    alien.draw()


def update():
    alien.x += random.randint(1, 20)
    alien.y += random.randint(-10, 10)
    if alien.x > WIDTH:
        alien.x = 0
        alien.y = random.randint(0, HEIGHT)
    if alien.y > HEIGHT:
        alien.y = 0

pgzrun.go()
