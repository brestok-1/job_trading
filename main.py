from binance.client import Client
import time


from data import get_klines
from movements import Data, get_own_movements, print_eth_changes


def main():
    data_eth = get_klines('ETHUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)
    data_btc = get_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, 120)
    eth_own_movements = get_own_movements(Data(data_eth, data_btc))
    print_eth_changes(eth_own_movements)


if __name__ == '__main__':
    print('Etherium Tracking launched')
    while True:
        main()
        time.sleep(60 * 60)
