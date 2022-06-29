from LinearRegression import LinearRegression
from data_processing import scale_data
import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot(X, y):
    f = plt.figure("Best_fit")
    f.clear()
    plt.plot(X, y_pred, color="red", linestyle="--")
    plt.scatter(X, y, color="blue")
    plt.ioff()
    plt.show()


def get_data(argv):
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
    print(X.head())
    return X

if __name__ == '__main__':
    reg = LinearRegression()
    X = get_data(sys.argv[1:])
    if len(X['km']) == 0:
        sys.exit(0)
    reg.load()
    # print(X.head())
    X_pred = X.copy()
    # print(X_pred.head())
    X_pred = scale_data(X_pred, standard_dev=reg.standard_dev, mean=reg.mean)
    # print("ici", X_pred.head())
    X_pred = X_pred['km']
    y_pred = reg.predict(X_pred)
    print(y_pred)
    pred_report = pd.DataFrame(data={"km": X['km'], "price": y_pred})
    pred_report.to_csv("pred/prediction.csv")
    plot(X, y_pred)
