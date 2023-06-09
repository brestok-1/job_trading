from typing import NamedTuple

import numpy
import numpy as np
import pandas as pd
from binance import Client
from statsmodels.regression.linear_model import RegressionResults
import statsmodels.api as sm

from data import get_klines, DATA_ETH, DATA_BTC


class Data(NamedTuple):
    data_eth: pd.DataFrame
    data_btc: pd.DataFrame


def get_own_movements(btc_impact: int):
    """This function returns the Etherium exchange rate without the influence of Bitcoin"""
    last_price = _get_last_price()
    eth_own_price = last_price.data_eth['Close'].values - btc_impact * last_price.data_btc['Close'].values
    return eth_own_price


def _get_last_price() -> Data:
    eth_last_price = get_klines('ETHUSDT', Client.KLINE_INTERVAL_1MINUTE, 60)
    btc_last_price = get_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, 60)
    return Data(eth_last_price, btc_last_price)


def get_btc_ratio(data: Data) -> int:
    """This function returns the coefficient of influence of Bitcoin on the Etherium"""
    linear_model = _get_regression_linear_model(data)
    btc_impact = linear_model.params[1]
    return btc_impact


def _get_regression_linear_model(data) -> RegressionResults:
    eth = data.data_eth['Close'].values
    btc = _reshape_data_btc(data)
    linear_model = sm.OLS(eth, sm.add_constant(btc)).fit()
    return linear_model


def _reshape_data_btc(data: Data) -> numpy.ndarray:
    data_btc = np.hstack(
        [data.data_btc['Close'].values.reshape(-1, 1), data.data_eth[['Open', 'High', 'Low', 'Volume']].to_numpy()])
    return data_btc


def print_eth_changes(eth_own_movements: list) -> None:
    """The function prints the result of the change
     in the Etherium exchange rate without the influence of Bitcoin
     if the change was more than 1%"""
    changes = _get_changes_in_percent(eth_own_movements)
    if changes > 1:
        print(f'During the last hour, the change was {changes:.2f}%')


def _get_changes_in_percent(eth_own_movements: list) -> int:
    min_eth = min(eth_own_movements)
    max_eth = max(eth_own_movements)
    changes_in_percent = (max_eth - min_eth) / min_eth * 100
    return changes_in_percent


BTC_IMPACT = get_btc_ratio(Data(DATA_ETH, DATA_BTC))
