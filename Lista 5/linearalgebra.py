import numpy as np
from scipy import linalg
import json
from time import time
from matplotlib import pyplot as plt

def generate_equation(n):
    '''
    :param n (int): size of a square matrix, and length of variables vector
    :return (np.array, np.array): random generated square matrix and a vector of variables
    '''
    a = np.array(np.random.rand(n,n))
    b = np.array(np.random.rand(n,1))
    return a,b



def time_tester(n):
    '''
    :param n (int): size of a matrix in equation
    :return (float): time taken to solve equation
    '''
    a, b = generate_equation(n)
    timer = time()
    try:
        linalg.solve(a,b)
    except np.linalg.LinAlgError:
        return 0
    return time() - timer

def generate_data(N):
    '''
    :param N (int): maximal size of a matrix
    :return: [time_tester(0), time_tester... ], [1 , ...]
                list of times it took to solve an equation and a list of sizes of matrix
    '''
    data = []
    step = 1
    size = list(range(1,N+1, step))
    for n in size:
        mean_time = 0
        for i in range(0,step):
            mean_time += time_tester(n+i)
        mean_time = mean_time
        data.append(mean_time)
        print(data[-1],n)
    return data, size

# tutaj generowałem dane
# data, size = generate_data(5000)

# wczytam moje wygenerowane wcześnej dane z plików JSON
data, size = json.load(open("n5000step1.json"))
data2, size2 = json.load(open("n5000step10.json"))

# oś x to rozmiar macierzy, oś y to ilość czasu w sekundach potrzebna na rozwiązanie układu równań
plt.scatter(size, data)
plt.scatter(size2, data2)
plt.savefig("wykres.png")