import numpy as np
import random
import matplotlib.pyplot as plt
import math
import pandas as pd
import matplotlib.patches as mpatches
#from scipy.spatial import distance


def k_means_cluster(xy, k):
    print(xy)

    rands = random.sample(range(0,len(xy)),k)

    clusters = [[] for i in range(k)]
    oldClusters = [[] for i in range(k)]
    means = []
    for i in range(0,len(rands)):
        means.append(xy[rands[i]])

    clustering = True
    n = 0
    while clustering:

        n += 1
        for p in xy:
            min_index = -1
            min_distance = 9999999
            for i in range(0,len(means)):
                temp_distance = distance(p,means[i])
                if temp_distance < min_distance:
                    min_distance = temp_distance
                    min_index = i
            clusters[min_index].append(p)
        means = update_means(clusters)
        if n % 20 == 0:
            print(n)
        if np.array_equal(oldClusters, clusters):
            clustering = False
        oldClusters = clusters

        clusters = [[] for i in range(k)]
    print(n)
    return oldClusters

def update_means(clusters):
    k = len(clusters)
    means = []
    for cluster in clusters:
        means.append(average_points(cluster))

    return means


def average_points(list_p):
    sums = [0] * len(list_p[0])
    n = 0
    for p in list_p:
        n += 1
        for i in range(0,len(p)):
            sums[i] += p[i]
    avg = []
    for sum in sums:
        avg.append(sum/n)
    return avg


def distance(p1,p2):
    num = 0
    for i in range(0,len(p1)):
        temp1 = p1[i]
        temp2 = p2[i]
        num += (temp1 - temp2)**2

    num = math.sqrt(num)
    return num
    #dist = distance
    #return dist

def display_clusters(clusters):
    x = []
    y = []
    colors = []
    colmap = ['r','g','b','y','o']

    for i in range(0,len(clusters)):
        for p in clusters[i]:
            x.append(p[0])
            y.append(p[1])
            colors.append(colmap[i])
    plt.scatter(x,y,color=colors)
    patches = []
    for i in range(0,len(clusters)):
        currStr = "Cluster " + str(i)
        patches.append(mpatches.Patch(color=colmap[i], label=currStr))
    plt.legend(handles=patches)
    plt.xlabel("Length")
    plt.ylabel("Width")
    plt.show()






data = pd.read_csv('cluster_data.txt', sep='	', header=None)
data.columns = ["row#","x","y"]
xy = []
for index, row in data.iterrows():
   xy.append([row['x'], row['y']])

clusters = k_means_cluster(xy, 2)
display_clusters(clusters)

print("End of Problem 1")

# It seems to make the most sense to cluster the data into two groups
# The data ends up being two clusters of two diamonds










