# this is facade provides access to all other elements

from bank import Bank
from customer import Customer


def main():
    customer1 = Customer()
    customer1.makePayment()

if __name__ == '__main__':
    main()
