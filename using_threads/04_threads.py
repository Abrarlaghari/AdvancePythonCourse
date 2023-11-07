import threading

# a global asset for a file
counter = 0
lock = threading.Lock()

def workerA():
    '''This worker increment counter'''
    global counter
    lock.acquire()

    try:
        while counter < 20:
            counter +=1
            print (f'worker A increment counter to {counter}')

    except Exception as e:
        print(f'something went wrong {e}')
    finally:
        lock.realease()

def workerB():
    '''This worker increment counter'''
    global counter
    lock.acquire()

    try:
        while counter > -20:
            counter -=1
            print (f'worker B increment counter to {counter}')

    except Exception as e:
        print(f'something went wrong {e}')
    finally:
        lock.realease()

def main():
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t1.start()
    t2.start()
    t1.join()
    t2.join()




if __name__ == '__main__':
    pass
