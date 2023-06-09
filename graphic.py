import statsmodels.api as sm
import matplotlib.pyplot as plt

from movements import Data, BTC_IMPACT


def print_dependency_level(data: Data) -> None:
    """This function makes a price movement graphic"""
    btc_impact_price = _get_predict(data)
    fig, ax = plt.subplots()
    data.data_eth.Close.plot(ax=ax)
    data.data_eth.IM.plot(ax=ax)
    plt.plot(btc_impact_price)
    plt.title("Eth's movement")
    ax.legend(['Closing Price of Eth', 'Own movements', "Movement with Bitcoin"])
    plt.show()


def _make_scaling(data: Data) -> None:
    for df in (data.data_btc, data.data_eth):
        for price_type in ('Open', 'Close', "High", "Low"):
            df[price_type] = (df[price_type] - df[price_type].mean()) / df[price_type].std()


def _get_predict(data: Data) -> int:
    _make_scaling(data)
    model = sm.OLS(data.data_eth['Close'],
                   sm.add_constant(data.data_btc[['Open', 'High', 'Low', 'Volume']] * BTC_IMPACT)).fit()
    btc_impact_price = model.predict(sm.add_constant(data.data_btc[['Open', 'High', 'Low', 'Volume']] * BTC_IMPACT))
    data.data_eth['IM'] = data.data_eth['Close'] - btc_impact_price
    return btc_impact_price
