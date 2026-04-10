import numpy as np


a = np.array([0.3, 2.9, 4.0])

y1 = np.exp(a) / np.sum(np.exp(a))
y2 = np.exp(a-2) / np.sum(np.exp(a-2))
print(y1)
print(y2)