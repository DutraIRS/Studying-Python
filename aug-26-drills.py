# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 07:55:05 2022

@author: b46832
"""

import numpy as np
import numpy.random as npr
import pandas as pd


ser_1 = pd.Series(npr.randint(10, size = 42))
ser_2 = pd.Series(npr.randint(10, size = 42))

# 1
def soma_ser(ser_1, ser_2, fill = 0):
    soma = ser_1.add(ser_2, fill_value = fill)
    return soma
    
def subtracao_ser(ser_1, ser_2, fill = 0):
    subtraction = ser_1.subtract(ser_2, fill_value = fill)
    return subtraction

def multiplicacao_ser(ser_1, ser_2, fill = 0):
    multiplication = ser_1.multiply(ser_2, fill_value = fill)
    return multiplication

def divisao_ser(ser_1, ser_2, fill = 0):
    division = ser_1.divide(ser_2, fill_value = fill)
    return division

# 2
def media_ser(ser_1):
    mean = ser_1.mean()
    return mean

def desv_pad_ser(ser_1):
    std = ser_1.std()
    return std

# 3

# pd.Series.value_counts()
# pd.Series.value_counts().sort_values()
# np.where(ser_1 % 5 == 0)

# # 4


# print(soma_ser(ser_1, ser_2), subtracao_ser(ser_1, ser_2), multiplicacao_ser(ser_1, ser_2), divisao_ser(ser_1, ser_2), media_ser(ser_1), desv_pad_ser(ser_1), sep = '\n\n')

# 5
ser_3 = ser_1 == ser_2
print(ser_1[ser_3])