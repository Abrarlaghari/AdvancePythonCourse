# The Fibonacci sequence is a interesting mathematical idea
# always aim for the performant code
# python also include cProfile
# python -m cProfile -o prof_out fib.py
# this will generate a report which will be then use by python to read it
# import timeit
# from memory_profiler import profile

def fib(n):
    '''LOw performance code'''
    if n<=1:
        return 1
    else:
        # recursion
        return (fib(n-1) + fib(n-2))
# @profile
def main():
    n = 40
    fib_values = []
    # start = timeit.default_timer()
    for _ in range(2, n+1):
        r = fib(_)
        fib_values.append(r)
    # end = timeit.default_timer()
    # print(f'Raw implementation took {end-start} seconds ')

if __name__ == '__main__':
    main()






##########################################################
#
#                   Memory Profiling
#
#
###########################################################






####################### n=34 ########################

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     16     42.2 MiB     42.2 MiB           1   @profile
#     17                                         def main():
#     18     42.2 MiB      0.0 MiB           1       n = 34
#     19     42.2 MiB      0.0 MiB           1       fib_values = []
#     20                                             # start = timeit.default_timer()
#     21     42.2 MiB      0.0 MiB          34       for _ in range(2, n+1):
#     22     42.2 MiB      0.0 MiB          33           r = fib(_)
#     23     42.2 MiB      0.0 MiB          33           fib_values.append(r)
#     24                                             # end = timeit.default_timer()
#     25                                             # print(f'Raw implementation took {end-start} seconds ')


####################### n=40 ########################


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     16     41.6 MiB     41.6 MiB           1   @profile
#     17                                         def main():
#     18     41.6 MiB      0.0 MiB           1       n = 40
#     19     41.6 MiB      0.0 MiB           1       fib_values = []
#     20                                             # start = timeit.default_timer()
#     21     41.7 MiB      0.0 MiB          40       for _ in range(2, n+1):
#     22     41.7 MiB      0.0 MiB          39           r = fib(_)
#     23     41.7 MiB      0.0 MiB          39           fib_values.append(r)
#     24                                             # end = timeit.default_timer()
#     25                                             # print(f'Raw implementation took {end-start} seconds ')




##########################################################
#
#                   cProfiling
#
#
###########################################################



###################### n=34 ##############################


#          48315632 function calls (70 primitive calls) in 4.666 seconds

#    Random listing order was used

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 48315595/33    4.666    0.000    4.666    0.141 review_exercise/review 3/profile_1.py:9(fib)
#         1    0.000    0.000    4.666    4.666 review_exercise/review 3/profile_1.py:17(main)
#         1    0.000    0.000    4.666    4.666 review_exercise/review 3/profile_1.py:9(<module>)
#        33    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    4.666    4.666 {built-in method builtins.exec}




###################### n=40 ##############################



#          866988872 function calls (82 primitive calls) in 83.573 seconds

#    Random listing order was used

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 866988829/39   83.573    0.000   83.573    2.143 review_exercise/review 3/profile_1.py:9(fib)
#         1    0.000    0.000   83.573   83.573 review_exercise/review 3/profile_1.py:17(main)
#         1    0.000    0.000   83.573   83.573 review_exercise/review 3/profile_1.py:9(<module>)
#        39    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000   83.573   83.573 {built-in method builtins.exec}
