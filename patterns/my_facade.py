# a facade brings together disperate (different) entities vis a single facade
# these classes should be in different modules
class Coder():
    def __init__(self) -> None:
        print('write some code')
    def __is_availabe(self): # mangled
        print('coding skills are avaiulable')
        return True
    def book_time(self):
        if self.__is_availabe():
            print('coder has been booked')
class Tester():
    def __init__(self) -> None:
        print('preparing some tests')
    def testing(self):
        print('tests are in place')

class Techinician():
    def __init__(self) -> None:
        print('designing things')
    def do_stuff(self):
        print('doping stuff')


class Artisan():
    def __init__(self) -> None:
        print('designing things')
    def make_prototypes(self):
        print('prepared design')


class Manager():
    '''This is the facade to other classes'''
    def __init__(self) -> None:
        print('Manager say that he will manage teams')

    def arange(self):
        self.coder = Coder()
        self.tester = Tester()
        self.technician = Techinician()
        self.artsan = Artisan()
    # put assets to work

        self.coder.book_time()
        self.tester.testing()
        self.technician.do_stuff()
        self.artsan.make_prototypes()

class client():
    def __init__(self) -> None:
        print ('we need a team')

    def askManager(self):
        self.manager = Manager()
        self.manager.arange()

    def __del__(self):
        print ('done')

if __name__ == '__main__':
    '''a facade can make ugle stuff easier'''
    clients = client()
    clients.askManager()
