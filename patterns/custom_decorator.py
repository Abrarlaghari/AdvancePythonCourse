# decorate something

def showArgs(f):
    def newFunc(*args, **kwargs):
        print( f'Running a function called {f.__name__}' ) # 'dunder' means double underscore
        print( f'The positional arguments are {args}' )
        print( f'The keyword arguments are {kwargs}' )
        return f(*args, **kwargs) # call the original function
    return newFunc

@showArgs
def isOdd(n):
    '''return True if odd else false'''
    return n%2 != 0


def squares(m,n):
    s = []
    for i in range(m,n):
        s.append(i*i)
        return s


if __name__ == '__main__':
    for i in range(0, 55):
        print(isOdd(i), end=', ')
