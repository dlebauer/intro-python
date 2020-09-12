import turtle

tina = turtle.Turtle()
tina.write("Hello world")

tina.forward(50)
tina.right(45)
tina.forward(50)

tina.clear()

#tina.shape('turtle')
tina.forward(200)
#for i in range(0,4):
#  tina.forward(20)
#  tina.left(90)
  

tony = turtle.Turtle()



tony.color('red')
tony.forward(30)
tony.left(120)
tony.forward(30)
tony.left(120)
tony.forward(30)

tina.clear()
tina.color('green')
tina.penup()
tina.goto(100, 100)
tina.pendown()
tina.goto(-100, 100)
tina.goto(-100, -100)
tina.goto(100, -100)
tina.goto(100, 100)




tony.color('red')
for i in range(0, 100):
  tony.forward(30+i)
  tony.left(30)

