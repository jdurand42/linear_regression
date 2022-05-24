from LinearRegression import LinearRegression
from data_processing import scale_data
import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot(X, y):
    f = plt.figure("Best_fit")
    f.clear()
    plt.plot(X, y_pred, color="red")
    plt.scatter(X, y, color="blue")
            #plt.plot(self.X, Y_pred, color="red")
            #plt.scatter(self.X, self.Y)
    plt.ioff()
    plt.show()


def get_data(argv):
    # X = pd.DataFrame(data={'km': []})
    i = 0
    b = []
    while i < len(argv):
        if argv[i] == '--csv':
            if i == len(argv):
                raise RuntimeError("Error: --csv option must be followed by a valid csv path")
            else:
                try:
                    df = pd.read_csv(argv[i+1])
                    for el in df['km']:
                        b.append(el)
                    i += 2
                    continue
                except:
                    raise RuntimeError("Error: --csv option must be followed by a valid csv path that contains a 'km' color")
        if isinstance(argv[i], (str)):
            try:
                b.append(float(argv[i]))
            except:
                raise ValueError("Error: Numeric options must be float")
        i += 1
    X = pd.DataFrame(data={'km': b})
    return X


# def build_prediction(X, y, path="pred/prediction.csv"):

if __name__ == '__main__':
    reg = LinearRegression()
    # for arg in sys.argv[1:]:
    #     print(arg)
    X = get_data(sys.argv[1:])
    print(len(X['km']))
    if len(X['km']) == 0:
        sys.exit(0)
    print(X.head(27))
    # X_pred = X.copy()
    reg.load()
    X_pred = X.copy()
    X_pred = scale_data(X_pred)
    X_pred = X_pred['km']
    y_pred = reg.predict(X_pred)
    print(y_pred)

    pred_report = pd.DataFrame(data={"km": X['km'], "price": y_pred})
    # print(pred_report.head())
    pred_report.to_csv("pred/prediction.csv")
    plot(X, y_pred)
