#python program to get suitable design
from turtle import *

from random import randint          #importing randint from random

speed(0)                            #setting the animation speed to 0

bgcolor('black')                    #background color of Turtle Graphics

x = 1

while x < 400:
    
    r = randint(0,255)              #red or r ranges from 0 to 255 for different color
    g = randint(0,255)              #green or g ranges from 0 to 255 for different color
    b = randint(0,255) 

    colormode(255)                  #set the color mode for different color values

    pensize(1)                      #setting the turtle size or pen size to 1
    
    pencolor(r,g,b)                 #setting the turtle colour to RGB   

    fd(50 + x)                      #turtle moving 50 units with increment of x in the while loop
    rt(90.911)                      #moving the turtle right angle with the value of 90.911


    x = x+1                         #incrementing the x value

exitonclick()