import os
import multiprocessing
import time
import timeit # a more accurate timer, it tires to ignore non-python stuff

def whichProc():
    '''declare which process ID this is running on'''
    print(f'Running on process ID {os.getpid()}')


if __name__ == '__main__':

    print(f'This device has {os.cpu_count()} processors')
    procs_l = []
    # sensible about number of the processors
    start_a = time.time()
    start_b = timeit.default_timer()
    for n in range(0,os.cpu_count()-1):
        p = multiprocessing.Process(target=whichProc)
        procs_l.append(p)
        p.start()
    for _ in procs_l:
        _.join()
    # counting on main process
    whichProc()
    time_a= (time.time())-start_a
    time_b = (timeit.default_timer())-start_b
    print(f'{time_a:0.3f} and {time_b:0.3f}')
