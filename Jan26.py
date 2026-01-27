import numpy as np 
import matplotlib.pyplot as plt

'''x = np.arange(0, 6, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
'''

#Perceptron
# x = input value(0,1), y = output vlaue(0,1), b = bias, w = weight
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.9
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.9
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 1
    else:
        return 0
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.4
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    tmp = AND(NAND(x1,x2), OR(x1,x2))
    print(tmp)


XOR(0,0)
XOR(0,1)
XOR(1,0)
XOR(1,1)