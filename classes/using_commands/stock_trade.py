class StockTrade: # implicit inherit from object
    def buy(self):
        print('buy stocks')
    def sell(self):
        print('sell stock')

if __name__ == '__manin__':
    s = StockTrade()
    s.buy()
    s.sell()
