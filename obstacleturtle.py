

from turtle import Turtle

class WallTurtle(Turtle):
  def __init__(self, starting_x, starting_y, x_size, y_size):    
   
   
    Turtle.__init__(self)
   
    
    # Sets up incoming variables
    self.starting_x = starting_x
    self.starting_y = starting_y
    self.x_size = x_size
    self.y_size = y_size
    self.speed(1000)

   

    #set turtle starting states
    self.shape("square")
    self.color("black")
    self.penup()
    self.goto(self.starting_x, self.starting_y)
    self.shapesize(self.x_size, self.y_size)
