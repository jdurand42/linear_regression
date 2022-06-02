import pandas as pd
from LinearRegression import LinearRegression
from data_processing import scale_data
import sys
import matplotlib.pyplot as plt

def print_metrics(metrics):
    print("---- METRICS ----")
    print("")
    for key in metrics:
        print(f"{key}: {metrics[key]}")

def plot_pred(X, y, pred, metrics):
    f = plt.figure("Eval")
    f.clear()
    plt.plot(X, y_pred, color="blue")
    plt.scatter(X, y, color="green")
    plt.scatter(X, y_pred, color="blue")

    for i in range(0, len(X)):
        plt.plot([X[i], X[i]], [y[i], y_pred[i]], linestyle="--", color="red")
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Please provide a valid csv file to evaluate your model as first arg")
    try:
        df = pd.read_csv(sys.argv[1])
        if "km" not in df or "price" not in df:
            raise ValueError("Error: Your csv must contain 'km' and 'price' column")
    except:
        sys.exit(1)

    data = scale_data(df.copy())
    X = data['km']
    y = data['price']

    reg = LinearRegression()
    reg.load()
    y_pred = reg.predict(X)
    metrics = reg.get_metrics(X, y)

    print_metrics(metrics)
    plot_pred(df['km'], y, y_pred, metrics)
