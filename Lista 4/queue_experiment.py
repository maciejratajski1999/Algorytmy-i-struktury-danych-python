from kolejka import FrontFIFOQueue
from matplotlib import pyplot as plt
# zadanie 3
# pomysł na zadanie przyszedł gdy stałem w łączonej kolejce do 3 kas w ruchliwym sklpeie
#
# Kierownik fast fooda zastanawia się czy bardziej opłaca expected_value się ustawiać klientów w jedną kolejkę, czy też rozbijać kolejkę na kilka kas
#
# Klientom, wydaje się, że pojedyncza kolejka porusza się szybciej, dlatego chętniej wtedy przychodzą do lokalu,
# mimo że stojąc w pojedynczej kolejce muszą spędzić dodatkowe kilka sekund na dojściu z kolejki do wolnej kasy
#
# Właściciel lokalu zauważył, że nie zawsze opłaca expected_value się robić kilka kolejek, zamiast jednej,
# a to czy expected_value się to opłaca zależy od ilości otwartych kas


def one_queue(service_time, n):
    '''
    :param service_time (integer): time to service each client
    :param n (integer): number of cash desks
    :return float: number of clients serviced each minute in one cash desk
    '''
    # dla jednej aktywnej kolejki
    queue = FrontFIFOQueue()
    time_counter = 0
    #ilość klientów
    i = 0
    #maksymalna ilość klientów czekających na obsługę w lokalu naraz
    max_clients = 50
    # mierzymy dla 3600 sekund, tj godziny
    while time_counter < 3600:
        # jeśli wciąż jest miejsce dla czekających, wchodzą nowi klienci
        if queue.size() < max_clients:
            for j in range(0,max_clients - queue.size()):
                i = i + 1
                queue.enqueue(i)
        # czas obsługi pojedynczego klienta + 15 sekund na dojście do wolnej kasy
        # obsługa naraz w n kasach
        for j in range(0,n):
            queue.dequeue()
        time_counter += service_time + 10

    # właściciela interesuje ile klientów na minutę jest w stanie obsłużyć w pojedynczej otwartej kasie
    return (i/time_counter * 60) / n

def n_queues(service_time, n):
    '''
    :param service_time (integer): time to service each client
    :param n (integer): number of cash desks
    :return float: number of clients serviced each minute in one cash desk
    '''
    # dla n aktywnych kolejek naraz
    queues = [FrontFIFOQueue() for i in range(0, n)]
    time_counter = 0
    i = 0
    # mniejsza maksymalna liczba oczekujących klientów
    max_clients = 30
    def queues_sizes(qs):
        '''
        :param qs (list of FrontFIFOQueue):
        :return (list of integers): returns a list of size coresponding for each queue
        '''
        # dla wygody i zkrócenia zapisu
        return [queue.size() for queue in qs]
    # mierzymy dla godziny czasu
    while time_counter < 3600:
        # nowi klienci wchodzą, tylko jeśli suma wszystkich klientów w kolejkach jest mniejsza niż 30
        if sum(queues_sizes(queues)) < max_clients:
            for j in range(0, max_clients - sum(queues_sizes(queues))):
                i = i+1
                # każdy nowy klient wybiera najkrótszą kolejkę
                q_sizes = queues_sizes(queues)
                queues[q_sizes.index(min(q_sizes))].enqueue(i)

        # w czasie service_time obsługiwany jest jeden klient na kasę
        for queue in queues:
            queue.dequeue()
        time_counter += service_time

    return (i/time_counter * 60) / n


if __name__ == "__main__":
    # powiedzmy że obsługa jednego klienta zajmuje 90 sekund
    service_time = 90
    # będziemy badali  ilości kas od 1 do 10
    numbers_of_desks = range(1,11)
    oneQ = [one_queue(service_time, n) for n in numbers_of_desks]
    nQ = [n_queues(service_time, n) for n in numbers_of_desks]


    plt.plot(numbers_of_desks, oneQ, numbers_of_desks, nQ)
    plt.ylabel("clients per minute per cash desk")
    plt.xlabel("number of cash desks")
    plt.xticks(numbers_of_desks)
    plt.legend(["one big queue", "one queue for each desk"])
    plt.show()

    # jak widać:
    # dla obecnych wejściowych bardziej opłaca się stworzyć wspólną kolejkę, jeśli ilośc otwartych kas nie przekracza 5