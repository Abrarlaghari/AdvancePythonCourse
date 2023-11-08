# for thread safe


from threading import Lock

lock = Lock()

def lock_a_method(meth):
    '''apply lock to any method'''
    def locked_method(self, *args, **kwargs):
        try:
            # lock.acquire()
            # result = meth(self, args, kwargs)
            # lock.release()
            # return result
            with lock:
                return meth(self, *args, **kwargs)
        except Exception as e:
            print(e)
    lock_a_method.__name__ = f'Locked_method{meth.__name__}'
    locked_method.__is_locked = True # a marker to indicate method is locked
    return locked_method


def make_thread_safe(cls, meth_l, lock):
    '''We can provide a list of methods of a class to be locked'''
    init = cls.__init__ # copy of original init
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock # from lock factory
    cls.__init__ = new_init
    # iterate over method_l and lock each method

    for meth in meth_l:
        old_meth = getattr (cls, meth)
        new_meth = lock_a_method(old_meth)
        setattr (cls, meth, new_meth)
    return cls

# to use as a decorator for a class
def lock_a_class(meth_list, lock):
    return lambda cls: make_thread_safe (cls, meth_list, lock)

@lock_a_class(['add', 'remove'], Lock)
class MySet(set):
    '''inherits from set.
     need to make the methods thread safe using decorator funuction'''
    def __init__(self, new_set):
        set.__init__(self, new_set)
    @lock_a_method # apply the decorator to make it thread safe
    def someMethods(self, new_value):
        if type(new_value) == int:
            self.add(new_value)
        else:
            pass





def main():
    ms = MySet({3,2,6,6,6,6, True, 'this is my set', True})
    print(ms.someMethods.__is_locked) # True



if __name__ == '__main__':
    main()
