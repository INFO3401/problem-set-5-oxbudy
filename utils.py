import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


def helloWorld():
  print("Hello, World!")

def loadAndCleanData(filename):
    data = pd.read_csv(filename, encoding='utf-8')
    data = data.dropna(axis=0)
    #print(data)
    return data

def computeProbability(feature, bin, data):
    # Count the number of datapoints in the bin
    count = 0.0

    for i,datapoint in data.iterrows():
        # See if the data is in the right bin
        if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
            count += 1

    # Count the total number of datapoints
    totalData = len(data)

    # Divide the number of people in the bin by the total number of people
    probability = count / totalData

    # Return the result
    return probability

def getConfidenceIntervals(column, dataframe):
    mean = dataframe[column].mean()
    sigma = dataframe[column].std()
    return stats.norm.interval(0.95, loc=mean, scale=sigma)

def runTTest(column1, column2, dataframe):
    return stats.ttest_ind(dataframe[column1], dataframe[column2])


#---------------------------------------------------------------------
#Problem Set 5
#8
def mergeData(dataframe1, dataframe2, mergecol):
    dataframe1[mergecol] = dataframe2[mergecol]
    #dataframe1.fillna(0)
    return dataframe1

#10
def plotTimeline(dataframe, x, y):
    plt.plot(dataframe[x], dataframe[y], '.')
    plt.show()

#12
def plotMultipleTimelines(dataframe, x, y, huecol):
    #c_map = {'US': 'g', 'China': 'r'}
    plt.scatter(dataframe[x],dataframe[y], c=huecol, cmap='inferno', marker='.')
    plt.show()

#d
