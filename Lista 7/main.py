from graph import Graph
from shortest_path import ShortestPath
from rivercrossing import RiverCrossing
from canisters import TwoLitresGame


# Przykładowe wywołania

if __name__ == '__main__':

    # zadanie 1:
    # tworzymy graf
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addVertex(7)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    g.addEdge(7,2)

    # zadanie 2:
    # poniższa metoda wygeneruje plik .dot o podanej nazwie dla podanego grafu
    g.generateDot("graf")

    # zadanie 3:
    # poniższe algoytmy wyszukają wirzchołka o danym kluczu w grafie, pokolei dla każdego 'białego',
    # czyli nieodwiedzonego wcześniej wierzchołka
    print("zadanie 3:")
    print(g.depth_first_search(0))
    print(g.breadth_first_search(6))

    # zadanie 4
    # sortowanie topologiczne zwraca tablicę, w której żaden element nie może wystąpic przed swoim rodzicem
    print("\nzadanie 4:")
    f = Graph()
    for i in range(0,4):
        f.addVertex(i)
    f.addEdge(0,3)
    f.addEdge(1,3)
    f.addEdge(2,1)
    print(f.topological_sort())

    # zadanie 5
    # zwraca słownik zawierający klucz : najkrótsza droga od podanego startu
    print("\nzadanie 5:")
    print(g.shortest_path(0))

    # zadanie 6
    # zwraca wykonane kroki dla zagadki o misjonarzach i kanibalach
    print("\nzadanie 6:")
    game = RiverCrossing()
    print(game.result)

    # zadanie 7
    # rozwiązuje zagadkę dla kanistrów o podanych pojemnościach i żądanej pojemności
    # zwraca wykonane kroki
    # jesli nie znajdzie rozwiązania zwraca None
    print("\nzadanie 7:")
    canisters_game = TwoLitresGame(first=3,second=4,goal=2)
    print(canisters_game.solve())
