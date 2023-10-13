import numpy as np

n_classes=4
n_data = 100

data = []
for class_idx in range(n_classes):
    data_ = class_idx * np.ones(100,)
    data.append(data_)
data = np.hstack(data)
print(data.shape)