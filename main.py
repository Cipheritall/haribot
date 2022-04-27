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


orderbook = client.get_order_book(symbol=f'{pairs[0]}{pairs[1]}')

print(orderbook)