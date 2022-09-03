import numpy as np
import numpy.random as npr
import pandas as pd

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ['I', 'II', 'III', 'IV', 'V']
dicionario_1 = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
np_array_1 = np.array(lista_1)

print(lista_1)
print(lista_2)
print(dicionario_1)
print(np_array_1)
print(':)   '*42, '\n\n')

ser_1 = pd.Series(lista_1)
ser_2 = pd.Series(lista_2)
print('Série 1: ', ser_1, '\n', sep=('\n'))
print('Série 2: ', ser_2, '\n', sep=('\n'))

ser_3 = pd.Series(data=lista_1, index=lista_2)
print('Série 3:', ser_3, '\n', sep=('\n'))

ser_4 = pd.Series(dicionario_1)
print('Série 4:', ser_4, '\n', sep=('\n'))
print(ser_4 == ser_3, '\n', sep=('\n'))

ser_5 = pd.Series(np_array_1)
print('Série 5:', ser_5, '\n', sep=('\n'))

ser_6 = pd.Series(data=lista_2, index=lista_1)
print('Série 3:', ser_3, '\n', sep=('\n'))

print('NumPy:', np_array_1, type(np_array_1), '\n\n')
print('NumPy to List:', np_array_1.tolist(), type(np_array_1.tolist()), '\n\n')
print('Series to NumPy:', ser_1.to_numpy(), type(ser_1.to_numpy()), '\n\n')
print('Series to List:', ser_1.to_list(), type(ser_1.to_list()), '\n\n')

print('Acessando os elementos: \n', ser_1[:3], '\n\n', sep='')
print('Acessando os elementos: \n', ser_1[:-3], '\n\n', sep='')
print('Acessando os elementos: \n', ser_1.head(3), '\n\n', sep='')
print('Acessando os elementos: \n', ser_1.tail(3), '\n\n', sep='')
print('Acessando o elemento 4: ', ser_3['IV'], '\n\n', sep='')
print('Acessando o elemento 4: ', ser_3[3], '\n\n', sep='')

print('Series IdxMax: ', ser_3.idxmax(), '\n\n', sep='')
print('Series IdxMin: ', ser_3.idxmin(), '\n\n', sep='')

print('Series Loc: \n', ser_3.loc['I':'SADSADCLOWNS'], '\n\n', sep='')

print('Series Loc: \n', ser_3.iloc[0:4], '\n\n', sep='')

dicionario_2 = {'I':10, 'II':42, 'III':7, 'V':1_000_000}
dicionario_3 = {'I':1, 'II':13, 'III':51, 'IV':0}

ser_7 = pd.Series(dicionario_2)
ser_8 = pd.Series(dicionario_3)
ser_9 = ser_7.add(ser_8)
ser_10 = ser_7 + ser_8
print(ser_10 - ser_9, '\n\n')

print('Sum of Series: \n', ser_9, '\n\n', sep='')
print('Subtraction of Series: \n', ser_7.sub(ser_8), '\n\n', sep='')
print('Series\' Count: ', ser_9.count(), '\n\n', sep='')
print('Series\' Size: ', ser_9.size, '\n\n', sep='')

print(ser_6, '\n\n\n', ser_6[3], '\n\n')

dicionario_4 = {'V':42}
ser_11 = pd.Series(dicionario_4)
ser_12 = pd.concat([ser_8, ser_11])

print(ser_12)
