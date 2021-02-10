import turtle; #imports turtle

t = turtle.Turtle() #assigns t

t.penup() #lifts the penup
t.color("red") #color becomes red
t.speed(50) #speed is assigned

for i in range(12): 
 
 t.goto(0,0) # goes to 0,0 

 t.forward(100) #moves forward 100

 t.pendown() # begins to draw
 
 t.begin_fill() #fills a color red
 
 t.circle(5) # fills a circles with a radius of 5 
 t.end_fill() #fills in the color 
 
 t.penup() #lifts pen up

 t.goto(0,0) #back to 0,0

 t.right(30) #moves right 30
 
t.penup()
t.goto(0,0)
t.write("CLOCK")
