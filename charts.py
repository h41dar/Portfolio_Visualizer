import matplotlib.pyplot as plt
import numpy as np


def chart_pie_percentage(data):

    result = [f'{k}: {v}' for k, v in data.items()]

    value = np.array(list(data.values()))
    key = list(result)

    plt.pie(value, labels=key, labeldistance=1)
    plt.legend(title='companies', loc='center left', bbox_to_anchor=(-0.6, 0.5))
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)

    plt.show()


def chart_bar_percentage(data):

    # result = [f'{k}: {v}' for k, v in data.items()]

    key = np.array(list(data.keys()))
    value = np.array(list(data.values()))

    plt.bar(key, value)
    plt.xticks(rotation=90)
    plt.show()
