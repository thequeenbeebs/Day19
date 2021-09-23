# INSTANCES, STATE, AND HIGHER ORDER FUNCTIONS

# Higher Order Functions and Event Listeners
#   Turtle Event Listeners - .listen()
#   Functions as Inputs - do not use the parentheses, only the name
#   Higher Order Function - a function that can work with other functions

# Object State and Instance
#   Each creation of an object is a different "instance" of an object
#   Each instance can have different attributes and do different things
#   State: the attributes of instances of objects - they have different color "states"

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()