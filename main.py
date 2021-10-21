from turtle import Screen
from keyboardturtle import KeyboardTurtle
from movingturtle import MovingTurtle
from obstacleturtle import WallTurtle


# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

# set up clickable instance


wall_list = []
#set up players
player_1 = KeyboardTurtle(window, walls = wall_list)


player_1.goto(-100,-95)

# set target of other player(our collison check) to the opposite player

moveT = MovingTurtle(screen_width)

#list setup 

#Create Wall



w28 = WallTurtle(62, 50, 3.5, .25)
wall_list.append(w28)

w27 = WallTurtle(-43, 39, .125, 7)
wall_list.append(w27)

w26 = WallTurtle(-20, 3, 1, 1)
wall_list.append(w26)
w26.color("crimson")

w25 = WallTurtle(10, -42, 1, 1)
wall_list.append(w25)
w25.color("dark orange")

w24 = WallTurtle(-43, -42, 1, 1)
wall_list.append(w24)
w24.color("gold")

w23 = WallTurtle(-20, -87, 1, 1)
wall_list.append(w23)
w23.color("spring green")

w22 = WallTurtle(-70, 3, 1, 1)
wall_list.append(w22)
w22.color("cyan")

w21 = WallTurtle(-93, -42, 1, 1)
wall_list.append(w21)
w21.color("dodger blue")

w20 = WallTurtle(-70, -87, 1, 1)
wall_list.append(w20)
w20.color("dark magenta")

w19 = WallTurtle(-210, 20, .25, 3.25)
wall_list.append(w19)

w18 = WallTurtle(-150, -20, .25, 4)
wall_list.append(w18)

w17 = WallTurtle(-120, -20, 6, 1)
wall_list.append(w17)

w16 = WallTurtle(140, -98, 8.4, 1)
wall_list.append(w16)

w15 = WallTurtle(90, -23, 1, 6)
wall_list.append(w15)

w14 = WallTurtle(90, -120, 5.5, 1)
wall_list.append(w14)

w13 = WallTurtle(40, -70, 5.7, 1)
wall_list.append(w13)

w12 = WallTurtle(-50, -130, 1, 10)
wall_list.append(w12)

"""
w11 = WallTurtle(-190, -8, 1, 10)
wall_list.append(w11)
"""

w10 = WallTurtle(-200, -70, 1, 3)
wall_list.append(w10)

w9 = WallTurtle(-190, -130, 1, 5.4)
wall_list.append(w9)

w8 = WallTurtle(-234, -40, 4, 1)
wall_list.append(w8)

w7 = WallTurtle(-234, 32, 5, 1)
wall_list.append(w7)

w6 = WallTurtle(41, 77, 1, 28.5)
wall_list.append(w6)

w5 = WallTurtle(-41, 132, 1, 27)
wall_list.append(w5)

w4 = WallTurtle(286, 0, 500, 1)
wall_list.append(w4)

w3 = WallTurtle(0, -186, 1, 500)
wall_list.append(w3)

w2 = WallTurtle(-290, 0, 500, 1)
wall_list.append(w2)

w1 = WallTurtle(0, 190, 1, 500)
wall_list.append(w1)




# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment