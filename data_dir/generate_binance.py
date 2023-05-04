import json 
import requests
import datetime 
from tqdm import tqdm
import pandas as pd 
key = "https://api.binance.com/api/v3/ticker/price?symbol="
curr_list = ['BTCUSDT','ETHUSDT']
symb_list = [] 
price_list = [] 
time = []
#while True: 
#    for i in curr_list: 
#        data = (requests.get(key+i)).json() 
#        print(datetime.datetime.now(),data) 
for j in tqdm(range(500)): 
    for i in curr_list: 
        data = (requests.get(key+i)).json() 
        symb_list.append(data['symbol']) 
        price_list.append(data['price'])
        time.append(datetime.datetime.now()) 
df = pd.DataFrame({
    'time':time, 
    'Currency':symb_list, 
    'Price':price_list
})
df['time'] = pd.to_datetime(df['time']) 
df = df.set_index('time') 
print(df.head()) 
df.to_csv("data_dir/binance.csv")
        
        
