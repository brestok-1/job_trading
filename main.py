import time

from data import DATA_ETH, DATA_BTC
from graphic import print_dependency_level
from movements import Data, get_own_movements, print_eth_changes, BTC_IMPACT


def main():
    eth_own_movements = get_own_movements(BTC_IMPACT)
    print_eth_changes(eth_own_movements)


if __name__ == '__main__':
    print('Etherium Tracking launched')
    print_dependency_level(Data(DATA_ETH, DATA_BTC))
    while True:
        main()
        time.sleep(3)
