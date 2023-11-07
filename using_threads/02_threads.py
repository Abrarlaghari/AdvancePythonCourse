from threading import Thread
import random
import time
from typing import Any

class MyClass:
    '''overriding a __call__ makes this class callable by thread'''
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for _ in range(0,10):
            print(f'{n} is sleeping')
            time.sleep(random.random()*.1)
def main():
    c1 = MyClass()
    thread_l = []
    for i in range(8):
        thread_l.append(Thread(target = c1, args=(i,)))
    for thread in thread_l:
        thread.start()
    for thread in thread_l:
        thread.join()


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'total time {end-start} seconds')
