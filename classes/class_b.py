from classes.class_a import Point


class Point3(Point):
    '''a point in 3-d'''

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z # call setter

    @property
    def z(self):
        return self.__z

    @x.setter
    def z(self,z):
        if type(x) in (int, float):
            self.__z = z
        else:
            raise TypeError

if __name__ == '__main__':
    pass
