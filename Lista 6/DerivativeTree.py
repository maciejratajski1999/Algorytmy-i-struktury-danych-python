class Expression:
    class Constant:
        def __init__(self, v):
            self.v = v

        def __str__(self):
            return str(self.v)

        def derivative(self, x):
            return Expression.Constant(0)

    class Plus:
        def __init__(self, a, b):
            self.a, self.b = a, b

        def __str__(self):
            return f"({self.a}+{self.b})"

        def derivative(self, x):
            return Expression.Plus(self.a.derivative(x), self.b.derivative(x))

    class Minus:
        def __init__(self, a, b):
            self.a, self.b = a, b

        def __str__(self):
            return f"({self.a}-{self.b})"

        def derivative(self, x):
            return Expression.Minus(self.a.derivative(x), self.b.derivative(x))

    class Variable:
        def __init__(self, v):
            self.v = v

        def __str__(self):
            return f"{self.v}"

        def derivative(self, x):
            if x == self.v:
                return Expression.Constant(1)
            else:
                return Expression.Constant(0)

    class Multiplication:
        def __init__(self, a, b):
            self.a, self.b = a, b

        def __str__(self):
            return f"({self.a}*{self.b})"

        def derivative(self, x):
            return Expression.Plus(Expression.Multiplication(self.a.derivative(x), self.b),
                                   Expression.Multiplication(self.a, self.b.derivative(x)))

    class Division:
        def __init__(self, a, b):
            self.a, self.b = a, b

        def __str__(self):
            return f"({self.a}/{self.b})"

        def derivative(self, x):
            return Expression.Division(Expression.Minus(Expression.Multiplication(self.a.derivative(x), self.b),
                                                        Expression.Multiplication(self.a, self.b.derivative(x))),
                                       Expression.Multiplication(self.b, self.b))

    class Logarithm:
        def __init__(self, x):
            self.x = x

        def __str__(self):
            return f"ln({self.x})"

        def derivative(self, y):
            return Expression.Division(self.x.derivative(y), self.x)

    class Power:
        def __init__(self, a, b):
            self.a, self.b = a, b

        def __str__(self):
            return f"({self.a}^{self.b})"

        def derivative(self, x):
            a = Expression.Power(self.a, self.b)
            b = Expression.Multiplication(self.a.derivative(x), Expression.Division(self.b, self.a))
            return Expression.Multiplication(a, Expression.Plus(b, Expression.Multiplication(self.b.derivative(x),
                                                                                             Expression.Logarithm(
                                                                                                 self.a))))