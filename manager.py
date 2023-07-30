
from multiprocessing import Pool
from strategy import Strategy

#import strategies:
from chase_strategy import Chase_Strategy


def run_strategy(ticker):
    strategy = Strategy(ticker, "csvs/"+ticker+".csv")
    return strategy.run()


def run_strategies(tickers):
    with Pool() as p:
        print(p.map(run_strategy, tickers))


if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "SPY", "TSLA", "ROKU", "INTC", "AMZN"]

    run_strategies(tickers)
