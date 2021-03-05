import pandas_datareader as pdr
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime

currency = "TRY"
cryptoOne = "BTC"
cryptoTwo = "AVAX"

start = datetime.datetime(2021,1,1)
end = datetime.datetime.now()

avax = pdr.DataReader(f"{cryptoOne}-{currency}", "duckduckgo", start, end)
btc = pdr.DataReader(f"{cryptoTwo}-{currency}", "duckduckgo", start, end)

plt.yscale("log")

plt.plot(btc["Close"], label="BTC")
plt.plot(avax["Close"], label="AVAX")
plt.legend(loc="upper left")

mpf.plot(data, type="candle", volume=True, style="duckduckgo")

plt.show()
