# We can use the pandas library in python to read in the csv file.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# This creates a pandas dataframe and assigns it to the titanic variable.

def LoadDataset():
    titanic = pd.read_csv("train.csv")
    return titanic


def CorrelationChart():
    titanic = LoadDataset()
    sns.set(font_scale=1)
    corr=titanic.corr()                                                     #["Survived"]
    plt.figure(figsize=(10, 10))

    sns.heatmap(corr, vmax=.8, linewidths=0.01,
                square=True,annot=True,cmap='YlGnBu',linecolor="white")
    plt.title('Correlation between features');

    plt.show()


CorrelationChart()










