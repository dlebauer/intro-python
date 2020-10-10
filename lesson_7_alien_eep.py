import pgzrun

alien = Actor('alien')
alien.pos = 100, 56
alien.topright = 0, 10


WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    screen.fill((255, 87, 51))
    alien.draw()

def update():
    alien.left += 0.5
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    animate(alien, pos = pos, duration = 1, tween = 'bounce_end')
    if alien.collidepoint(pos):
        set_alien_hurt()
    else:
        print("You missed me!")

#def on_mouse_move(pos):
#    alien.angle = alien.angle_to(pos)
#    animate(alien, pos = pos, duration = 1, tween = 'bounce_end')

def set_alien_hurt():
    sounds.eep.play()
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'

# last line
pgzrun.go()
