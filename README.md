# Guidelines 

About 5-8 pages 

describe what the codes does

how readme.md works:
https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax


# Project Title

This project is an attempt to predict security fluctuations and help human traders make more rational and favorable decisions. Its decision-making ability will root in machine learning based on neural networks. The ultimate goal of this algorithm is to be trained by historical stock data to achieve the goal of attaining a high win rate as the stock market plays out in real time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them (pandas and whatnot)

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Before running each individual test, change the constant inputs in Constants.py to your desired indexes.
```
Description of what each constant represents: 
Test: 
Repo:
INFO:
STARTDATE: number of days after the year of 2005, as the starting date of our test. 
TRAIN_ITERATION: number of training iterations.
NUM_OF_STARTING_POINTS: mumber of starting points.
STRUCTURE: 
TICKER: the stock symbol. 
BIAS: 
DRUNKNESS_INDEX: speed of training. 
```
```
Examples Constants set
TEST = 100
REP = 200
INFO = 10
STARTDATE = 2500
TRAIN_ITERATION = 10000
NUM_OF_STARTING_POINTS = 5
STRUCTURE = [10,3,1]
TICKER = 'GOOG'


BIAS = -1
DRUNKNESS_INDEX = 1.2

```

result: (just examples)

![](images/1%20FFN%201%20with%20test%20dat.png)
![](images/1%20FFN%202%20with%20test%20data.png)


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [numpy] - Used for fast matri manipulations
* [pandas] - For retrieving historical stock data


## Versioning

This is the only version!

## Authors

* **Jien Li** 
* **Anran Du** 
* **Chuyu Duan** 


## License

License? What license?

## Acknowledgments

* thank you for reading this far

