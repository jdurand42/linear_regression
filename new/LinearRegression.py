import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
import yaml

class LinearRegression:
    def __init__(self, learning_rate=0.01):
        self._a = 0
        self._b = 0
        self._l = learning_rate
        self._export_path = "./yaml/config.yaml"
        self._metrics = {}
        max_epochs = 10000

    def fit(self, X, y, **kwargs):
        if "max_epochs" in kwargs:
            self.max_epochs = kwargs['max_epochs']
        y_pred = np.array([], dtype=np.float64)
        for epoch in range(0, self.max_epochs):
            y_pred = self.predict(X)
            m = len(X)
            self._b = self._b - (self._l * ((1/m) * (np.sum(y_pred - y))))
            self._a = self._a - (self._l * ((1/m) * (np.sum((y_pred - y) * X))))
        self.get_metrics(X, y)
        print(str(self))

    def predict(self, X):
        y_pred = np.array([], dtype=np.float64)
        for x in X:
            y_pred = np.append(y_pred, self._a * x + self._b)
        return y_pred

    def plot(self, X, y, y_pred):
        # y_pred = self.predict(X)
        f = plt.figure("Best_fit")
        f.clear()
        plt.plot(X, y_pred, color="red")
        plt.scatter(X, y)
        #plt.plot(self.X, Y_pred, color="red")
        #plt.scatter(self.X, self.Y)
        plt.ioff()
        plt.show()

    def get_metrics(self, X, y):
        y_pred = self.predict(X)
        m = len(y_pred)
        b = np.array([], dtype=np.float64)

        # RMSE
        self._metrics['RMSE'] = (1/m) * (np.sum((y - y_pred) * (y - y_pred)))
        self._metrics['MAE'] = (1/m) / abs(np.sum(y - y_pred))
        print("mean: ", y.mean())
        mean = y.mean()
        y_mean = np.full(m, mean)
        self._metrics['RSQUARE'] = 1 - ((np.sum((y - y_pred) * (y - y_pred))) / np.sum((y - y_mean) * (y - y_mean)))


    def export(self):


    def configurate(self, config):
        pass

    def load(self, path):
        config = {
            'a': self._a,
            'b': self._b,
            'metrics': self._metrics,
            'learning_rate': self.l,
            '_export_path': self._export_path,
            'max_epochs': self.max_epochs,
        }
        try:
            with open(self._export_path, "w+"):

        pass

    def __str__(self):
        return f"a: {self._a}, b: {self._b}, metrics: {self._metrics}"
