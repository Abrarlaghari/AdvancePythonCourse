from abc import ABCMeta, abstractclassmethod

class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def dopay(self):
        pass #never implement in the abstract
