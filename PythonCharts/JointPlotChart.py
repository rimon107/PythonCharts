# We can use the pandas library in python to read in the csv file.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd # conventional alias
from sklearn.datasets import load_boston


def LoadDataset():
    dataset = load_boston()
    return dataset


def JointPlotChart():
    dataset = LoadDataset()
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

    sns.set(font_scale=1)
    print(df)
   
    x,y = df['RAD'], df['LSTAT']

    sns.jointplot(x, y, kind='scatter')

    # save to file, remove the big white borders
    plt.savefig('attribute_correlations.png', tight_layout=True)

    plt.show()



JointPlotChart()













