import numpy as np
import pandas as pd
from binance.client import Client
import statsmodels.api as sm
import time

from correlation import print_impact_analysis, Data
from data import get_klines


def main():
    data_ETHUSDT = get_klines('ETHUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)
    data_BTCUSDT = get_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)
    print_impact_analysis(Data(data_ETHUSDT['Close'], data_BTCUSDT['Close']))


# # Новые параметры
# x = np.hstack([x.reshape(-1, 1), data_ETHUSDT[['Open', 'High', 'Low', 'Volume']].to_numpy()])
#
# # Регрессия
# model = sm.OLS(y, sm.add_constant(x))
# results = model.fit()
#
#
# # print(results.summary())
#
# # Коэффициенты
# # print("Коэффициент линейной зависимости от BTCUSDT:", results.params[1])
# # print("Константа:", results.params[0])
#
# # Функция для выявления процента изменения
# def has_1pct_change(time_series):
#     min_val = time_series[0]
#     max_val = time_series[0]
#
#     for val in time_series:
#         if val < min_val:
#             min_val = val
#         if val > max_val:
#             max_val = val
#
#     pct_change = abs(max_val - min_val) / min_val * 100
#
#     if pct_change >= 1.:
#         return pct_change
#
#     return False
#
#
# # Вечный цикл оповещений
# while True:
#     latest_data_eth = get_klines('ETHUSDT', Client.KLINE_INTERVAL_1MINUTE, 60)
#     latest_data_btc = get_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, 60)
#     print(latest_data_eth['Close'].values)
#     # Собственные колебания ETHUSDT
#     eth_without_btc = latest_data_eth['Close'].values - results.params[1] * latest_data_btc['Close'].values
#     print(eth_without_btc)
#
#     change = has_1pct_change(eth_without_btc)
#     if change:
#         print(f'В течении последнего часа произошло изменение на {change:.2f}%')
#
#     time.sleep(60 * 60)
#

if __name__ == '__main__':
    main()
