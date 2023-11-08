# The Fibonacci sequence is a interesting mathematical idea
# always aim for the performant code
# python also include cProfile
# python -m cProfile -o prof_out fib.py
# this will generate a report which will be then use by python to read it
import timeit
from memory_profiler import profile


cache = {0: 0, 1: 1}

def fib(n):
    '''LOw performance code'''
    if n<=1:
        return 1
    else:
        # recursion
        return (fib(n-1) + fib(n-2))

def fib_mem(n):
    if n in cache:
        return cache[n]
    cache[n] = fib_mem(n - 1) + fib_mem(n - 2)
    return cache[n]

def main():
    n = 34
    # fib_values = []
    # start = timeit.default_timer()
    # for _ in range(2, n+1):
    #     r = fib(_)
    #     fib_values.append(r)
    # end = timeit.default_timer()
    # print(f'Raw implementation took {end-start} seconds ')


    # checking the memoization fibnacci
    fib_values = []
    start = timeit.default_timer()
    for _ in range(2, n+1):
        r = fib_mem(_)
        fib_values.append(r)
    end = timeit.default_timer()
    print(f'Memoization implementation took {end-start} seconds ')
    print(fib_values)

if __name__ == '__main__':
    main()
