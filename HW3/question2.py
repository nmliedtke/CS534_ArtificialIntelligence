from scipy.io import arff
import random
import matplotlib.pyplot as plt
import math
import pandas as pd
import matplotlib.patches as mpatches

def logistic_regression(x,y):
    a=1

def fix_df(df):
   # df_new = df.select_dtypes(object)
    #mask = ~df_new.apply(lambda series: series.str.contains('?')).any(axis=1)
    #df = df[mask]

    df.drop(df[df.apply(lambda row: b'?' in row.to_string(header=False), axis=1)].index, inplace=True)
    for index, row in df.iterrows():

        print(float(row['sg']))



data = arff.loadarff('ckd_data\chronic_kidney_disease_full.arff')
print(data)
df = pd.DataFrame(data[0])

#fix_df(df)

df['appet'].apply(lambda x: x.decode("utf-8"))
print(df)