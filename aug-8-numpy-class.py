import numpy as np
import numpy.random as npr

print(np.version.version, "#"*20, '', sep=('\n'))

gerador = npr.default_rng(42)
array_1 = gerador.random((3, 3))
print(array_1, '\n')
print(gerador.standard_normal(10), '\n')
print(np.sort(array_1), '\n')
print(array_1.sort(), '\n\n', array_1)

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]

array_2 = np.array([0, 1, 2, 3])
array_3 = np.array([1, 2, 3, 4])
print(array_2, array_3)
print(lista_a*3, '\n\n', array_2*array_3)

print(lista_a+lista_b, array_2+array_3, array_2+20)

print('\n\n', array_2/array_3, array_3/2)

print('\n\n', array_3/0)
array_4 = array_3/0 + 2
print(array_4*0)

array_5 = array_2.reshape(1,4)
array_6 = array_3.reshape(4,1)
print(array_5, '\n\n' , array_6, '\n\n', array_6*array_5, '\n\n', array_5*array_6, '\n\n\n\n')


# 1
array_7 = np.ones((10))*42
print('Exercício 1: ', '\n',  array_7, '\n\n')

# 2
array_8 = np.arange(1, 10)
array_8 = array_8.reshape((3, 3))
print('Exercício 2: ', '\n', array_8, '\n\n')

array_9 = np.array([1, 2, 3, 4, 5, 6])
indices = array_9 > 3
print(indices, '\n\n', array_9[indices], '\n\n', array_9[array_9%2==0], '\n\n')

array_10 = np.arange(1, 10).reshape(3,3)
array_10_indexes = np.array([[True, False, True], [False, False, False], [True, True, True]])
print(array_10[array_10_indexes])

notas = np.array([80, 76, 95, 3, 42, 75])
print('Média das notas do filme: ')
print(round(np.average(notas), 2))
print('Mediana das notas do filme: ')
print(round(np.median(notas), 2))
print('Desvio padrão das notas do filme: ')
print(round(np.std(notas), 2))
print('Variância das notas do filme: ')
print(round(np.var(notas), 2))
print('Mínimo das notas do filme: ')
print(round(np.amin(notas), 2))
print('Máximo das notas do filme: ')
print(round(np.amax(notas), 2))
print('Alcance das notas do filme: ')
print(round(np.ptp(notas), 2))
print('Percentil das notas do filme: ')
print(round(np.percentile(notas, 70), 2))

ndarray = npr.standard_normal(10)
print('Exemplo 1: \n', ndarray, '\n', 'float16:', np.mean(ndarray, dtype = np.float16), '\n', 'float64: ',np.mean(ndarray, dtype = np.float64))