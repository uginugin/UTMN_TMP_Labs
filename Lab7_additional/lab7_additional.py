from random import randint
from algorithms import *
from time import process_time
import tracemalloc

def result(foo):
    def wrapper(arg):
        start_time = process_time()
        start_mem = tracemalloc.start()
        return_value = foo(arg)
        print("{0:15}|{1:30}|".format(foo.__name__, process_time()-start_time), end = '')
        mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print("{0:10} {1:10}|{2:10}|".format(mem[0], mem[1], mem[1]-mem[0]))
        return return_value
    return wrapper

if __name__=='__main__':
    a = [randint(-5000, 5000) for i in range(1000)]
    head = "{0:15}|{1:30}|{2:32}| ".format("Название", "Время, с", "Память (| Current, Peak | Used)")
    print(head)
    print("_"*(len(head)-1))
    func_list = [merge_sort, quick_sort, bubble_sort,  selection_sort]
    for i in func_list[::-1]:
        result(i)(a.copy())

    print("_"*(len(head)-1))

    input("Press enter to close the program...")

