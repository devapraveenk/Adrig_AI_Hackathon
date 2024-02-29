import pickle
import sklearn
import pandas as pd

pickled_model = pickle.load(open('model.pkl', 'rb'))
def predict_text(s):
    out=pickled_model.predict([s])
    return (out[0])

def data(path):
    df=pd.read_csv(path)
    feature_column_name = df.columns[0]
    df['sentiment'] = pickled_model.predict(df[feature_column_name])
    df['sentiment'] = df['sentiment'].map({0: 'Negative', 1: 'Neutral',2:"Positive"})
    return df



