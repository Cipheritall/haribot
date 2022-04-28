###
# BandMaster
###

from binance.client import Client
import pandas as pd
from time import sleep

from config import *
from signals import *
from logging_config import *

# Setup
logging = init_logging()
api_key, api_secret = get_binance_keys()
setup_config = get_setup_config()
pairs = setup_config['basic_setup']['pairs']
client = Client(api_key, api_secret)

gmt_usdt_symbol=f'{pairs[0]}{pairs[1]}'


klines_df = get_pair_candles_df(client,gmt_usdt_symbol)
logging.info(f"\n{klines_df.head(90)}")

