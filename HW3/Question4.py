from scipy.io import arff
import random
import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def logistic_regression(x,y):
    a=1

def fix_df(df):
    df_copy = pd.DataFrame().reindex_like(df)
    df_copy['age'] = df['age']
    df_copy['bp'] = df['bp']
    df_copy['bgr'] = df['bgr']
    df_copy['bu'] = df['bu']
    df_copy['sc'] = df['sc']
    df_copy['sod'] = df['sod']
    df_copy['pot'] = df['pot']
    df_copy['hemo'] = df['hemo']
    df_copy['pcv'] = df['pcv']
    df_copy['wbcc'] = df['wbcc']
    df_copy['rbcc'] = df['rbcc']
    #print(df_copy['bp'])
    df_copy=(df_copy-df_copy.min())/(df_copy.max()-df_copy.min())


    # deal with sg
    for i in range(0,len(df_copy)):
        sg = df.iloc[i]['sg']
        al = df.iloc[i]['al']
        su = df.iloc[i]['su']
        rbc = df.iloc[i]['rbc']
        pc = df.iloc[i]['pc']
        pcc = df.iloc[i]['pcc']
        ba = df.iloc[i]['ba']

        htn = df.iloc[i]['htn']
        dm = df.iloc[i]['dm']
        cad = df.iloc[i]['cad']
        appet = df.iloc[i]['appet']
        pe = df.iloc[i]['pe']
        ane = df.iloc[i]['ane']
        classVal = df.iloc[i]['class']

        if sg == b'1.005':
            df_copy.iloc[i]['sg'] = 0
        elif sg == b'1.010':
            df_copy.iloc[i]['sg'] = 0.25
        elif sg == b'1.015':
            df_copy.iloc[i]['sg'] = 0.5
        elif sg == b'1.020':
            df_copy.iloc[i]['sg'] = 0.75
        elif sg == b'1.025':
            df_copy.iloc[i]['sg'] = 1

        if al == b'0':
            df_copy.iloc[i]['al'] = 0
        elif al == b'1':
            df_copy.iloc[i]['al'] = 0.2
        elif al == b'2':
            df_copy.iloc[i]['al'] = 0.4
        elif al == b'3':
            df_copy.iloc[i]['al'] = 0.6
        elif al == b'4':
            df_copy.iloc[i]['al'] = 0.8
        elif al == b'5':
            df_copy.iloc[i]['al'] = 1

        if su == b'0':
            df_copy.iloc[i]['su'] = 0
        elif su == b'1':
            df_copy.iloc[i]['su'] = 0.2
        elif su == b'2':
            df_copy.iloc[i]['su'] = 0.4
        elif su == b'3':
            df_copy.iloc[i]['su'] = 0.6
        elif su == b'4':
            df_copy.iloc[i]['su'] = 0.8
        elif su == b'5':
            df_copy.iloc[i]['su'] = 1

        if rbc == b'abnormal':
            df_copy.iloc[i]['rbc'] = 0
        elif rbc == b'normal':
            df_copy.iloc[i]['rbc'] = 1

        if pc == b'abnormal':
            df_copy.iloc[i]['pc'] = 0
        elif pc == b'normal':
            df_copy.iloc[i]['pc'] = 1

        if pcc == b'notpresent':
            df_copy.iloc[i]['pcc'] = 0
        elif pcc == b'present':
            df_copy.iloc[i]['pcc'] = 1

        if ba == b'notpresent':
            df_copy.iloc[i]['ba'] = 0
        elif ba == b'present':
            df_copy.iloc[i]['ba'] = 1

        if htn == b'no':
            df_copy.iloc[i]['htn'] = 0
        elif htn == b'yes':
            df_copy.iloc[i]['htn'] = 1

        if dm == b'no':
            df_copy.iloc[i]['dm'] = 0
        elif dm == b'yes':
            df_copy.iloc[i]['dm'] = 1

        if cad == b'no':
            df_copy.iloc[i]['cad'] = 0
        elif cad == b'yes':
            df_copy.iloc[i]['cad'] = 1

        if appet == b'poor':
            df_copy.iloc[i]['appet'] = 0
        elif appet == b'good':
            df_copy.iloc[i]['appet'] = 1

        if pe == b'no':
            df_copy.iloc[i]['pe'] = 0
        elif pe == b'yes':
            df_copy.iloc[i]['pe'] = 1

        if ane == b'no':
            df_copy.iloc[i]['ane'] = 0
        elif ane == b'yes':
            df_copy.iloc[i]['ane'] = 1

        if classVal == b'notckd':
            df_copy.iloc[i]['class'] = 0
        elif classVal == b'ckd':
            df_copy.iloc[i]['class'] = 1
    #print(df_copy)
    #print(df_copy.to_string())
    return df_copy
   # df_new = df.select_dtypes(object)
    #mask = ~df_new.apply(lambda series: series.str.contains('?')).any(axis=1)
    #df = df[mask]

    #df.drop(df[df.apply(lambda row: b'?' in row.to_string(header=False), axis=1)].index, inplace=True)
    #for index, row in df.iterrows():

     #   print(float(row['sg']))

def removeNaN(df):
    numerical = ['age', 'bp', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']
    categorical = ['sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
    for title in numerical:
        df[title] = df[title].fillna(df[title].mean())

    for title in categorical:
        df[title] = df[title].fillna(df.mode()[title][0])
    return df

def calcFMeasure(pred, actual):
    TP = 0
    FP = 0
    FN= 0
    for i in range(0,len(pred)):
        if pred[i] == actual[i]:
            TP += 1
        elif pred[i] > actual[i]:
            FP += 1
        elif pred[i] < actual[i]:
            FN += 1
    Pre = TP / (TP + FP)
    Rec = TP / (TP + FN)

    f = (2 * Pre * Rec) / (Pre + Rec)
    return f


data = arff.loadarff('ckd_data\chronic_kidney_disease_full.arff')
#print(data)
df = pd.DataFrame(data[0])

#fix_df(df)


#print(df)
#print(df.iloc[0]['class'] == b'ckd')
#print(df.max())
#print(df.to_string())
df = fix_df(df)


#print(df.to_string())
#print("rbc")
#print(df['rbc'].mode())
df = removeNaN(df)
#print(df.to_string())
#print(df.columns.values[:-1])
#print(df.columns.values[:-1])
dfSamp = df.sample(frac=0.8)
dfTest = df.drop(dfSamp.index)
df1 = dfSamp[dfSamp.columns.values[:-1]]
df2 = dfSamp[['class']]

dfTestVals = dfTest[dfTest.columns.values[:-1]]
dfTestClassifier = dfTest[['class']]

X = df1.values
y = np.ravel(df2.values)

clf = SVC(gamma='auto',kernel='linear')
clf.fit(X, y)
#print(dfTest)
#print(dfTest.values[:][:-1])
#print(dfTestClassifier)
#print(clf.predict(dfTestVals.values))
print("F Measure for Linear SVM: " + str(calcFMeasure(clf.predict(dfTestVals.values), dfTestClassifier.values)))

clf1 = SVC(gamma='auto',kernel='rbf')
clf1.fit(X, y)
print("F Measure for RBF SVM: " + str(calcFMeasure(clf1.predict(dfTestVals.values), dfTestClassifier.values)))

clf2 = RandomForestClassifier(n_estimators=100)
clf2.fit(X,y)
print("F Measure for Random Forest: " + str(calcFMeasure(clf2.predict(dfTestVals.values), dfTestClassifier.values)))
