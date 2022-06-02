from LinearRegression import LinearRegression
from data_processing import scale_data
import pandas as pd

if __name__ == '__main__':
    data_path = "./data/data.csv"
    data = pd.read_csv(data_path)

    reg = LinearRegression()
    df = scale_data(data.copy())
    X = df['km']
    y = df['price']

    reg.fit(X, y, max_epochs=5000)
    y_pred = pd.DataFrame(reg.predict(X))
    X = data['km']
    reg.plot(X, y, y_pred)

    reg.export()
