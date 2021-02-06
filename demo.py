import turtle
import math
r=turtle.Turtle()
# r.color("red","yellow")
# r.begin_fill()
# r.forward(100)
# r.left(90)
# r.forward(100)
# r.left(90)
# r.forward(100)
# r.left(90)
# r.forward(100)
# r.end_fill()

# r.penup()
# r.forward(20)
# r.pendown()

# r.setheading(180)
# r.forward(100)
# r.setheading(-90)
# r.forward(100)
# r.setheading(0)
# r.forward(100)
# r.setheading(90)
# r.forward(100)
r.begin_fill()
r.color("blue","pink")
r.speed(5)
for i in range(50):
  r.forward(math.sqrt(i)*10)
  r.left(170)
r.end_fill()  
  




turtle.done()
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()