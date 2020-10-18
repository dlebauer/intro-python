### 1. Get the alien to move at a diagonal

* Starting with this code, change one line to make the alien move at a diagonal, from top left to bottom right
* Hint: you only need to change one line
* Hint 2: how much is the `alien.y` variable changing with each update? 

```python
import pgzrun

WIDTH = 300
HEIGHT = 300

alien = Actor('alien')
alien.pos = WIDTH/2, HEIGHT/2

def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()


def update():
    alien.x += 5
    alien.y += 0
    if alien.x > WIDTH:
       alien.x = 0
    if alien.y > HEIGHT:
       alien.y = 0

pgzrun.go()
```

### 2. Moving the alien with keys:

* Copy-paste the following code to a new file
* you will notice that the arrow keys work, but not as expected.
* fix the code so that it works as expected.
* hint: the line after `if keyboard.left` determines what happens when you hit the left arrow key
* hint 2: `alien.y` determines how the alien position will change on the y-axis

```python
# from https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun


# Homework: make it so the keys move alien in the expected direction
# i.e. up arrow moves alien up, etc


WIDTH = 300
HEIGHT = 300

alien = Actor('alien')
alien.pos = WIDTH/2, HEIGHT/2

def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()


def update():
    if keyboard.left:
        alien.y -= 5
    elif keyboard.right:
        alien.x -= 5    
    if keyboard.up:
        alien.x -= 5    
    if keyboard.down:
        alien.x += 5    
    
pgzrun.go()
```

### 3. Extra Credit: two aliens

* Put two aliens on the screen
* One goes around in a circle, and the other is controlled by the arrow keys
* hint: you will have to create a second alien, e.g. `alien2`
