#!/usr/bin/env python
# coding: utf-8

# # Reading  stock historical data directly from yahoo finance 

# Installation:pip install yahoo-finance 

# yfinance:Python module to get stock data from Yahoo! Finance

# A powerful financial data module used for pulling both fundamental and technical data from Yahoo Finance.
# ->As of Version 0.10, Yahoo Financials now returns historical pricing data for commodity futures, cryptocurrencies, ETFs, mutual funds, U.S. Treasuries, currencies, indexes, and stocks.

# Module Methods
# The financial data from all methods is returned as JSON.
# You can run multiple symbols at once using an inputted array or run an individual symbol using an inputted string.
# YahooFinancials works with Python 2.7, 3.3, 3.4, 3.5, 3.6, and 3.7 and runs on all operating systems. (Windows, Mac, Linux).

# # Importing Libraries 

# In[96]:


import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr


# Getting stock data from yahoo(fromstart data to end data).Here we are intiliazing start date as 01-01-2019 and end date as current date(31-08-2020).

# In[98]:


yf.pdr_override()
stock =input("Enter a stock ticker symbol ")##our input is QQQ 
print(stock)##printing the stock
startyear=2019
startmonth=1
startday=1
start=dt.datetime(startyear,startmonth,startday)##initializing the start as 01-01-2019  
now=dt.datetime.now()##initializing the now as end date 
df=pdr.get_data_yahoo(stock,start,now)##fetching the stock values from startdate to current date and store it into df.

print(df)


# In[108]:


len(df)   ##length of dataset is 421 rows and 6 columns


# In[109]:


df                  ##data frame 


# # Cleaning Process 

# Cleaning process is important step for every dataset in datascience life cycle and it is the first step in datascience life cycle.In this process first  we will find the missing values in the dataset and then fill the missing  values by using fillna function

# In[103]:


def clean_data(stock_data,col,start,now):
    weekdays=pd.date_range(start=start,end=now)
    clean_data=stock_data[col].reindex(weekdays)
    clean_data = clean_data.fillna(method='ffill')
    return clean_data
adj_closure=clean_data(df,'Adj Close',start,now)


# After cleaning the 'adj_closure' will be like this

# In[106]:


print(adj_closure)


# # Statistics of the 'adj_closure' in the dataset

# last=np.mean(adj_closure.tail(1))
# short_mean=np.mean(adj_closure.tail(1))
# long_mean=np.mean(adj_closure.tail(1))
# short_rolling=adj_closure.rolling(window=20).mean()
# long_rolling=adj_closure.rolling(window=200).mean()

# # visualization 

#   Date vs adj_closure 

# In[119]:


def create_plot(adj_closure):
    last=np.mean(adj_closure.tail(1))
    short_mean=np.mean(adj_closure.tail(1))
    long_mean=np.mean(adj_closure.tail(1))
    plt.subplots(figsize=(12,8))
    plt.plot(adj_closure)
    plt.xlabel('Date')
    plt.ylabel('Adj Close(p)')
    plt.legend('adj_closure')
    plt.title('Stock Price over Time')
    plt.show()

create_plot(adj_closure)


# In[120]:


def create_plot(adj_closure):
    short_rolling=adj_closure.rolling(window=20).mean()
    long_rolling=adj_closure.rolling(window=200).mean()
    plt.subplots(figsize=(12,8))
    plt.plot(adj_closure)
    plt.plot(short_rolling,label="20 day rolling mean")
    plt.plot(long_rolling,label="200 day rolling mean")
    plt.xlabel('Date')
    plt.ylabel('Adj Close(p)')
    plt.legend()
    plt.title('Stock Price over Time')
    plt.show()

create_plot(adj_closure)


# In[123]:


ma=50
smastring="Sma_"+str(ma)
###adding the sma string for comparision with Adj Close to analyze whether stock close is high or low.
df[smastring]=df.iloc[:,4].rolling(window=ma).mean()
df=df.iloc[ma:]


# In[124]:


for i in df.index:
    print(i)


# compare the  sma string with Adj Close to find out the statistics of the stock amd initialize the numh and numl as zero to track the information about the stock whether the close id high or low 

# In[125]:


numh=0
numl=0
for i in df.index:
    if (df["Adj Close"][i]>df[smastring][i]):
        print("The close is higher")
        numh+=1
    else:
        print("The close is low")
        numl+=1
print(numh,numl)
    


# In[126]:


print(str(numh))


# In[127]:


print(str(numl))


# Usage Examples(yahoo-finance ):
# The class constructor can take either a single ticker or a list of tickers as it’s parameter.
# This makes it easy to initiate multiple classes for different groupings of financial assets.
# Quarterly statement data returns the last 4 periods of data, while annual returns the last 3.

# In[ ]:





# In[ ]:




