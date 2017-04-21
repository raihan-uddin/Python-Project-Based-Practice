import turtle

def drw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    drw_square(brad)

    #Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("white")
    angie.circle(100)
    window.exitonclick()

draw_art()