# We can use the pandas library in python to read in the csv file.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd # conventional alias
from pandas.tools.plotting import parallel_coordinates
from sklearn import datasets


def LoadDataset():
    dataset = datasets.load_iris()
    return dataset


def ParrarelCorrelationPlotChart():
    iris = LoadDataset()
    X = pd.DataFrame(iris.data[:, :4],columns=['sepal length','sepal width','petal  length','petal width']) # we only take the first two features.
    X['class'] = iris.target

    #pcp plot
    parallel_coordinates(X,'class')
    plt.show()


ParrarelCorrelationPlotChart()


