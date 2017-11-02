import turtle

my_turtle = turtle.Turtle()
i=25
while(True):
    i=i+5
    my_turtle.forward(i)
    my_turtle.left(90)
    if i==500:
        break
    
