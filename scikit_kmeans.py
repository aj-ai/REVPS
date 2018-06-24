""" Referenced: http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

"""

from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def inputClusters():
    print("Enter the number of clusters: ")
    numClusters = input()
    return int(numClusters)

def findClusterCenters(kmeans):
    return kmeans.cluster_centers_

def findMaxInClusterLongLat(cluster_map, i, maxindex):
    return (str(cluster_map[cluster_map.cluster == i]['latitude'][maxindex[i]]) + ", " +
        str(cluster_map[cluster_map.cluster == i]['longitude'][maxindex[i]]))

data = pd.read_csv('detroit-gun-violence-data_01-2013_03-2018.csv')
data.dropna(how = 'all', inplace = True)
X = data.loc[:, ['latitude', 'longitude']]
X.dropna(how = 'all', inplace = True)
numClusters = inputClusters()
kmeans = KMeans(n_clusters = numClusters, random_state = 0).fit(X)
X = data.loc[:, ['latitude', 'longitude', 'n_affected']]

cluster_map = pd.DataFrame()
cluster_map['data_index'] = X.index.values
cluster_map['latitude'] = X['latitude']
cluster_map['longitude'] = X['longitude']
cluster_map['numAffected'] = X['n_affected']
cluster_map['cluster'] = kmeans.labels_

maxlist = []
maxindex = []
for i in list(range(numClusters - 1)):
    maxlist.append(max(cluster_map[cluster_map.cluster == i]['numAffected']))
    maxindex.append(cluster_map[cluster_map.cluster == i]['numAffected'].idxmax(
        axis = 0, skipna = True))

print("KMeans Cluster Centers")
print(findClusterCenters(kmeans))

for i in list(range(numClusters - 1)):
    print("KMeans Cluster %s Max: " % str(i) + str(maxlist[i]))
    print(findMaxInClusterLongLat(cluster_map, i, maxindex))
    
    

    
