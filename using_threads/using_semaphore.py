# semphoses let us specify the maximum number of concurrent threads that can access a resources

from collections.abc import Callable, Iterable, Mapping
import random
import threading
import time
from typing import Any

#a global asset
ticketsAvailable = 100

class TicketSeller(threading.Thread):
    ticketsSold = 0

    def __init__(self, sem) -> None:
        threading.Thread.__init__(self)
        self._sem = sem
    def run(self):
        global ticketsAvailable
        running = True
        while running:
            self._sem.acquire()
            self.randomDelay()
            if ticketsAvailable <= 0:
                running = False
            else:
                self.ticketsSold +=1
                ticketsAvailable -=1
            self._sem.release()
    def randomDelay(self):
        time.sleep(random.randint(0,4)/16)

def main():
    sem = threading.Semaphore(4)
    sellers = []

    for i in range(0,4):
        seller = TicketSeller(sem)
        sellers.append(seller)
        seller.start()
    for s in sellers:
        s.join()

if __name__ == '__main__':
    main()
