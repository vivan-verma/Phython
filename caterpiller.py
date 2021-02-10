
'''
#Create a catterpiller
import random # imports the random command

import turtle   #turtle is being imported

t = turtle.Turtle() # assigning t for turtle

t.penup() # raises the pen up to not draw

RADIUS = 30 # sets the radius of the cirlce

DIAMETER = RADIUS * 2 #Find Diameter

x = -300 #starts at the coordiante (-300,x)

y = 0 # y value is 0 

colors = ['red', 'green', 'purple', 'pink', 'black', 'orange','gray'] #Gives different colors to the code

t.goto(x,y) #moves the pen to the coordiante

for i in range(10): #ets a range from 0 - 10
    t.penup() #Brings the pen up
    
    t.color(random.choice(colors)) #gives a random color from the colors variable

    t.penup() #does not draw
    
    t.begin_fill() #fills the circle with a green color
 
    t.circle(RADIUS) #draws a circle with a radius of 50

    t.end_fill() #fills the color in green
    
    t.penup()  #Brings the pen up
    
    t.goto((x + (i + 1) * DIAMETER), y) #Changes the x value by the diameter multiplied by the radius times the number of circles

t.penup() #picks up the pen

t.color('black') #assigns color to be black


t.begin_fill() #begins to fill the color black

y = 5 # new coordinates

x = 270 # new coordinates

t.goto(x,y)#moves to new coordinates

t.pendown()#begins to draw

t.circle(15) #circle radius 15

t.end_fill()#fills the color in black

t.penup() #picks up pen

y = 30 #new coordinates

x = 270 # new coordinates

t.begin_fill() #begins to fill with black

t.goto(x,y) #moves to new coordinates

t.pendown() #begins to draw

t.circle(15) #circle radius 15

t.end_fill() #fills the color in black
'''
import turtle   #turtle is being imported

t = turtle.Turtle() # assigning t for turtle

t.penup()
t.color("red")
t.speed(50)

for i in range(12):
    t.goto(0,0)

    t.forward(100)

    t.pendown()

    t.begin_fill()

    t.circle(5)

    t.end_fill()

    t.penup()

    t.goto(0,0)

    t.right(30)

t.penup()
t.goto(0,0)
t.write("CLOCK")

