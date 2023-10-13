import numpy as np
import matplotlib.pyplot as plt
#테스트 데이터를 만들어 넣어준다.
test_data = np.random.uniform(low=-10,high=10, size=(2,))
#4개의 클래스를 만들어준다.
n_classes = 4
#클래스당 총 100개의 데이터를 찍어준다.
n_data = 100
#데이터를 배열로 만들어 줄 빈 배열을 만들어준다.
data = []
centroids = [] # centroid 저장해야 나중에 그릴 수 있음

for _ in range(n_classes):
    centroid = np.random.uniform(low=-10, high=10, size=(2,))
    data_ = np.random.normal(loc=centroid, scale=1, size=(n_data, 2))

    centroids.append(centroid)  # centroid 저장해두기
    data.append(data_)

centroids = np.vstack(centroids) # (4, 2)의 centroid array
data = np.vstack(data)

fig, ax = plt.subplots(figsize=(5, 5))
for class_idx in range(n_classes):
    data_ = data[class_idx * n_data : (class_idx + 1) * n_data]
    ax.scatter(data_[:, 0], data_[:, 1], alpha=0.5)

for centroid in centroids: # centroid에 각각 접근해서 그리기
    ax.scatter(centroid[0], centroid[1], c='purple', marker='x', s=100)

#랜덤한 값의 데이터 값을 찍어준다.
ax.scatter(test_data[0],test_data[1],alpha=0.5,marker="x",color="black")

plt.show()