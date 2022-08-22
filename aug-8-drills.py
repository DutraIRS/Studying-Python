import numpy as np
import numpy.random as npr

print('Exercício 1: ', '\n')
array_1 = np.arange(1, 12, 3)
array_2 = np.arange(2, 13, 3)
array_3 = array_1 + array_2
print(array_3, '\n\n')

print('Exercício 2: ', '\n')
array_3 = array_3.reshape(2,2)
array_3 = array_3 + np.zeros((2,2))
array_3 = array_3.transpose()
print(array_3, '\n\n')

print('Exercício 3: ', '\n')
array_4 = np.arange(0, 8, 2).reshape(2,2)
array_4 = array_3*array_4
print(array_4, '\n\n')

print('Exercício 4: ', '\n')
array_5 = npr.default_rng().integers(5, size = 10)
array_6 = npr.default_rng().integers(5, size = 10)
index = []
for i in range(len(array_5)):
    if array_5 in array_6:
        index = index.append(array_5[i])
print(index)