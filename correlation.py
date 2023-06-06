import pandas as pd
from typing import Literal
import statsmodels.api as sm
from scipy.stats import pearsonr
from typing import NamedTuple


class Cointegration(NamedTuple):
    coint_t: int
    pvalue: int
    crit_level: int


class Data(NamedTuple):
    ethusdt: pd.Series
    btcusdt: pd.Series


def print_impact_analysis(data: Data) -> None:
    cointegration_level = _get_cointegration_level(data)
    print(f'coint_t: {cointegration_level.coint_t}\n'
          f'pvalue: {cointegration_level.pvalue}\n'
          f'crit_value: {cointegration_level.crit_level}')
    corelation = _get_correlation_level(data)
    print(f'Correlation : {corelation}')


def _get_cointegration_level(data: Data) -> Cointegration:
    coint_t, pvalue, crit_level = sm.tsa.stattools.coint(data.ethusdt, data.btcusdt)
    return Cointegration(coint_t, pvalue, crit_level)


def _get_correlation_level(data: Data) -> int:
    corelation = pearsonr(data.ethusdt, data.btcusdt)[0]
    return corelation
