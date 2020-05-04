# Guidelines 

About 5-8 pages 

A documentation of the design.

Demonstration of the project. 

how readme.md works:
https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax


# Network-Science Final Project: ATM Machine

This project is an attempt to predict security fluctuations and help human traders make more rational and favorable decisions. Its decision-making ability will root in machine learning based on neural networks. The ultimate goal of this algorithm is to be trained by historical stock data to achieve the goal of attaining a high win rate as the stock market plays out in real time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them (pandas and whatnot)

```
Open the terminal, go to the home directory, and type pip install pandas.
```

![](images/pandas:install.png)

### Installing

A step by step series of examples that tell you how to get a development env running

First go to your desired repository and make a local clone of the project. 

```
Example: Corys-MacBook-Pro:project corry$ git clone https://github.com/jienli/ATM.git
```

Then go to the ATM file.

```
Corys-MacBook-Pro:project corry$ cd ATM
```
Open your text editor. In our case we use Atom. 

```
Corys-MacBook-Pro:ATM corry$ atom .
```
Try the files ending with .py. These are the sample results.
![](https://github.com/jienli/ATM/blob/master/images/5791588609220_.pic_hd.jpg)
![](https://github.com/jienli/ATM/blob/master/images/5801588609231_.pic_hd.jpg)
![](https://github.com/jienli/ATM/blob/master/images/5811588609244_.pic_hd.jpg)
![](https://github.com/jienli/ATM/blob/master/images/5821588609272_.pic_hd.jpg)
![](https://github.com/jienli/ATM/blob/master/images/5831588609290_.pic_hd.jpg)
![](https://github.com/jienli/ATM/blob/master/images/WechatIMG901.png)

## Running the tests

Before running each individual test, change the constant inputs in Constants.py to your desired indexes.
```
Description of what each constant represents: 
Test: 
Repo: number of test set (stock data of consecutive days).
INFO: number of data in each set.
STARTDATE: number of days after the year of 2005, January 1, as the starting date of our test. 
TRAIN_ITERATION: number of training iterations.
NUM_OF_STARTING_POINTS: mumber of starting points.
STRUCTURE: neural network structure, number of nodes in each layer(first layer need to match info), last layer need to be 1, only 3 layers for now
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

