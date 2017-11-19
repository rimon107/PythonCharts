# We can use the pandas library in python to read in the csv file.
import matplotlib.pyplot as plt
import numpy as np


def ErrorBarPlotChart():
    x = np.linspace(0, 2 * np.pi)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.errorbar(x, y_sin, 0.2)
    plt.errorbar(x, y_cos, 0.2)
    plt.show()

    plt.show()


ErrorBarPlotChart()




