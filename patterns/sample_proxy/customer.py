# from debit_card import debitCard

# class Customer():
#     def __init__(self) -> None:
#         print('lets buy')
#         self.debitCard = debitCard()
#         self.isPurchased = False

#     def makePayment(self):
#         self.isPurchased = self.debitCard.doPay()

#     def __del__(self):
#         if self.isPurchased:
#             print('bought')
#         else:
#             pass
# if __name__ == '__main__':
#     pass



from debit_card import DebitCard

class Customer():
    def __init__(self):
        print('lets buy some stuff')
        self.debitCard = DebitCard()
        self.isPurchased = None
    def makePayment(self):
        self.isPurchased = self.debitCard.doPay()
    def __del__(self):
        if self.isPurchased: # this will be True or False
            print('We bought something')
        else:
            print('Awww not enough dosh')


if __name__ == '__main__':
    pass
