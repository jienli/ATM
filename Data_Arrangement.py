from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

import Stock_Data as sdata
from Neural_Net import NeuralNetwork
import Constants as CONSTANT



"""
format:

rep = 100                   # number of test set (stock data of consecutive days)
info = 20                   # number of data in each set
startDate = 2500            # start day, days from 2005.01.01
train_iteration = 10000     # number of times it trains
structure=[20,5,1]          # neural network structure, number of nodes in each layer
                            # (first layer need to match info), last layer need to be 1, only 3 layers for now
"""
test = CONSTANT.TEST
rep = CONSTANT.REP
info = CONSTANT.INFO
startDate = CONSTANT.STARTDATE
train_iteration = CONSTANT.TRAIN_ITERATION
structure = CONSTANT.STRUCTURE
num_of_starting_points = CONSTANT.NUM_OF_STARTING_POINTS


## Get Stock Data from "Stock_Data"

# Common Tickers: SPX???; GOOG; AAPL; TSLA;
ticker = CONSTANT.TICKER

stock_data = sdata.get_data(ticker)
adj_close_raw = sdata.clean_data(stock_data, 'Adj Close')




## ASSEMBLE THE TRAINING DATA SET
## Group to 100 days data as input and the following day as output

# Adjust prices to 0-1
max = 0
min = np.inf

#     # accoding to only the train and test data
# for j in range(startDate, startDate + info + rep + test + 1):
#     i = adj_close_raw[j]
#     if (i > max):
#         max = i
#     if (i < min):
#         min = i
#     # give a little wiggle room
# min = min * 0.9
# max = max * 1.1

    # accoding to the entire data history
for i in adj_close_raw:
    if (i > max):
        max = i
    if (i < min):
        min = i


print(min, max)
adj_close = (adj_close_raw - min) / (max - min)



training_inputs = np.empty((rep,info))
# print(training_inputs)
training_outputs = np.empty((rep, 1))

for i in range(0, rep):
    ## Get the Inputs
    training_inputs[i] = np.asarray(adj_close[startDate + i:startDate + i + info], dtype=np.float32)
    # np.append(training_inputs, np.asarray(adj_close[i:i + 100]))

    ## Get the Outputs
    training_outputs[i] = np.asarray(adj_close[startDate + i + info + 1], dtype=np.float32)
    # np.append(training_outputs, np.asarray(adj_close[i + 101]))
    # if (adj_close[i + 1] > adj_close[i]):
    #     training_outputs.append(1)
    # else:
    #     training_outputs.append(0)



# print("training inputs :")
# print(training_inputs[1:50])
# print("training outputs :")
# print(training_outputs[1:50])

np.set_printoptions(suppress=True)

neural_network = NeuralNetwork(structure=structure)

print("Random synaptic weights: ")
print(neural_network.synaptic_weights)

neural_network.train(training_inputs, training_outputs, train_iteration, num_of_starting_points)

print()
print("Synaptic wieght after training: ")
print(neural_network.synaptic_weights)


# Change parameter so that the graphing takes in the testing set (the next 50 days)
# Also add the testing data to the input data array
rep += test
training_and_testing_inputs = np.empty((rep,info))
training_and_testing_outputs = np.empty((rep, 1))
for i in range(0, rep):
    ## Get the Inputs
    training_and_testing_inputs[i] = np.asarray(adj_close[startDate + i:startDate + i + info], dtype=np.float32)
    # np.append(training_inputs, np.asarray(adj_close[i:i + 100]))



# Graph the predicted and the original
predicted = []
original = adj_close_raw[startDate + 1 + info : startDate + rep + info]
for i in range(0, rep):
    layer = neural_network.think(training_and_testing_inputs[i])
    predicted.append(layer[len(layer) - 1][0] * (max - min) + min)

# for i in range(0, rep):
#     original[i].append(predicted[i])

predicted_arr = np.asarray(predicted)
original_arr = np.asarray(original)

max
plt.style.use("ggplot")
plt.subplots(figsize=(12, 8))
# plt.plot(adj_close_raw[1+info:rep+info], label="Original")
plt.plot(original_arr, label="Original")
plt.plot(predicted_arr, label="Predicted")
plt.axvline(x=rep - test, color='k', linestyle='--')
# plt.plot(predicted, label="Predicted")
plt.xlabel("Date")
plt.ylabel("Adj Close (p)")
plt.legend()
plt.title("Stock Price over Time (GOOG)")
plt.show()
