import numpy as np
import matplotlib.pyplot as plt

n_classes = 4
n_data =100
data = []
centroids=[] #centroid 저장해야 나중에 그릴 수 있음
for _ in range(n_classes):
    centroid = np.random.uniform(low=-10, high=10,size=(2,))
    data_ = np.random.normal(loc=centroid, scale=1, size=(n_data,2))

    centroids.append(centroids) #centroid 저장해두기
    data.append(data_)

centroids = np.vstack(centroids)# (4,2)의 centroid array
data = np.vstack(data)

fig, ax = plt.subplots(figsize=(5,5))
for class_idx in range(n_classes):
    data_ = data[class_idx * n_data :(class_idx+1)*n_data]

    ax.scatter(data_[:,0],data[:,1],alpha=0.5)

for centroid in centroids: #centroid에 각각 접근해서 그리기
    ax.scatter(centroid[0],centroid[1], c='purple', marker='x',s=100)

plt.show()