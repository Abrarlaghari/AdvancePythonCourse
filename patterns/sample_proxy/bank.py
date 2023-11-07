from payment import Payment
import random

class Bank(Payment):
    def __init__(self) -> None:
        self.card = None
        self.account = None

    def setCard(self, card):
        self.card = card

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds():
        print(f'bank is checking if {self.__getAccount()} has founds')
        return bool(random.getrandbits(1))

    def doPay(self):
        if self.__hasFunds():
            print('bank is paying')
            return True
        else:
            print('insufficient fund')
            return False


if __name__ == '__main__':
    pass
