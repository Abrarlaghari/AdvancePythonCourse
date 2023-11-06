class Agent():

    def __init__(self) -> None:
        self.__order_queue = []

    def place_order(self, order):
        self.__order_queue = order
        order.executer()

if __name__ == '__main__':
    pass
