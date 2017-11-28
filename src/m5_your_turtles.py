"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ryan Epstein
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.

import rosegraphics as rg

window = rg.TurtleWindow()

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 3)
red_turtle.speed = 10

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 3)
blue_turtle.speed = 10

for k in range (3):
    blue_turtle.right(90)
    blue_turtle.forward(30)


for k in range (3):
    red_turtle.left(90)
    red_turtle.forward(30)


#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
