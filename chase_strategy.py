from strategy import Strategy

class Chase_Strategy(Strategy):

    def __str__(self):
        return("Chase_Strategy on "+self.ticker)

    def run(self):
        return 0.0
