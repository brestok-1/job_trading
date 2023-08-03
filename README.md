# <div align="center">Ethereum tracking script 📈</div>

<div align="center">
<img src="assets/ethereum-1.jpg" align="center" style="width: 80%; height: 40%" />
</div>

<br/>

I made a script that tracks Ethereum's own movements, without the influence of Bitcoin. Thanks to this project, I got
acquainted with the Binance API, as well as with such mathematical concepts as correlation, the level of cointegration,
the construction of linear regression models, and many others.

## Description

<div align="center">
<img src="assets/btceth.jpg" align="center" style="width: 80%; height: 40%" />
</div>

<br/>

**I was given a test task**:

> 1. You need to determine the price movements of the ETHUSDT futures, excluding movements caused by the influence of
     the
     BTCUSDT price. Describe the methodology you chose, the parameters you selected, and why.
> 2. Write a Python program that tracks the real-time price of ETHUSDT futures with minimal delay, and using the method
     you selected, determines its own price movements. When the price changes by 1% in the last 60 minutes, the program
     outputs a message to the console. The program should continue to run, constantly reading the current price.

I have solved this task. I had to get acquainted with different methods and technologies of Data Science.

## Technologies

***Languages***

![Python](https://img.shields.io/badge/-Python-1C1C1C?&style=for-the-badge)

***Libraries***

![Python-binance](https://img.shields.io/badge/-Python--binance-1C1C1C?&style=for-the-badge)
![NumPy](https://img.shields.io/badge/-NumPy-1C1C1C?&style=for-the-badge)
![Pandas](https://img.shields.io/badge/-Pandas-1C1C1C?&style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/-matplotlib-1C1C1C?&style=for-the-badge)

First, I received data from the last 120 BTCUSDT and ETHUSDT klines and convert them to Pandas Dataframe objects. Next,
I determined the correlation levels of Pierce and cointegration by taking the closed price data of BTCUSDT as a
constant. Next, I created a linear regression model, specifying the BTCUSDT data as a constant, and thus, in the obtained
parameters, I determined the level of influence of BTCUSDT on ETHUSDT. Next, I analyzed the model and calculated the
predicted effect of BTCUSDT price changes on ETHUSDT price changes by multiplying the BTCUSDT price variables by the
factor 'BTC_IMPACT', which represents the force of influence, and built a graph consisting of the price movement of
BTCUSDT, ETHUSDT and ETHUSDT's own movements. I got a dataframe with data of my own movements and wrote a function that
determines the percentage of price change ETHUSDT.

## Project setup

***Via virtual environment***

1. Create and activate a python virtual environment
2. In the terminal, enter the following command:

```
pip3 install -r requirements.txt
```

3. Create a .env file and paste the data from the .env.example file into it
4. Log in to Binance, go to this page and create a new API key.
5. Copy the API Key and Secret Key, paste their values into the BINANCE_API_KEY and BINANCE_SECRET_KEY variables.
6. Run the file main.

## <div align="center">Thank you for using my script! 👋</div>