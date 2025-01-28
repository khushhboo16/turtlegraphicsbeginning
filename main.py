import turtle as t
import random
pig= t.Turtle()

directions = [0, 90, 180, 270]
pig.pensize(15)
t.colormode(255)

def random_color():
  r= random.randint(0,255)
  g= random.randint(0,255)
  b= random.randint(0,255)
  random_color=(r,g,b)
  return random_color
for i in range(200):
  pig.color(random_color())
  pig.forward(30)
  pig.setheading(random.choice(directions))
  
