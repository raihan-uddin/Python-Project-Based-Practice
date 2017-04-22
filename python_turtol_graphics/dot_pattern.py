import  turtle

def draw_pattern(t, height, width, dot_distance):
    for i in range(height):
        for i in range(width):
            t.dot()
            t.forward(dot_distance)
        t.back(dot_distance*width)
        t.right(90)
        t.forward(dot_distance)
        t.left(90)

def draw_art():
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(50)
    dot_distance = 10
    width = 20
    height = 20
    t.penup()
    draw_pattern(t, height, width, dot_distance)


    window.exitonclick()

draw_art()