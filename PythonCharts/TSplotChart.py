# We can use the pandas library in python to read in the csv file.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd # conventional alias
from pandas.tools.plotting import parallel_coordinates
from sklearn import datasets


def LoadDataset():
    dataset = sns.load_dataset("gammas")
    return dataset


def TSPlotChart():
    dataset = LoadDataset()
    sns.set(color_codes=True)

    ax = sns.tsplot(time="timepoint", value="BOLD signal",
                unit="subject", condition="ROI",
                data=dataset)

    plt.show()


TSPlotChart()



