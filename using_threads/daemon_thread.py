# a daemon thread will continue running until the main thread terminates

from threading import Thread
import time

def standardThrea():
    print('stating a standard thread')
    time.sleep(5)
    print('ending standard thread')

def daemonthread():
    print('starting daemion thread')
    while True:
        print('daemon thread')
        time.sleep(0.5)

if __name__ == '__main__':
    s = Thread(target=standardThrea)
    d = Thread(target=daemonthread, daemon=True)
    s.start()
    d.start()
    s.join()
    # no need for daemon to join it will terminate when main thread terminates
