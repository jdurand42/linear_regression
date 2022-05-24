import pandas

def scale_data(data):
    df = data
    df['km'] = (df['km'] - df['km'].mean()) / df['km'].std()
    return df
