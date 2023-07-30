#!/usr/bin/python

import yfinance as yf
import sys

stocks = sys.argv[1:]

for stock_name in stocks:

    speriod = "3650d"
    sinterval = "1d"

    stock = yf.Ticker(stock_name)

    hist = stock.history(period=speriod, interval=sinterval)

    listized = hist["Close"].values.tolist()

    print("Number of points:", len(listized))

    #with open("./csvs/"+stock_name+"-"+speriod+"-"+sinterval+".csv", "w") as f:
    with open("./csvs/"+stock_name+".csv", "w") as f:
        for entry in listized:
            f.write(str(entry)+"\n")


