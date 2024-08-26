from turtle import *

#############################################################
# functions
#############################################################

def rectangle(lengthA, lengthB):
	for x in range(4):
		if x == 0 or x == 2:
    			forward(lengthA)
		else:
			forward(lengthB)
		left(90)

#############################################################
# turtle setup
#############################################################

setup(width = 1.0, height = 1.0) 
shape("turtle")
speed(10)

#############################################################
# turtle logic
#############################################################

#left(90)
#right(90)
#forward(100)

rectangle(200, 100)

#############################################################
# end
#############################################################

exitonclick()
