from memory_profiler import profile

import collections # a bunch of additional data structures

@profile # invoke memory profile
def myFn():
    my_deq = collections.deque('6565645')

    # print(my_deq)
    for i in range(0,1024):
        my_deq.append(i)
        my_deq.appendleft(i)
    return my_deq

if __name__ == '__main__':

    # de = collections.deque('tenet')
    # de.append('s')
    # de.appendleft('s')
    # print(type(de), de)
    # de.pop()
    # de.popleft()
    r = myFn()
    # print(r)
