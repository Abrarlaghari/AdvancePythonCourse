# using rlock

import threading
import time

class MyWorker():

    def __init__(self) -> None:
        self.a = 1
        self.b =2
        self.rlock = threading.RLock()

    def modifyA(self):
        with self.rlock:
            print(f'Rlock is acquired {self.rlock._is_owned()} to modify A')
            self.a += 1
            time.sleep(1)
    def modifyB(self):
        with self.rlock:
            print(f'Rlock is acquired {self.rlock._is_owned()} to modify B')
            self.b -= 1
            time.sleep(1)
    def modifyBoth(self):
        self.modifyA()
        self.modifyB()

def main():
    w =MyWorker()
    w.modifyA()
    w.modifyB()
    w.modifyBoth()

if __name__ == '__main__':
    main()
