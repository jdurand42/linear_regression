import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# import yaml
import json

class LinearRegression:
    def __init__(self, learning_rate=0.01, standard_dev=1.0, mean=0):
        self.theta1 = 0
        self.theta0 = 0
        self.l = learning_rate
        self.export_path = "./json/config.json"
        self.metrics = {}
        self.standard_dev = standard_dev
        self.mean = mean

    def fit(self, X, y, **kwargs):
        if "max_epochs" in kwargs:
            self.max_epochs = kwargs['max_epochs']
        y_pred = np.array([], dtype=np.float64)
        for epoch in range(0, self.max_epochs):
            y_pred = self.predict(X)
            m = len(X)
            b = self.theta0 - (self.l * ((1/m) * (np.sum(y_pred - y))))
            a = self.theta1 - (self.l * ((1/m) * (np.sum((y_pred - y) * X))))
            self.theta0 = b
            self.theta1 = a
        self.get_metrics(X, y)
        print(str(self))

    def predict(self, X):
        y_pred = np.array([], dtype=np.float64)
        for x in X:
            y_pred = np.append(y_pred, self.theta1 * x + self.theta0)
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
        self.metrics['RMSE'] = (1/m) * (np.sum((y - y_pred) * (y - y_pred)))
        self.metrics['MAE'] = (1/m) / abs(np.sum(y - y_pred))
        mean = y.mean()
        y_mean = np.full(m, mean)
        self.metrics['RSQUARE'] = 1 - ((np.sum((y - y_pred) * (y - y_pred))) / np.sum((y - y_mean) * (y - y_mean)))
        return self.metrics

    def export(self):
        config = {
            'theta1': self.theta1,
            'theta0': self.theta0,
            'metrics': self.metrics,
            'learning_rate': self.l,
            'export_path': self.export_path,
            'max_epochs': self.max_epochs,
            'standard_dev': self.standard_dev,
            'mean': self.mean
            }
        try:
            with open(self.export_path, "w+") as file:
                json.dump(config, file)
                print(f"Config successully writen to {self.export_path}")
        except:
            print("Error while writing config")
        file.close()

    def configurate(self, config):
        pass

    def load(self, **kwargs):
        path = self.export_path
        if path in kwargs:
            path = kwargs['path']
        try:
            with open(path, "r") as file:
                config = json.load(file)
                self.theta1 = config['theta1']
                self.theta0 = config['theta0']
                self.metrics = config['metrics']
                self.l = config['learning_rate']
                self.export_path = config['export_path']
                self.max_epochs = config['max_epochs']
                self.standard_dev = config['standard_dev']
                self.mean = config['mean']
                print("Object successully loaded")
                file.close()
        except:
            print("No conf file found, Initialazing with default value")

    def __str__(self):
        return f"a: {self.theta1}, b: {self.theta0}, metrics: {self.metrics}, std: {self.standard_dev}"
