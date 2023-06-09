import pandas as pd
from binance.client import Client
import os
from dotenv import load_dotenv
from typing import Literal

load_dotenv()
binance_api_key = os.getenv("BINANCE_API_KEY")
binance_secret_key = os.getenv("BINANCE_SECRET_KEY")

client = Client(binance_api_key, binance_secret_key)


def get_klines(symbol: Literal['ETHUSDT'] | Literal['BTCUSDT'], interval: str, quantity: int) -> pd.DataFrame:
    klines = _get_klines_output(symbol, interval, quantity)
    df = _refactor_to_df(klines)
    return df


def _get_klines_output(symbol: Literal['ETHUSDT'] | Literal['BTCUSDT'], interval: str, quantity: int) -> list:
    klines = client.futures_klines(symbol=symbol, interval=interval, limit=quantity)
    return klines


def _refactor_to_df(klines: list) -> pd.DataFrame:
    df = pd.DataFrame(klines, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
                                       'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                                       'Taker buy quote asset volume', 'Ignore'])
    return _configure_df(df)


def _configure_df(df: pd.DataFrame) -> pd.DataFrame:
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')
    df = df.set_index('Close time')
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df = df.astype('float')
    return df


DATA_ETH = get_klines('ETHUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)
DATA_BTC = get_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)