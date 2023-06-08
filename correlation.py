import pandas as pd
from typing import Literal
import statsmodels.api as sm
from scipy.stats import pearsonr
from typing import NamedTuple
from statsmodels.iolib.summary2 import Summary
from statsmodels.regression.linear_model import RegressionResults


class Cointegration(NamedTuple):
    coint_t: int
    pvalue: int
    crit_level: int


class DataSeries(NamedTuple):
    ethusdt: pd.Series
    btcusdt: pd.Series

