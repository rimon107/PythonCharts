# We can use the pandas library in python to read in the csv file.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# This creates a pandas dataframe and assigns it to the titanic variable.

def LoadDataset():
    titanic = pd.read_csv("train.csv")
    return titanic


def DistributionLineChart():
    titanic = LoadDataset()
    sns.set(font_scale=1)
    titanic.Age[titanic.Pclass == 1].plot(kind='kde')    
    titanic.Age[titanic.Pclass == 2].plot(kind='kde')
    titanic.Age[titanic.Pclass == 3].plot(kind='kde')
     # plots an axis lable
    plt.xlabel("Age")    
    plt.title("Age Distribution within classes")
    # sets our legend for our graph.
    plt.legend(('1st Class', '2nd Class','3rd Class'),loc='best') ;

    plt.show()


DistributionLineChart()











