## Lesson 10 Class notes 

### Review Coordinate Systems

See https://fcs-cs.github.io/cs1-2018/modules/01-introduction/computer-coordinates/

* Cartesian - used in Scratch. Y pos up, X pos right
* Computer graphics: Y pos down


### Review - separate `update()` into `update_alien()`

Change this:

```python
def update():
    if keyboard.up:
        alien.y -= 5    
```

to this:

```python
def update_alien():
    if keyboard.up:
        alien.y -= 5    
        
def update():
    update_alien()
```

- how many new lines did I add?
  - two lines of code, one empty line of 
- why is this useful? 
  - so that when we have lots of elements on the screen, we can keep track of their behaviors independently

#### Add gravity


##### first attempt: constantly increasing speed

```python
def update_alien():
    alien.y += 1
    if keyboard.up:
        alien.y -= 5     

```

#### second attempt: define velocity

Velocity is speed, with a direction (direction is either x or y)

- Define a new variable "Velocity in Y direction": `alien.vy`
  - if `alien.vy` > 0, which direction will the alien go?
  - what would `alien.vx` mean?
  
* `alien.vy`
* `alien.vx`

```python
GRAVITY = 0.1
def update_alien():
    alien.vy += GRAVITY
    alien.y += alien.vy 
    if keyboard.up:
        alien.y -= 5     
```

- add the following so that the alien keeps going faster, returning to the top each time it goes off the bottom

```python
    if alien.y > HEIGHT:
        alien.y = 0
```

- how would you set alien velocity back to 0 each time it falls off the bottom?

```python
def update_alien():
    alien.vy += GRAVITY
    alien.y += alien.vy 
    if keyboard.up:
        alien.y -= 5     
```

## Lesson 10 Homework


![bird0](images/flappybird/bird0.png)
![bird1](images/flappybird/bird1.png)
![bird2](images/flappybird/bird2.png)

### 1. Setting up 

1. put all of the flappy bird images in your /images folder. They are in https://github.com/dlebauer/intro-python/tree/master/images/flappybird
  - drag and drop or right click --> save as to save to your images folder 
2. Start with [flappybird_v1.py](https://github.com/dlebauer/intro-python/blob/master/lesson_10_flappybird_v1.py)

### 2. Creating a `SPEED` Variable

Create a variable called `SPEED` to control the speed.
This will make it easier to adjust the game speed.

<details>
  <summary>Hint</summary>
  
  - write `SPEED = 1` below `WIDTH` and `HEIGHT` at the top of the program
</details>

<details>
  <summary>Hint</summary>
  
  - replace `pipe_top.left -= 2` with `pipe_top.left -= SPEED`
</details>

- run the program - how did it change?
- make sure the bottom pipe is also moving

<details>
  <summary>Hint</summary>
  
  - `pipe_bottom.left` controls the speed of the bottom pipe
</details>


<details>
  <summary>See the answer </summary>
  
```python
SPEED = 1 # at top with other variables
def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()

```


</details>

### 3. Create a Gravity variable that depends on Speed

- similar to `SPEED` make bird velocity in y direction change by `GRAVITY`
- but, make `GRAVITY` depend on `SPEED` so that when you change SPEED it changes both gravity and pipe speed


<details>
  <summary>Hint </summary>
`GRAVITY = SPEED * 0.2` at the top of the program

</details>


<details>
  <summary>Another hint</summary>
  - hint: change `bird.vy += 0.2`
  
</details>

