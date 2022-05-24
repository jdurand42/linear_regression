from LinearRegression import LinearRegression
from data_processing import scale_data
import pandas as pd

# A value is standardized as follows:
#
#     y = (x – mean) / standard_deviation
#
# Where the mean is calculated as:
#
#     mean = sum(x) / count(x)
#
# And the standard_deviation is calculated as:
#
#     standard_deviation = sqrt( sum( (x – mean)^2 ) / count(x))


if __name__ == '__main__':
    data_path = "./data/data.csv"
    data = pd.read_csv(data_path)

    reg = LinearRegression()
    df = scale_data(data.copy())
    print(df.head())
    X = df['km']
    y = df['price']
    print(X.head())
    print(y.head())

    reg.fit(X, y, max_epochs=5000)
    y_pred = pd.DataFrame(reg.predict(X))
    X = data['km']
    # print("ici X", X.head())
    # print(y.head())
    # print(y_pred.head())
    reg.plot(X, y, y_pred)

    reg.export()

# reg2 = LinearRegression()
# reg2.load()
# print(str(reg2))

# scale data
