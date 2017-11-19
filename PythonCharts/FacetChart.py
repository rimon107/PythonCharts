# We can use the pandas library in python to read in the csv file.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# This creates a pandas dataframe and assigns it to the titanic variable.



def LoadDataset():
    titanic = pd.read_csv("train.csv")
    return titanic


def NormalFacetGridChart():
    titanic = LoadDataset()
    sns.set(font_scale=1)
    g = sns.FacetGrid(titanic, hue="Survived", col="Pclass", margin_titles=True,
                      palette={1:"seagreen", 0:"gray"})
    g=g.map(plt.scatter, "Fare", "Age",edgecolor="w").add_legend();

    plt.show()


def ModifiedFacetGridChart():
    titanic = LoadDataset()
    sns.set(font_scale=1)
    g = sns.FacetGrid(titanic, hue="Survived", col="Sex", margin_titles=True,
                palette="Set1",hue_kws=dict(marker=["^", "v"]))
    g.map(plt.scatter, "Fare", "Age",edgecolor="w").add_legend()
    plt.subplots_adjust(top=0.8)
    g.fig.suptitle('Survival by Gender , Age and Fare');
    plt.show()


ModifiedFacetGridChart()








