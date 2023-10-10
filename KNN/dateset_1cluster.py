#create dataset
#평균이 (5,3)이고 표준편차가 x,y 방향으로 모두 1인 (100,2) dataset 만들기

import numpy as np

n_data = 100
data = np.random.normal(loc=[5,3], scale=[1,1], size=(n_data,2))
print(data)
print(np.mean(data, axis=0))
print(np.std(data,axis=0))