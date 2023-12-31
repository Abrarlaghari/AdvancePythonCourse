from orders import Order # access to our abstract base class
from stock_trade import StockTrade


class SellStock(Order):
    def __init__(self, stock) -> None:
        self.stock = stock
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        if type(new_stock) == StockTrade:
            self.__stock = new_stock

    def execute(self):
        return self.stock.sell()


if __name__ == '__main__':
    s = StockTrade()
    bs = SellStock(s)
    bs.execute()
