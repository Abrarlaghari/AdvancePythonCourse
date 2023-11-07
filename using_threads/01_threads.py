from threading import Thread
import random
import time

def myFn(n):
    for _ in range(0,10):
        print(f'{n} is sleeping')
        time.sleep(random.random()*0.1) #sleep up to 0.1 secs

def main():
    start = time.time()
    # myFn(1)
    # myFn(2)
    # myFn(3)
    # myFn(4)
    # myFn(5)

    t1 = Thread(target=myFn, args=(1,))
    t2 = Thread(target=myFn, args=(2,))
    t3 = Thread(target=myFn, args=(3,))
    t4 = Thread(target=myFn, args=(4,))
    t5 = Thread(target=myFn, args=(5,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    end = time.time()
    print(f'total time {end-start}')

if __name__ == '__main__':
    main()
