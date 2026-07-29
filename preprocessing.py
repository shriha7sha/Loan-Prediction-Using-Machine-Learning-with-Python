import pandas as pd

def preprocess(data):

    data = pd.get_dummies(data)

    return data
