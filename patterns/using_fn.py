# functional programming uses functions rather than classes

def isEven(n):
    '''True if even else false'''
    return n%2 == 0

def addThem(m,n):
    return m+n

def main():
    '''Python has map and filter and functional features'''
    # map objects do not maintain all the values in memory. they yield results on demand
    results = map(isEven, range(-10,11))
    print(results) # its a map object and we can iterate

    print(results.__next__())
    print(results.__next__())
    print(results.__next__())

    for _ in results:
        print(f'Even: {_}')


    # filter
    matching = filter(isEven, range(-10,11))
    print(matching)

if __name__ == '__main__':
    main()
