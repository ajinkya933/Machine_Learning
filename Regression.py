import pandas as pd
import quandl

# get google stock data from quandl.com and display them
df=quandl.get('WIKI/GOOGL')
print("****************************** RAW DATA FROM QUANDL.COM *******************************")

print(df.head())

print("****************************** PROCESSED DATA *******************************")

df=df[["Adj. Open", 'Adj. High','Adj. Low','Adj. Close', "Adj. Volume",]]

# HL_PCT is high minus the low percent in stock
df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Close'] *100.0
# PCT_change is the percentage change (new-old/old)
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] *100.0
# I look the data which is useful
df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())

