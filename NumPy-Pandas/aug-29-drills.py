import numpy as np
import numpy.random as npr
import pandas as pd

# 1: Write a program that finds the elements of a series that don't belong to a second series
ser_1 = pd.Series([1, 2, 3, 9])
ser_2 = pd.Series([3, 9, 5, 4, 7, 0])
ser_3 = pd.Series([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 6, 8, 9, 9, 9, 9, 9])

def uniques(ser_1, ser_2):
    shared_list = []
    unique_list = []
    
    for i in range(len(ser_1)):
        for j in range(len(ser_2)):
            if ser_1[i] == ser_2[j]:
                shared_list.append(ser_1[i])
    
    for i in range(len(ser_1)):
        if ser_1[i] not in shared_list:
            unique_list.append(ser_1[i])
    
    return unique_list
    
print(uniques(ser_1, ser_2))

# Teacher's solution
# step 1: ser_1.isin(ser_2)
# step 2: ~ ser_1.isin(ser_2)
# answer: ser_1[~ ser_1.isin(ser_2)]

# 2: Write a program that finds a series' elements' positions in another series
def positions_shared(ser_1, ser_2):
    positions_list = []
    
    for i in range(len(ser_1)):
        for j in range(len(ser_2)):
            if ser_1[i] == ser_2[j]:
                positions_list.append(j)
                
    return positions_list

print(positions_shared(ser_1, ser_2))

# Teacher's solution
# result = []
# for elemento in ser_2:
#   try:
#       indice = pd.Index(ser_1).get_loc(elemento)

#   except KeyError as error:
#       print('Item not found!', error, sep='\n\n')      

#   else:
#       result.append(indice)
