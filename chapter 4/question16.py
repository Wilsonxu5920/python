
import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.speed(0) 
for side_length in range(4, 404, 4): 
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    
    t.penup()
    t.backward(4)  
    t.left(90)  
    t.forward(4)  
    t.right(90)  
    t.pendown()