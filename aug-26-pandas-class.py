import numpy as np
import numpy.random as npr
import pandas as pd

dicionario_1 = {"I":10, 'II':42, 'III':7, 'V':1_000_000}
dicionario_2 = {'I':1, 'II':13, 'III':51, 'IV':0}

ser_1 = pd.Series(dicionario_1)
ser_2 = pd.Series(dicionario_2)

resultado = ser_1.add(ser_2, fill_value = 0)
print('Soma das séries: ', resultado, '\n\n', sep = '\n')
print('Soma das séries - Contagem: ', resultado.count(), '\n', sep = '\n')
print('Soma das séries - Tamanho: ', resultado.size, '\n', sep = '\n')

print('# Fill')
resultado = ser_1.add(ser_2)
resultado.fillna(42, inplace = True)
print('Soma das séries: ', resultado, '\n\n', sep = '\n')
print('Soma das séries - Contagem: ', resultado.count(), '\n', sep = '\n')
print('Soma das séries - Tamanho: ', resultado.size, '\n', sep = '\n')

print('# Drop')
resultado = ser_1.add(ser_2)
resultado.dropna(inplace = True)
print('Soma das séries: ', resultado, '\n\n', sep = '\n')
print('Soma das séries - Contagem: ', resultado.count(), '\n', sep = '\n')
print('Soma das séries - Tamanho: ', resultado.size, '\n', sep = '\n')