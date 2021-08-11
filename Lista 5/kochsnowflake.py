import turtle

class KochSnowflake:
    '''
    Draws a Koch Snowflake in a square window using turtle module
    n is the level of recursion
    '''

    def __init__(self, size, n):
        '''
        :param size (int): size x size is the dimensions of the window
        :param n (int): level of recursion
        '''
        height, width = size, size
        koch_snowflake = turtle.Screen()
        koch_snowflake.setup(height+10, width+10)
        self.Turtle = turtle.Turtle()
        self.Turtle.speed(0)
        self.Turtle.penup()
        self.Turtle.goto(0 , height/2 )
        self.Turtle.pendown()
        length = ((3) ** (1 / 2)) * width / 2
        self.Turtle.right(60)
        self.__draw_curve(n, length)
        turtle.Screen().exitonclick()
        koch_snowflake.getcanvas().postscript(file="kochsnowflake.eps")

    def __draw_line(self, n, length):
        '''
        :param n (int): depth of recursion (1 is straight line)
        :param length (number): length of a line if n == 1
        '''
        if n == 1:
            self.Turtle.forward(length)
        else:
            length = length/3
            self.__draw_line(n-1, length)
            self.Turtle.left(60)
            self.__draw_line(n - 1, length)
            self.Turtle.right(120)
            self.__draw_line(n-1, length)
            self.Turtle.left(60)
            self.__draw_line(n-1, length)

    def __draw_curve(self, n, length):
        '''
        :param n (int): level of recursion
        :param length: base length between two vertices of a triangle for n==1
        '''
        for i in range(0,3):
            self.__draw_line(n, length)
            self.Turtle.right(120)

# przykładowe wywołanie w oknie 1000x1000 i poziomie rekursji 7
KochSnowflake(1000,4)