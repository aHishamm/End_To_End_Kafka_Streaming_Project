import datetime as dt
import yfinance as yf 
#fetching previous stock data for Apple
stock_data = yf.download('AAPL',dt.datetime(2001,1,1),dt.datetime(2023,1,1)) 
#saving the time series stock data information to a csv file to be fed to Kafka 
stock_data.to_csv("data_dir/stocks.csv",index=True)