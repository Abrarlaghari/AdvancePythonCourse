from threading import Thread
import random
import time

class MyClass(Thread):
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n
    def run(self):
        for _ in range(0,10):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*.1)
def main():
    thread_l = []
    for _ in range(15):
        thread_l.append(MyClass(_))
    for thread in thread_l:
        thread.start()
    for thread in thread_l:
        thread.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'total time taken {end-start} seconds')
