from strategy import Strategy

class Chase_Strategy(Strategy):

    def run(self):
        print(self.ticker * 5)
        return 0
