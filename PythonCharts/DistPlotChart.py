# We can use the pandas library in python to read in the csv file.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# This creates a pandas dataframe and assigns it to the titanic variable.

def LoadDataset():
    titanic = pd.read_csv("train.csv")
    return titanic


def DistPlotChart():
    titanic = LoadDataset()
    sns.set(font_scale=1)
    sns.set_style("whitegrid")
    sns.distplot(titanic["Age"].dropna(),
                 bins=80,
                 kde=False,
                 color="red")
    plt.title("Age Distribution")
    plt.ylabel("Count");

    plt.show()


DistPlotChart()
