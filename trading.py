from binance.client import Client

from data import get_klines

# Последние 120 свечей фьючерса ETHUSDT и BTCUSDT с интервалом 1 минута
data_ETHUSDT = get_klines('ETHUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)
data_BTCUSDT = get_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)

