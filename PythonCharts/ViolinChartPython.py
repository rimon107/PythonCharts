import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show():
    # Load the data
    sns.set_style("whitegrid")

    # Create violinplot
    tips = sns.load_dataset("tips")

    sns.violinplot(x="day", y="total_bill", data=tips)

    # Show the plot
    plt.show()



show()

