from turtle import Turtle
from obstacleturtle import WallTurtle

class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               window,  
               straight = "Up", 
               turn_right = "Right",
               turn_left = "Left",
               back = "Down",
               wall_turtle = WallTurtle,
               other_player = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.window = window
    self.straight = straight
    self.turn_right = turn_right
    self.back = back 
    self.turn_left = turn_left
    self.other_player = other_player
    self.WallTurtle = wall_turtle

    #set turtle starting states
    self.shape("turtle")
    self.color("green")
    self.penup()

    # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_forward, self.straight)
    self.window.onkey(self.go_left, self.turn_left)
    self.window.onkey(self.go_back, self.back)

    #sets up controlling variables (y not implemented)
    self.movement_speed = 2
    self.turn_speed = 20
    self.collision_distance = 5

  # Movement Methods
  def go_forward(self):
    self.forward(self.movement_speed)
    if self.check_collision(self.wall_turtle):
      print("crash")
      quit()
      
  def go_right(self):
    self.right(self.turn_speed)

  def go_left(self):
    self.left(self.turn_speed)

  def go_back(self):
    self.forward(-self.movement_speed)
    if self.check_collision(self.wall_turtle):
      print("crash")
      quit()

  


  # Useful Methods

  # This checks if object collides with another object.  
  # Right now it checks against the other player, but 
  # it doesn't NEED to.  It can check against any
  # other turtle object

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False


    # TODO: finish setting up the inputs (left and down)
    
