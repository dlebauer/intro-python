import pgzrun

alien = Actor('alien')
alien2 = Actor('alien_hurt')
alien.pos = 250, 250
alien2.pos = 50, 50
#alien.topright = 0, 10
alien.direction = -5,0

WIDTH = alien.height + 1000
HEIGHT = 1000

def draw():
    screen.clear()
    screen.fill((196, 117, 6))
    alien.draw()
    alien2.draw()

def update():
    update2()
    alien.left += 2.5
    alien.angle +=5
    dx, dy = alien.direction
    alien.move_ip(dx, dy)
    if alien.left > WIDTH:
        alien.right = 0
        alien.left += 2.5

def update2():
    alien2.angle +=5

def on_mouse_move(pos):
    alien.angle = alien.angle_to(pos)
    animate(alien, pos = pos, duration = 1, tween = 'linear', on_finished = set_alien_hurt )
    alien2.angle = alien2.angle_to(pos)
    animate(alien2, pos = pos, duration = 1, tween = 'linear', on_finished = set_alien_hurt )

def set_alien_hurt():
    sounds.eep.play()
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'

# last line
pgzrun.go()
