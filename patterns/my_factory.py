class Animal():
    '''All our ceartures from here'''
    def make_a_noise(self):
        pass
# here are some concrete creatures

class Dog(Animal):
    def make_a_noise(self):
        return 'woof'
class Cat(Animal):
    def make_a_noise(self):
        return 'meow'
class Lion(Animal):
    def make_a_noise(self):
        return 'roar'
class Bat(Animal):
    def make_a_noise(self):
        return '___'

# here is a creature factory

class CreatureFactory():
    def make_sound(self, obj):
        return eval(obj)().make_a_noise()
    # added the factory code
