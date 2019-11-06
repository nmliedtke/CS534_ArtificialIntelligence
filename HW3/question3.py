from scipy.io import arff
import random
import matplotlib.pyplot as plt
import math
import pandas as pd
import matplotlib.patches as mpatches
import numpy as np
import question1
from sklearn.datasets import load_digits
from sklearn import metrics
from sklearn.cluster import AgglomerativeClustering, AffinityPropagation
def determineDigit(arr,digits):
    for i in range(0,len(digits.images)):
        flattened_list = []
        # flatten the lis
        for x in digits.images[i].tolist():
            for y in x:
                flattened_list.append(y)
        if arr == flattened_list:
            return digits.target[i]

def countNumsInCluster(cluster,digits):
    counts = [0] * 10
    for arr in cluster:
        i = determineDigit(arr,digits)
        #print("digitDetermined: " + str(i))
        counts[i] += 1

    return counts.index(max(counts))
def sciKitLabelClusters(clustering, digits):
    Z = np.zeros((max(clustering.labels_)+1,10))
    for i in range(0,len(clustering.labels_)):
        clusterVal = clustering.labels_[i]
        dig = determineDigit(digits.data[i].tolist(),digits)
        Z[clusterVal][dig] += 1
    labels = [-1] * (max(clustering.labels_)+1)
    for i in range(0,len(labels)):
        labels[i] = Z[i].tolist().index(max(Z[i]))
    return labels

def sciKitPredictionArr(clustering, labels):
    pred = clustering.labels_
    for i in range(0,len(pred)):
        pred[i] = labels[pred[i]]
    return pred

def labelClusters(clusters, digits):
    labels = [-1] * 10
    for i in range(0,len(clusters)):
        cluster = clusters[i]
        labels[i] = countNumsInCluster(cluster, digits)
    return labels

def predictionArr(clusters, labels):
    pred = []
    for i in range(0,len(clusters)):
        for data in clusters[i]:
            pred.append(labels[i])

    return pred

def trueArr(clusters, digits):
    true = []
    for cluster in clusters:
        for arr in cluster:
            true.append(determineDigit(arr,digits))

    return true

def confusionMatrix(trueArr, predArr):
    conf = np.zeros((10,10))

    for i in range(0,len(predArr)):
        conf[trueArr[i]][predArr[i]] += 1
    for i in range(0,10):
        if not i in predArr:
            conf[:,i] = -1
    return conf


digits = load_digits()
#digits.data= digits.data[0:6]
#print(digits.data)"""

#print(len(digits.images))

clusters = question1.k_means_cluster(digits.data.tolist(),10)
#print(clusters[0][0])
#print(determineDigit(clusters[0][0],digits))
#print(countNumsInCluster(clusters[0],digits))
labels = labelClusters(clusters,digits)
#print("labels" + str(labels))
pred = predictionArr(clusters,labels)
true = trueArr(clusters,digits)
conf = confusionMatrix(true,pred)
print("K means clustering confusion Matrix: ")
print(conf)
print("Fowlkes Mallows Score for K Means Clustering: " + str(metrics.fowlkes_mallows_score(true,pred)))

#print(digits.data[0])
clustering = AgglomerativeClustering(linkage='ward', distance_threshold=None,n_clusters=10)
clustering.fit(digits.data)
#expected  = digits.target
#predicted = clustering
aggLables = sciKitLabelClusters(clustering,digits)
aggPred = sciKitPredictionArr(clustering,aggLables)
aggConf = confusionMatrix(digits.target, aggPred)
print("Agglomerative Confusion Matrix")
print(aggConf)
print("Fowlkes Mallows Score for Agglomerative Clustering: " + str(metrics.fowlkes_mallows_score(digits.target, aggPred)))


clustering1 = AffinityPropagation().fit(digits.data)
print(clustering1.labels_)
affLables = sciKitLabelClusters(clustering1,digits)
affPred = sciKitPredictionArr(clustering1,affLables)
affConf = confusionMatrix(digits.target, affPred)
print("Affinity Confusion Matrix")
print(affConf)
print("Fowlkes Mallows Score for Affinity Clustering: " + str(metrics.fowlkes_mallows_score(digits.target, affPred)))

