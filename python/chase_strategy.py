from strategy import Strategy
import pandas as pd
import datetime

class Chase_Strategy(Strategy):

    def __str__(self):
        return("Chase_Strategy on "+self.ticker)

    def run(self):
        self.acwx = pd.read_csv(self.csv_path+"ACWX.csv")
        self.bonds = pd.read_csv(self.csv_path+"Bonds.csv")
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.acwx['Date'] = pd.to_datetime(self.acwx['Date'])
        self.bonds['Date'] = pd.to_datetime(self.bonds['Date'])

        return 0.0
    
    #Finding the date to start the lookback
    def find_start_date(self):
        #Finding the security that starts the latest
        latest = max(self.bonds["Date"][0], self.acwx["Date"][0], self.df["Date"][0])

        #Finding the nearest start of the month to the latest start
        while True:
            if latest not in self.df['Date'].tolist():
                latest + datetime.timedelta(days=1)
            elif latest.day == 1:
                break
            elif latest.day == 2:
                break
            elif latest.day == 3:
                break
            elif latest.day == 4:
                break
            else:
                continue

        #Adding a year to start look back, then checking to see if valid 
        test_start_date = latest + datetime.timedelta(years=1)
        
        while test_start_date not in self.df['Date'].tolist():
            test_start_date + datetime.timedelta(days=1)

        return test_start_date
    
    def annual_return_pct(self, end_date, dataframe):
        test_lookback_date = end_date - datetime.timedelta(years=1)

        while test_lookback_date not in self.df['Date'].tolist():
            test_lookback_date + datetime.timedelta(days=1)

        end_price = self.price_from_date(end_date, dataframe)
        lookback_price = self.price_from_date(test_lookback_date, dataframe)
 
        ar_pct = (end_price - lookback_price)/lookback_price

        return ar_pct
        
    def compare_returns():
        #uses annual_return_pct
        #returns ETF to purchase that month
        pass


    def month_forward():
        pass

    def price_from_date(self, date, dataframe):
        i = dataframe.index[dataframe["Date"] == date].tolist()
        return dataframe[i]["Close"]
    
    '''FUTURE USE
        Function takes test_start date
        runs compare_returns
        
        Does SOMETHING with that - pass to brokerage class, makes trades itself :(
        
        jumps a month forward
        runs compare_returns...

        so on and so forth


        '''
