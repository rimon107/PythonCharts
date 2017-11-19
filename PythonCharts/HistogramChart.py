# We can use the pandas library in python to read in the csv file.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# This creates a pandas dataframe and assigns it to the titanic variable.
titanic = pd.read_csv("train.csv")

sns.set(font_scale=1)

g = sns.FacetGrid(titanic, col="Sex", row="Survived", margin_titles=True)
g.map(plt.hist, "Age", color="purple");

plt.show()







