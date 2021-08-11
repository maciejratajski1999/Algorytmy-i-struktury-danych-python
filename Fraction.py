class Fraction:
    '''
    Class Fraction
     acts as a Fraction of two integers: nominator / denominator
    '''

    def __init__(self, num, dem):
        '''
        :param num (int): Numerator of a Fraction
        :param dem (int): Denominator of a Fraction

        given parameters are tested, if valid the Fraction gets simplified if possible
        self.numerator (int): Numerator after simplification
        self.denominator (int): Denominator after simplification
        '''
        num, dem = self.__test_args(num, dem)
        gcd = self.gcd(num, dem)
        self.numerator = int(num / gcd)
        self.denominator = int(dem / gcd)

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        other = self.__test_other(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        dem = self.denominator * other.denominator
        return Fraction(num, dem)

    def __sub__(self, other):
        other = self.__test_other(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        dem = self.denominator * other.denominator
        return Fraction(num, dem)

    def __mul__(self, other):
        other = self.__test_other(other)
        num = self.numerator * other.numerator
        dem = self.denominator * other.denominator
        return Fraction(num, dem)

    def __reciprocal(self, other):
        '''
        :param other (Fraction(a,b)):
        :return: Fraction(b,a)
        '''
        return Fraction(other.denominator, other.numerator)

    def __truediv__(self, other):
        other = self.__test_other(other)
        return self * self.__reciprocal(other)

    def __eq__(self, other):
        other = self.__test_other(other)
        return (self.numerator == other.numerator and self.denominator == other.denominator)

    def __lt__(self, other):
        other = self.__test_other(other)
        return (self.numerator / self.denominator < other.numerator / other.denominator)

    def __le__(self, other):
        other = self.__test_other(other)
        return (self.numerator / self.denominator <= other.numerator / other.denominator)

    def __gt__(self, other):
        other = self.__test_other(other)
        return (self.numerator / self.denominator > other.numerator / other.denominator)

    def __ge__(self, other):
        other = self.__test_other(other)
        return (self.numerator / self.denominator >= other.numerator / other.denominator)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def __convert_args(self, num, dem):
        if isinstance(num, int) and isinstance(dem, int):
            return num, dem
        elif (isinstance(num, float) and isinstance(dem, int)) or (isinstance(num, int) and isinstance(dem, float)) or (
                isinstance(num, float) and isinstance(dem, float)):
            '''if one of the parameters is float and the other an integer or both are floats'''
            return self.__float_to_fraction(num / dem)
        elif isinstance(num, str) or isinstance(dem, str):
            try:
                return self.__convert_args(float(num), float(dem))
            except:
                raise TypeError("wrong input Type, numerator and denominator must be numbers")

    def __test_args(self, num, dem):
        num, dem = self.__convert_args(num, dem)
        if dem == 0:
            raise ZeroDivisionError("denominator can't be equal to 0")
        if dem < 0:
            num = 0 - num
            dem = 0 - dem
        return num, dem

    def __float_to_fraction(self, number):
        '''
        :param number (float): number to be converted
        :return:
            int(other), 10**divisor - how many times should the int(other) be divided to be equal to :param number
            number == Fraction(int(other), 10**divisor)
        '''
        other = str(number)
        divisor = len(other) - other.find(".") - 1
        other = [digit for digit in other if digit != "."]
        other = ''.join(other)
        return int(other), 10 ** divisor

    def __test_other(self, other):
        if isinstance(other, Fraction):
            return other
        elif isinstance(other, int):
            return Fraction(other, 1)
        elif isinstance(other, float):
            num, dem = self.__float_to_fraction(other)
            return Fraction(num, dem)
        else:
            other_type = str(type(other))
            raise TypeError("Wrong value: " + str(other) + ", type " + other_type + " not supported for this operation")
