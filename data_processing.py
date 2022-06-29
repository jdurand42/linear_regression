import pandas
import numpy as np
from math import sqrt

def mean_list(x):
    return x.sum() / len(x)

def standard_deviation(X, mean):
    b = np.array([])
    if len(X) == 1:
        X.append(0.0)
    for x in X:
        b = np.append(b, (x - mean) * (x - mean))
    variance = mean_list(b)
    print(variance)
    return sqrt(variance)

def scale_data(data, mean=None, standard_dev=None):
    df = data
    if mean is None:
        mean = df['km'].mean()
    if standard_dev == None:
        standard_dev = standard_deviation(list(df['km']), mean)

    print("std", standard_dev)
    for i in range(0, len(df['km'])):
        df['km'][i] = (df['km'][i] - mean) / standard_dev

    # df['km'] = (df['km'] - df['km'].mean()) / standard_dev
    print(df.head(2))
    return df
