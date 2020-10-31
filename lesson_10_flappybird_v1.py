import pgzrun

WIDTH = 400
HEIGHT = 708

bird = Actor('bird1', (75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

def reset_pipes():
    pipe_gap_y = HEIGHT / 2
    pipe_top.pos = (WIDTH, pipe_gap_y - 100)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + 100)

pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
reset_pipes()  # Set initial pipe positions.

def update_pipes():
    pipe_top.left -= 2
    pipe_bottom.left -= 2
    if pipe_top.right < 0:
        reset_pipes()

def update_bird():
    bird.vy += 0.2
    bird.y += bird.vy / 2
    bird.x = 75
    if bird.vy < 0:
        bird.image = 'bird2'
    else:
        bird.image = 'bird1'
    if bird.y < 0 or bird.y > HEIGHT:
        bird.y = 200
        bird.vy = 0
        reset_pipes()

def update():
    update_pipes()
    update_bird()

def on_key_down():
    bird.vy = -2.5

def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()

pgzrun.go()

