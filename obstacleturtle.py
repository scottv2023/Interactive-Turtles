from turtle import Screen, Turtle

class WallTurtle(Turtle):
  def __init__(self,                
               x = 0 , 
               y = 190):

    Turtle.__init__(self)


  
    # Sets up incoming variables
    self.x = x
    self.y = y
    self.window = Screen()

    #set turtle starting states
    self.shape("square")
    self.shapesize(1,30,1)
    self.color("gray")
    self.penup()
    self.setx(self.x)
    self.sety(self.y)

  # This checks if object collides with another object.  

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False
   
