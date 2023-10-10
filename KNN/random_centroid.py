#random_centroid
import numpy as np
import matplotlib.pyplot as plt

#centroid로 기준값이 되는 값을 설정
centroid = np.random.uniform(low=-5,high=5,size=(2,))

#100이라는 값
n_data = 100

#data 변수를 만들고 무작위로 뽑을 수 있고, 위치는 centroid가 되는 것으로 설정
data = np.random.normal(loc=centroid,scale=1,size=(n_data,2))

plt.scatter(centroid[0],centroid[1],c='red')
plt.scatter(data[:,0],data[:,1])

plt.show()