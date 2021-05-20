#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas_datareader


# In[2]:


pip install yfinance


# In[3]:


pip install Yahoo-ticker-downloader


# In[4]:


import pandas as pd
import yfinance as yf


# In[ ]:





# In[5]:


amd.history(period="max")


# In[ ]:


tsla_df = yf.download('TSLA', 
                      start='2019-01-01', 
                      end='2019-12-31', 
                      progress=False)
tsla_df.head()


# In[ ]:


import pandas as pd
import yfinance as yf
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pylab', 'inline')

stocks = []
stockPrices=[]
stockDividends=[]
def addStock(stock):
    stocks.append(stock)
    
def getDividend():
    for stock in stocks:
        newStock = yf.Ticker(stock)
        stockDividends.append(newStock.dividends)
        
def getPrice():
    for stock in stocks:
        newStock = yf.Ticker(stock)
        stockPrices.append(newStock.history(period='1y'))
    
def viewPortfolio():
    data = {'Ticker':stocks, 
        'Price': stockPrices, 
        'Dividend Yield':stockDividends,
           'Year High': stocks,
           'Year Low': stocks} 
    df = pd.DataFrame(data) 
    print(df)
  #  portfolio = pd.Series()
   # print(portfolio)



print("~~~~~~~Robo Stock Advisor~~~~~~~")
print("|AT: Analyze Ticker     |")
print("|A: Add stock to portfolio      |")
print("|V: View Portfolio              |")
print("|AI: Add Indicators             |")
print("|VT: View Ticker                |")
print("|Q: Quit                        |")
print()
inp = input("To begin, make a selection: ")

while inp != "Q":
    
    if inp =="AT":
        tickerPick = input("Enter a ticker: ")
        date = input("Enter a date (MUST BE IN YYYY/MM/DD format!)")
        tick = pdr.get_data_yahoo(tickerPick,date)
        print(tick.head())
        
        tickDf = pd.DataFrame(tick.Close)
        tickDf['9dayMA']=tickDf.Close.rolling(9,min_periods=1).mean().shift()
        tickDf['21dayMA']=tickDf.Close.rolling(21,min_periods=1).mean()
        plt.figure(figsize=(15,10))
        plt.grid(True)
        plt.plot(tickDf['Close'],label= tickerPick)
        plt.plot(tickDf['9dayMA'],label= '9 day moving average')
        plt.plot(tickDf['21dayMA'],label= '21 day moving average')
        plt.legend(loc=2)
        
        plt.show()
        
        #compute change
        tickDf['Change'] = np.log(tickDf['Close']/tickDf['Close'].shift())
        plt.plot(tickDf.Change)
        plt.show()
        
        #Compiute volaility average
        tickDf['Volatility']=tickDf.Change.rolling(21,min_periods=1).std().shift()
        plt.plot(tickDf.Volatility)
        plt.show()
        
        #Price Analysis
        tickDf['Actual_Change'] = tickDf['Close']-tickDf['Close'].shift(1)
        
        tickDf['Expected_Change']=tickDf['Close'] * tickDf['Volatility']
        tickDf=tickDf.iloc[1:]
        print(tickDf.head())
        
    
    
    
    if inp == "VT" :
        tickInp = input("Enter a valid Ticker Symbol: ")
        tick = yf.Ticker(tickInp)
        print(tick.info)
        inp = input(" make a selection: ")

    if inp=="A":
        ask = True
        while ask:
            stockInput = input("Stock you would like to add to portfolio: ")
            addStock(stockInput)
            follow = input("Would you like to add another stock, Y/N? ")
            if follow =="Y":
                ask=True
                print(stocks)
            elif follow=="N":
                ask=False
                print(stocks)
        inp = input(" make a selection: ")
    if inp=="V":
        getDividend()
        getPrice()
        viewPortfolio()
        inp = input(" make a selection: ")
  
 
    
    
    if inp =="Q":
        raise SystemExit
    


# In[ ]:






# In[ ]:




