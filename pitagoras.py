def Pitagoras(n):
    '''
    dla danego n znajduje trójkąt pitagorejski o bokach a,b,c taki, że a + b + c = n

    :param n: szukana suma a+b+c
    :return: a, b, c,
        cnt - suma wykonanych mnożeń
        cnt(n) ~~ (3/8)*n^2
        złożoność Pitagoras należy do O(n^2)
    '''
    cnt = 0
    for a in range(1, int(n/2)):
        for b in range(a, int(n/2)):
            c = n - a - b
            cnt = cnt + 3
            if a + b + c == n and a ** 2 + b ** 2 == c ** 2:
                return a,b,c, str(cnt)


def Pitagoras2(N):
    '''
    dla danego N znajduje trójkąt pitagorejski o bokach a,b,c taki, że a + b + c = N
    nie działa dla wszystkich N, ale dla większości znajduje znacznie szybciej


    :param N: szukana suma a+b+c
    :return: a, b, c,
        cnt - suma wykonanych mnożeń
        cnt(N) pesymistycznie ~~ (1/2)*N^2 + 6
        złożoność Pitagoras2 należy do O(n^2)
    '''
    cnt = 0
    for n in range(1, int(N/2)):
        for m in range(n, int(N/2)):
            cnt = cnt + 4
            if (2*(m**2) + 2*m*n) == N:
                cnt = cnt+6
                return (m**2 - n**2), (2*m*n), (m**2 + n**2), str(cnt)
    return cnt

'Zadanie 3.' \
'Dla przypadku N = 1000, wystarczy znaleźć parę liczb m > n,' \
'taką aby ([m^2 - n^2] + [2*m*n] + [m^2 + n^2]) było równe 1000' \
'[m^2 - n^2] = a' \
'[2*m*n] = b' \
'[m^2 + n^2] = c'


