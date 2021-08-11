import unittest
from BinaryHeap import BinaryHeap
import random
from time import time
from matplotlib import pyplot

class MyTestCase(unittest.TestCase):
    def test_something(self):
        i_table = [1000*i for i in list(range(10,110,10))]
        times = []
        for i in i_table:
            timer = time()
            random_list = [random.randint(0,100) for x in range(0,i)]
            heap = BinaryHeap(random_list)
            heap_list = heap.sort()
            self.assertEqual(heap_list, sorted(random_list))
            times.append(time()-timer)
        pyplot.plot(i_table, times)
        pyplot.show()


if __name__ == '__main__':
    unittest.main()
