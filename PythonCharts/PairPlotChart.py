# We can use the pandas library in python to read in the csv file.

import matplotlib.pyplot as plt
import seaborn as sns




def LoadDataset():
    iris = sns.load_dataset("iris")
    return iris


def PairPlotChart():
    iris = LoadDataset()

    sns.set(font_scale=1)

    g = sns.pairplot(iris, hue="species")

    plt.show()



PairPlotChart()












