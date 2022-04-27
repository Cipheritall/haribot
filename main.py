###
# BandMaster
###

from binance.client import Client
import pandas as pd
from time import sleep

from config import *

# Setup
api_key, api_secret = get_binance_keys()
setup_config = get_setup_config()
pairs = setup_config['basic_setup']['pairs']
client = Client(api_key, api_secret)
gmt_usdt_symbol=f'{pairs[0]}{pairs[1]}'

klines = client.get_historical_klines(gmt_usdt_symbol, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# Adapting data
columns_values = [
          "Date",
          "Open",
          "High",
          "Low",
          "Close",
          "Volume",
          "Close time",
          "Quote asset volume",
          "Number of trades",
          "Taker buy base asset volume",
          "Taker buy quote asset volume",
          "Ignore"
]

klines_df = pd.DataFrame(klines, columns =columns_values)
print(klines_df.head(30))