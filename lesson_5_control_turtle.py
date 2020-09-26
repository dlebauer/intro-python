# https://stackoverflow.com/q/44863600/199217
import turtle

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(10)
# Create a variable `screen`, a Screen() object, that will handle keyss
screen = turtle.Screen()

# Define functions for each arrow key
def go_left():
  tina.left(7)

def go_right():
  tina.right(7)

def go_forward():
  tina.forward(10)

def go_backward():
  tina.backward(10)

# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

# Tell the screen to listen for key presses
screen.listen()
turtle.done()
