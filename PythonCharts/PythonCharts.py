# We can use the pandas library in python to read in the csv file.
import pandas as pd

#for numerical computaions we can use numpy library
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# This creates a pandas dataframe and assigns it to the titanic variable.
titanic = pd.read_csv("train.csv")

titanic_test = pd.read_csv("test.csv")

titanic_test.isnull().sum()

sns.set(font_scale=1)


ax = sns.boxplot(x="Survived", y="Age", 
                data=titanic)

ax = sns.stripplot(x="Survived", y="Age",
                   data=titanic, jitter=True,
                   edgecolor="gray")
plt.title("Survival by Age",fontsize=12);

plt.show()






