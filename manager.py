
from multiprocessing import Pool
from strategy import Strategy

#import strategies:
from chase_strategy import Chase_Strategy


def run_strategy(ticker_and_strat):
    curr_ticker, curr_strat = ticker_and_strat
    strategy = curr_strat(curr_ticker, "csvs/"+curr_ticker+".csv")
    return strategy.run()

def run_strategies(ticker_and_strats):
    with Pool() as p:
        results = p.map(run_strategy, ticker_and_strats)
        print("Percent returns:", results)

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "SPY", "TSLA", "ROKU", "INTC", "AMZN"]
    strategies = [Strategy, Chase_Strategy]

    ticker_and_strats = []

    for ticker in tickers:
        for strategy in strategies:
            ticker_and_strats.append((ticker, strategy))
    

    print(ticker_and_strats)

    run_strategies(ticker_and_strats)



