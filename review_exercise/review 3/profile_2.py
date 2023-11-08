# import timeit
# from memory_profiler import profile

cache = {0: 0, 1: 1}

def fib_mem(n):
    if n in cache:
        return cache[n]
    cache[n] = fib_mem(n - 1) + fib_mem(n - 2)
    return cache[n]

# @profile
def main():
    n = 34
    # checking the memoization fibnacci
    fib_values = []
    # start = timeit.default_timer()
    for _ in range(2, n+1):
        r = fib_mem(_)
        fib_values.append(r)
    # end = timeit.default_timer()
    # print(f'Memoization implementation took {end-start} seconds ')
    # print(fib_values)

if __name__ == '__main__':
    main()



##########################################################
#
#                   Mmemoery Profiling
#
#
###########################################################









####################### n=34 ########################

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     12     41.3 MiB     41.3 MiB           1   @profile
#     13                                         def main():
#     14     41.3 MiB      0.0 MiB           1       n = 34
#     15                                             # checking the memoization fibnacci
#     16     41.3 MiB      0.0 MiB           1       fib_values = []
#     17                                             # start = timeit.default_timer()
#     18     41.3 MiB      0.0 MiB          34       for _ in range(2, n+1):
#     19     41.3 MiB      0.0 MiB          33           r = fib_mem(_)
#     20     41.3 MiB      0.0 MiB          33           fib_values.append(r)
#     21                                             # end = timeit.default_timer()
#     22                                             # print(f'Memoization implementation took {end-start} seconds ')
#     23                                             # print(fib_values)



####################### n=1000 ########################


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     12     42.3 MiB     42.3 MiB           1   @profile
#     13                                         def main():
#     14     42.3 MiB      0.0 MiB           1       n = 1000
#     15                                             # checking the memoization fibnacci
#     16     42.3 MiB      0.0 MiB           1       fib_values = []
#     17                                             # start = timeit.default_timer()
#     18     42.4 MiB      0.0 MiB        1000       for _ in range(2, n+1):
#     19     42.4 MiB      0.2 MiB         999           r = fib_mem(_)
#     20     42.4 MiB      0.0 MiB         999           fib_values.append(r)
#     21                                             # end = timeit.default_timer()
#     22                                             # print(f'Memoization implementation took {end-start} seconds ')
#     23                                             # print(fib_values)







##########################################################
#
#                   cProfiling
#
#
###########################################################





####################### n=34 ########################



#          136 function calls (70 primitive calls) in 0.000 seconds

#    Random listing order was used

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     99/33    0.000    0.000    0.000    0.000 review_exercise/review 3/profile_2.py:6(fib_mem)
#         1    0.000    0.000    0.000    0.000 review_exercise/review 3/profile_2.py:13(main)
#         1    0.000    0.000    0.000    0.000 review_exercise/review 3/profile_2.py:4(<module>)
#        33    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}



####################### n=1000 ########################

#          4000 function calls (2002 primitive calls) in 0.001 seconds

#    Random listing order was used

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  2997/999    0.000    0.000    0.000    0.000 review_exercise/review 3/profile_2.py:6(fib_mem)
#         1    0.000    0.000    0.001    0.001 review_exercise/review 3/profile_2.py:13(main)
#         1    0.000    0.000    0.001    0.001 review_exercise/review 3/profile_2.py:4(<module>)
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
