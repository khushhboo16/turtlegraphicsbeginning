import turtle as t
import random
pig= t.Turtle()
colours=["red", "dark orchid" , "dark blue" , "orange red" , "purple" , "yellow" , "lime"]
directions = [0, 90, 180, 270]
pig.pensize(15)

for i in range(200):
  pig.color(random.choice(colours))
  pig.forward(30)
  pig.setheading(random.choice(directions))
