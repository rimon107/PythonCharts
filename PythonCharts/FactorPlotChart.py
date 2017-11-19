# We can use the pandas library in python to read in the csv file.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# This creates a pandas dataframe and assigns it to the titanic variable.

def LoadDataset():
    titanic = pd.read_csv("train.csv")
    return titanic


def FactorPlotChart():
    titanic = LoadDataset()
    sns.set(font_scale=1)
    g = sns.factorplot(x="Age", y="Embarked",
                    hue="Sex", row="Pclass",
                    data=titanic[titanic.Embarked.notnull()],
                    orient="h", size=2, aspect=3.5, 
                   palette={'male':"purple", 'female':"blue"},
                    kind="violin", split=True, cut=0, bw=.2);

    plt.show()


FactorPlotChart()


