from turtle import *

#############################################################
# functions
#############################################################

def star(edges, length):
    for i in range(edges):
        forward(length)
        right(2*360/edges)
        forward(length)
        left(360/edges)

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

star(8, 200)

#############################################################
# end
#############################################################

exitonclick()
