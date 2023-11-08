import multiprocessing
import os
import time


class MyProc(multiprocessing.Process):
    def __init__(self) -> None:
        super(MyProc, self).__init__()
    def run(self):
        '''overriding the sun method'''

        print(f'child process Id is {os.getpid} aka {multiprocessing.current_process().pid}')



def main():
    '''start a few processes'''
    proc_l =[]
    for p in range(0, os.cpu_count()-1):
        proc = MyProc()
        proc_l.append(proc)
        proc.start()
    for _ in proc_l:
        _.join()

if __name__ == '__main__':
    main()
