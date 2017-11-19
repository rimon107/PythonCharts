# We can use the pandas library in python to read in the csv file.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd # conventional alias
from pandas.tools.plotting import parallel_coordinates
from sklearn import datasets
from statsmodels.graphics.mosaicplot import mosaic


def LoadDataset():
    dataset = pd.DataFrame({'size' : ['small', 'large', 'large', 'small', 'large', 'small'], 'length' : ['long', 'short', 'short', 'long', 'long', 'short']})
    
    return dataset


def ParrarelCorrelationPlotChart():
    dataset = LoadDataset()
    mosaic(dataset, ['size', 'length'])
    plt.show()


ParrarelCorrelationPlotChart()


