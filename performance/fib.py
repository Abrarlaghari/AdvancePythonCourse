# The Fibonacci sequence is a interesting mathematical idea
# always aim for the performant code
# python also include cProfile
# python -m cProfile -o prof_out fib.py
# this will generate a report which will be then use by python to read it
import timeit
from memory_profiler import profile


def fib(n):
    '''LOw performance code'''
    if n<=1:
        return 1
    else:
        # recursion
        return (fib(n-1) + fib(n-2))

# @profile
def main():
    n = 32
    fib_values = []
    start = timeit.default_timer()
    for _ in range(2, n+1):
        r = fib(_)
        fib_values.append(r)
    end = timeit.default_timer()
    print(f'process took {end-start} seconds ')


if __name__ == '__main__':
    main()
