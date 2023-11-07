def showArgs(f):
    def newFunc(*args, **kwargs):
            # checking whether any of arg/kwargs is empty
        for i in args:
            if i == "":
                raise Exception("Sorry, one of the args is empty")
        for i in kwargs:
            if kwargs[i] == "":
                raise Exception("Sorry, one of the kwargs is empty")
        return f(*args, **kwargs)
    return newFunc

# here are two simple functions
@showArgs
def printstrings(n):
    print(n)


if __name__ == '__main__':
    stringgs = ['hello', 'hi', 'bye']
    for i in stringgs:
        printstrings(i)
