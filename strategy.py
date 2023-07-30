import pandas as pd

class Strategy:
    def __init__(self, ticker, csv_path):
        self.ticker = ticker
        self.csv_path = csv_path #path to csv for ticker
        self.df = pd.read_csv(csv_path) #creating pandas dataframe from ticker csv

    def __str__(self):
        return("Strategy on "+self.ticker) 

    def run(self):
        #Top level strategy function. manager.py calls this function to start a new strategy thread.
        print(self.csv_path, len(self.df.index), "entries")

        return 0.0 #Return percent return, I think that would be best?

