import  turtle

def draw_patern(t):
    t.pendown()
    t.forward(100)
    t.right(30)
    t.forward(60)
    t.left(30)
    t.forward(30)
    t.penup()
    t.home()

def draw_art():
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(30)
    move = 1
    for i in range(360):
        draw_patern(t)
        t.right(move)
        move +=1
    window.exitonclick()

draw_art()