import pandas as pd
import numpy as np

indices = ['ET', 'Klonoa', 'Ookami', 'Dead by daylight', 'Minecraft']
colunas = ['Lançamento', 'Unidades vendidas', 'Nota']
dados = [[1982, 2600000, 6.0], [2000, 1, 10.0], [2007, 600000, 9.5], [2016, 3000000, 7.5], [2011, 200000000, 4.0]]

df = pd.DataFrame(dados, index = indices, columns = colunas)

print('Dataframe: ', df, sep = '\n')
print('\n', ':) '*42, '\n')

print(df.at['ET', 'Nota'])
print('\n', ':) '*42, '\n')

print(df['Nota'].min())
print('\n', ':) '*42, '\n')

print(df['Nota'].max())
print('\n', ':) '*42, '\n')

print(df['Nota'].median())
print('\n', ':) '*42, '\n')

print(df['Nota'].mean())
print('\n', ':) '*42, '\n')

# Valores Ausentes
indices = ['Student 1', 'Student 2', 'Student 3']
colunas = ['Name', 'Age', 'ID']
data = [['Aluninho', 15, 100], ['Aluno', 21, np.nan], ['Alunão', 18, 102]]

df = pd.DataFrame(data, index=indices, columns=colunas)

print(df)
print('\n', ':) '*42, '\n')

print(df.isnull())
print('\n', ':) '*42, '\n')

print(df[df['ID'].isnull()])
print('\n', ':) '*42, '\n')

print(df.notnull())
print('\n', ':) '*42, '\n')

print(df[df['ID'].notnull()])
print('\n', ':) '*42, '\n')

print(df.dropna(thresh=3))
print('\n', ':) '*42, '\n')

print(df.fillna(101))
print('\n', ':) '*42, '\n')

df = pd.read_csv('Polos_Nacionais_de_Agricultura_Irrigada.csv', encoding = 'latin_1')
print(df.head())
df.to_csv('PNAI.csv', index = False, encoding = 'latin_1')
