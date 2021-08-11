import turtle


def draw_Hilbert_curve(n):
    step = int(200/n)
    middle = int(step/2)
    height, width = (2**n)*step, (2**n)*step
    hilbert_curve = turtle.Screen()
    hilbert_curve.setup(height,width)
    hilbert_turtle = turtle.Turtle()
    hilbert_turtle.penup()

    hilbert_turtle.goto(-height/2 + middle, width/2 - middle)

    hilbert_turtle.pendown()


    def first_iteration(degree):
        hilbert_turtle.forward(step)
        hilbert_turtle.left(degree)
        hilbert_turtle.forward(step)
        hilbert_turtle.left(degree)
        hilbert_turtle.forward(step)

    def second_iteration(degree):
        first_iteration(degree)
        hilbert_turtle.right(degree)
        hilbert_turtle.forward(step)
        first_iteration(360 - degree)
        hilbert_turtle.left(degree)
        hilbert_turtle.forward(step)
        hilbert_turtle.left(degree)
        first_iteration(360 - degree)
        hilbert_turtle.forward(step)
        hilbert_turtle.right(degree)
        first_iteration(degree)

    orientation = n % 2 == 1
    if orientation:
        hilbert_turtle.right(90)
    turn = {True: 90, False:270}
    if n == 1:
        first_iteration(turn[orientation])
    elif n == 2:
        second_iteration(turn[orientation])
    else:
        pass





draw_Hilbert_curve(3)