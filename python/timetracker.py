import datetime
import pandas as pd

class TimeTracker:
    def __init__(self, trading_ticker, other_tickers):
        #pass timetracker pandas. trading_tracker is one panda, other_tickers is a list of pandas.
        self.trading_ticker = trading_ticker
        self.other_tickers = other_tickers

    def find_start_date(self):
        #Finding the security that starts the latest                                                                   
        latest = max([self.trading_ticker] + self.other_tickers) #Seeing if our main ticker is most recent, or one of the other tickers
                                                           
        #Finding the nearest start of the month to the latest start
        while True:       
            if latest not in self.trading_ticker['Date'].tolist():
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



