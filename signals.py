from binance.client import Client
import pandas as pd

def get_pair_candles_df(client,gmt_usdt_symbol,candle_timing="5m",interval= "1 day ago UTC"):
    klines = client.get_historical_klines(gmt_usdt_symbol, candle_timing,interval)
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
    return klines_df

