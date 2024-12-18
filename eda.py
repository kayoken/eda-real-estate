import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
import pandas as pd
from matplotlib.ticker import PercentFormatter

warnings.filterwarnings("ignore")


def init():
    plt.rcParams.update({"figure.figsize": (
        8, 5), "axes.facecolor": "white", "axes.edgecolor":  "black"})
    plt.rcParams["figure.facecolor"] = "w"
    pd.plotting.register_matplotlib_converters()
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    df_houses = pd.read_csv('./data/eda.csv')
    print(df_houses)


if __name__ == '__main__':
    init()
