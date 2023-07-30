from strategy import Strategy
import pandas as pd
import datetime

class Chase_Strategy(Strategy):

    def __str__(self):
        return("Chase_Strategy on "+self.ticker)

    def run(self):
        self.acwx = pd.read_csv(self.csv_path+"ACWX.csv")
        self.bonds = pd.read_csv(self.csv_path+"Bonds.csv")

        return 0.0
    
    def year_return(self, date_string, ticker):
        dt = datetime.datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S")
        


    def make_datetime(self, date_string):
        dt = datetime.datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S")
        return dt
