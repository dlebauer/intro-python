# Introduction to coding with Python

_These are class notes_ for a group of elememtary and middle school students who have learned fundamentals of programming and are comfortable with the Scratch block-based programming language. They learned using Google's CSFirst platform.

We meet 1h/week, have minimal homework, and are starting by loosely following the textbook [Python for Kids](https://www.amazon.com/Python-Kids-Playful-Introduction-Programming/dp/1593274076). The primary goal is for the students to have fun. The curriculum will be guided by student interests.

### Lesson 1: 

- From Scratch to Python
- Introduction to the Python console
- Operators +,-,*,/,>,<
- Numbers and Strings
- Variables  
- Lists
- Subsetting lists

**class notes / code snpippets:** [lesson_1.py](https://github.com/dlebauer/intro-python/blob/master/lesson_1.py)

**Homework:** Use variables and operators to solve one of your homework problems

### Lesson 2: 

- Intro to the Interactive Development Environments (IDE)
  - a text file and a console
  - we will start with a blank 'Trinket' https://trinket.io/python3/9fa205cb41?runMode=console
- lists
- the `print` statement
- string substitution
- for loops and indexing

**class notes / code snpippets:** [lesson_2.py](https://github.com/dlebauer/intro-python/blob/master/lesson_2.py)

**Homework**:

- Use a list, a for loop, and operators to solve the following:

On Monday you find a goose that lays diamond eggs. It lays the first egg that day, and you take it to a jewelery store. The owner says it is worth 3 million dollars! On Tuesday you find out that it lays one egg per day. Write a for loop program that tells you how much many diamonds you will have on Tuesday, Wednesday, Thursday, and Friday and how much they will be worth. Specifically, write a loop that prints the following output:

```python
On Tuesday you have 2 eggs worth 3 million dollars
On Wednesday you have 2 eggs worth 6 million dollars
On Thursday you have 3 eggs worth 9 million dollars
On Friday you have 4 eggs worth 12 million dollars
```

Hint: see the [lesson 2 notes](https://github.com/dlebauer/intro-python/blob/master/lesson_2.py)

### Lesson 3:

- review homework
  - solve homework w/ dictionaries
  - create vectors eggs and value
  - plot eggs vs value
- draw pictures with turtles

## Lesson 4: 

- control the screen size
- images: 
   - find and download using google image search
   - create and export using google drawings
   - import into trinket
- add background image and change turtle image https://trinket.io/python/041c755b35

## Lesson 5

- how to write a function
- control the turtle with up/down/left/right keys https://trinket.io/python/89f11c3faf


## Lesson 6: 

- install IDE on your computer
- start learning either arcade or pygame!

Homework

- Create a new project in PyCharm or Spyder 
- save this image in a folder named 'images/' https://pygame-zero.readthedocs.io/en/stable/_images/alien.png
- cut and paste this into your file named main.py :  https://raw.githubusercontent.com/dlebauer/intro-python/master/lesson_6_alien_run.py
- Run the game. Try to click on the alien and see what happens.

Answer the following questions:
  1. what does += mean?
  2. how does the alien get from the left side to the right side?
  3. how does the alien get back from the right side to the left side?
  4. how can you make the alien say 'Eek!'?


## Lesson 7:

Today we continued working through the pgzero tutorials - and learned how to get the alien to make a sound 
Answers to questions in todays class are below. 


1. What is that IDE some students were using that looked so much easier to use than PyCharm or Spyder?
  - I just learned about this last week - it is called 'Mu' and it is designed specifically to make it easier to learn (by hiding all of the fancy stuff that PyCharm and Spyder offer). It is pre-configured for learning with pgzero!!!
  - You can download it from https://codewith.mu/
2. How to change the background color?
  - add `screen.fill((255, 87, 51))` to turn the background red
  - The three numbers `(255, 87, 51)` refer to the red, green, and blue content on a scale of 0-255. 
     - You can find the three numbers required for any particular by googling "color picker" https://www.google.com/search?q=color+picker
     
3. How to have the alien chase the mouse?
   - Add `animate(alien, pos = pos, duration = 1, tween = 'bounce_end')` to the function `on_mouse_down`, e.g.:
   
```python
def on_mouse_down(pos):
    alien.angle = alien.angle_to(pos)
    animate(alien, pos = pos, duration = 1, tween = 'bounce_end')
    if alien.collidepoint(pos):
        set_alien_hurt()
    else:
        print("You missed me!")
```   

This will make the alien go to wherever you clicked. If you want the alien to always follow the mouse, you can add this function:

```
def on_mouse_move(pos):
    alien.angle = alien.angle_to(pos)
    animate(alien, pos = pos, duration = 1, tween = 'bounce_end')
```

Here is the code from the end of today's lesson that includes the sound response, red background, and following functionality: https://github.com/dlebauer/intro-python/blob/master/lesson_7_alien_eep.py 
