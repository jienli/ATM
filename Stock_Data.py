#######################################################################################
#       Try 1: not good, gave up (https://www.youtube.com/watch?v=AF8zgxLukg4&list=WL&index=23&t=1s)
#######################################################################################

# import pandas as pd
# import numpy as np
# from sklearn.svm import SVR
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# Load the Data
# from google.colab import files
# uploaded = files.upload()
# df = pd.read_csv("GOOG_30_dayd.csv")
# df.head(7)



#######################################################################################
#         Try 2: DOES NOT WROK (https://www.youtube.com/watch?v=V4kvcds6CWk) (Google deprecated)
#######################################################################################

# import pandas as pd
# import pandas_datareader.data as web
# import datetime as dt
# from datetime import datetime
# import os
#
# from Neural_Net_v1 import NeuralNetwork
#
#
# def get_stock_data():
#     tickers = ["MCD", "AAPL", "GOOGLE", "XOM"] # capitalize tickers
#
#     start = dt.datetime(2016,1,1) # can import 5 years mac with iex
#
#     end = dt.datetime(2016,1,20) # can import 5 years mac with iex
#     # end = dt.datetime.today()
#
#     if not os.path.exists("stockdata"):
#         os.makedirs("stockdata")
#
#     for ticker in tickers:
#         print (ticker)
#         try:
#             df = web.DataReader(ticker, "iex", start, end)
#             print(df.head())
#             df.to_csv("stockdata/{}.csv". format(ticker))
#             print(ticker, "downloaded")
#         except Exception as e:
#             print(e, "error")
#
#
# get_stock_data()



#######################################################################################
#         Try 3: TODO (https://www.youtube.com/watch?v=DOHg16zcUCc)
#######################################################################################

from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


START_DATE = '2005-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

# print(END_DATE)

UK_STOCK = 'UU.L'
USA_STOCK = 'GOOG'


# get data from yahoo finance
def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker,
                                    'yahoo',
                                    START_DATE,
                                    END_DATE)
        # # print(stock_data)
        # # print(clean_data(stock_data, 'Adj Close'))
        # adj_close = clean_data(stock_data, 'Adj Close')
        # # print(get_stats(adj_close))
        # create_plot(adj_close, ticker)
        return stock_data

    except RemoteDataError:
        print("No data found for {t}".format(t=ticker))


# clean any obviously wrong data
def clean_data(stock_data, col):
    weekdays = pd.date_range(start=START_DATE, end=END_DATE)
    # clean_data = (~stock_data[col]).reindex(weekdays)
    # cleaned_data = stock_data[col].reindex(weekdays)
    clean_data = stock_data[col]

    # print(cleaned_data)
    # for i in cleaned_data:
    #     print(i)

    return clean_data.fillna(method='ffill') # propogate non-null value
    # return clean_data.fillna(method=0) # fill any non-number to 0


def get_stats(stock_data):
    return {
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling': stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean(),
    }

def create_plot(stock_data, ticker):
    stats = get_stats(stock_data)
    # plt.style.use("dark_background")
    # plt.style.use("bmh")
    plt.style.use("ggplot")
    # plt.style.use("graystyle")
    # plt.style.use("fivethirtyeight")
    plt.subplots(figsize=(12, 8))
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling'], label="20 day rolling mean")
    plt.plot(stats['long_rolling'], label="200 day rolling mean")
    plt.xlabel("Date")
    plt.ylabel("Adj Close (p)")
    plt.legend()
    plt.title("Stock Price over Time")
    plt.show()


if __name__ == "__main__":
    ticker = USA_STOCK

    stock_data = get_data(ticker)

    adj_close = clean_data(stock_data, 'Adj Close')
    adj_close
    # adj_close = stock_data['Adj Close']
    print(adj_close)
    # print(get_stats(adj_close))
    create_plot(adj_close, ticker)
