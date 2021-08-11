import turtle

class HilbertCurve:
    '''
    Draws a Hilber Curve using the turtle module in a square window
    '''

    def __init__(self, size, n):
        '''
        :param size (int): size of a square window size x size
        :param n (int): given level of recursion
        '''
        pixels = 2**n
        self.step = int(size/pixels)
        middle = int(self.step/2)
        height, width = size, size
        hilbert_curve = turtle.Screen()
        hilbert_curve.setup(height, width)
        self.Turtle = turtle.Turtle()
        self.Turtle.speed(0)
        self.Turtle.penup()
        self.Turtle.goto(-height / 2 + middle, width / 2 - middle)
        self.Turtle.pendown()

        degree = 90
        self.__draw_curve(n, degree)
        turtle.Screen().exitonclick()

    def __draw_curve(self, n, degree):
        '''
        :param n (int): depth of recursion
        :param degree (int): degree of turning
        '''
        if n==0:
            return
        else:
            self.Turtle.right(degree)
            self.__draw_curve(n-1, degree+180)
            self.Turtle.forward(self.step)

            self.Turtle.left(degree)
            self.__draw_curve(n-1, degree)
            self.Turtle.forward(self.step)


            self.__draw_curve(n-1, degree)
            self.Turtle.left(degree)
            self.Turtle.forward(self.step)

            self.__draw_curve(n-1, degree+180)
            self.Turtle.right(degree)


# przykładowe wywołanie w oknie o rozmiarze 1000x1000 dla 5 poziomu rekursji
h = HilbertCurve(1000,3)