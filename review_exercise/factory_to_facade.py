class Dog():
    def __init__(self):
        print('This is a dog')
    def sound(self):
        print('woof')
class Cat():
    def __init__(self):
        print('This is a Cat')
    def sound(self):
        print('meow')
class Lion():
    def __init__(self):
        print('This is a lion')
    def sound(self):
        print('roar')
class Bat():
    def __init__(self):
        print('This is a bat')
    def sound(self):
        print('_____')

# here is a zoo
class zoo():
    '''This is a facade to all the animals'''
    def __init__(self):
        print('You can see various animals here')
    def showme(self):
        '''The facade will provide instances of all the other subsystems/microservices etc.'''
        self.dog      = Dog()
        self.cat     = Cat()
        self.lion = Lion()
        self.bat     = Bat()
        # we could easily add additional assets here
        # put the assets to work
        self.dog.sound() # if not available we should handle ...
        self.cat.sound()
        self.lion.sound()
        self.bat.sound()

class Visitor():
    '''Client needs resources to solve a problem'''
    def __init__(self):
        print('I am a visitor to zoo')
    def visitzoo(self):
        print('lets check animals')
        self.zoo = zoo() # we now have access to our facade
        self.zoo.showme()
    def __del__(self): # every class will run __del__ whn done
        print('All done')


if __name__ == '__main__':
    '''a facade can make ugly stuff easier to look at'''
    customer = Visitor()
    customer.visitzoo()
