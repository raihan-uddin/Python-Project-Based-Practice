import turtle

def draw_clock(draw):
    draw.penup()
    draw.forward(50)
    draw.pendown()
    draw.forward(25)
    draw.penup()
    draw.forward(15)
    draw.stamp()
    draw.home()

def draw_art():
    window = turtle.Screen()
    draw = turtle.Turtle()
    draw.shape("turtle")
    draw.color("red")
    draw.speed(4)
    move = 30
    draw.stamp()

    for i in range(1,13):
        draw_clock(draw)
        draw.right(move)
        move += 30

    window.exitonclick()

draw_art()