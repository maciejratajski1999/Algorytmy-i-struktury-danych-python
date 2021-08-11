class MaxiumumProbability:

    def __init__(self, n, k, p):
        self.n = n
        self.k = k
        self.p = p
        self.negative_p = 1 - p
        # counter of multiplications used
        self.counter = 0

    def __counter(self, n):
        '''
        add n to counter
        '''
        self.counter += n

    def binomial_expansion(self, n, k):
        '''
        counts the bonomial coeficcient without doing any multiplications
         for n >= k
        :param n (int):
        :param k (int):
        :return: binomial coefficient of n choose k
        '''
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return self.binomial_expansion(n - 1, k - 1) + self.binomial_expansion(n - 1, k)

    def exponentiation_by_squaring(self, x, n):
        '''
        counts x to the power of n doing approximately ~~ 2*log2(n) multiplications
        :param x (number):
        :param n (int):
        :return: x^n
        '''
        if n == 0:
            return 1
        if n % 2 == 0:
            self.__counter(2)
            return self.exponentiation_by_squaring(x ** 2, n / 2)
        self.__counter(3)
        return x * self.exponentiation_by_squaring(x ** 2, (n - 1) / 2)

    def probability(self):
        '''
        :return (float): sum i=0 -> k ((n choose i) * p^i * (1-p)^(n-k)
        '''
        # reset the counter
        self.counter = 0
        # [p^0, p^1]
        p_powers = [1, self.p]
        # [(1-p)^(n-k)]
        negative_p_powers = [self.exponentiation_by_squaring(self.negative_p, self.n - self.k)]

        # # the following for loop replaces the fold functions, which python core features lack
        # p_powers = [1, p ... p] ->  1 , k times p
        # p_powers.fold(accumulate = 1, lambda element: accumulate*element)
        # # now p_powers would equal [1, p^1, p^2 ... p^k]
        # # accordingly for (1-p)
        # negative_p_powers = [ (1-p) ... (1-p), (1-p)^(n-k)] k times p, (1-p)^(n-k) at the end
        # negative_p_powers.foldright(accumulate = 1, lambda element: accumulate*element)
        # # negative_p_powers would equal [(1-p)^n, (1-p)^n-1, ... (1-p)^n-k]
        for i in range(1, self.k + 1):
            if i > 1:
                self.__counter(1)
                p_powers.append(p_powers[-1] * self.p)
            self.__counter(1)
            negative_p_powers.append(negative_p_powers[-1] * self.negative_p)
        negative_p_powers.reverse()

        self.__counter(2)
        return sum(
            [self.binomial_expansion(self.n, i) * p_powers[i] * negative_p_powers[i] for i in range(0, self.k + 1)])


# p = MaxiumumProbability(100,4,0.5)
# print(p.probability())
# print(p.counter)

def polynomial(x, a):
    '''
    :param x (number): x for wich the polynomial is evaluated
    :param a (list of numbers): list of coefficients [a0, a1 ... an]

    :return: value of a polynomial(x) =  x^n * an + x^n-1 * an-1 + ... + x*a1 + a0
    '''
    # Horner's method:
    # polynomial(x) = a0 + x*(a1 + x*(a2 + ... + xn-1*(an-1 + an*x)

    # [a0, a1 ... an] changes to --> [an, an-1 ... a0]
    a.reverse()

    # starting value is an
    value = a[0]

    for coefficient in a[1:]:
        # value = x*value + ai for i descending from n-1 to 0
        value = x * value + coefficient
    return value


# print(polynomial(3,[-1,2,-6,2]))

def character_count(path):
    '''
    :param path (string): path to file

    :return counter (dictionary): {"character" : occurences}
    '''

    # convert the content of a file to a string
    file = open(path).read()

    counter = {}

    while len(file) > 0:
        # take the first character in file
        character = file[0]
        # count how many times it occures
        occurrences = file.count(character)
        # add character : occurences to counter dictionary
        counter[character] = occurrences
        # remove all occurences of that counter from file string
        file = file.replace(character, "")

    return counter

# print(character_count("sample_file.txt"))
