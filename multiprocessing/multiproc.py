import os
import multiprocessing

def whichProc():
    '''declare which process ID this is running on'''
    print(f'Running on process ID {os.getpid()}')


if __name__ == '__main__':

    print(f'This device has {os.cpu_count()} processors')
    procs_l = []
    # sensible about number of the processors
    for n in range(0,os.cpu_count()-1):
        p = multiprocessing.Process(target=whichProc)
        procs_l.append(p)
        p.start()
    # counting on main process
    whichProc()
