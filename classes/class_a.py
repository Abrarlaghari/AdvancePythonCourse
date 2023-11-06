class Point():
    ''' A point in 2-d space'''
    __slots__ = ('__x','__y')
    def __init__(self, x, y):
        self.x =  x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        if type(x) in (int, float):
            self.__x = x
        else:
            raise TypeError

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        if type(y) in (int, float):
            self.__y = y   # name mangling ()
        else:
            raise TypeError
    def __str__(self):
        return f'The point is a x: {self.x} and y {self.y}'


if __name__ == '__main__':
    p1 = Point(2,7)
    print(p1)
