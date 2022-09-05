import pandas as pd

indices = ['ET', 'Klonoa', 'Ookami', 'Dead by daylight', 'Minecraft']
colunas = ['Lançamento', 'Unidades vendidas', 'Nota']
dados = [[1982, 2600000, 6.0], [2000, 1, 10.0], [2007, 600000, 9.5], [2016, 3000000, 7.5], [2011, 200000000, 4.0]]

df_2022 = pd.DataFrame(dados, index = indices, columns = colunas)
print('Dataframe: ', df_2022, sep = '\n')

print('\n', ':) '*42, '\n')

print('Lançamento: ', df_2022['Lançamento'], type(df_2022['Lançamento']), '\n', sep = '\n')
# A dataframe is made out of many series with a shared index

print('Lançamento: ', df_2022.Lançamento, type(df_2022.Lançamento), '\n', sep = '\n')

print('Lançamento: ', df_2022[['Lançamento', 'Unidades vendidas']], type(df_2022[['Lançamento', 'Unidades vendidas']]), '\n', sep = '\n')

print('ET: ')
print(df_2022.loc['ET'], type(df_2022.loc['ET']), '\n', sep = '\n')

print(df_2022.loc[['ET', 'Klonoa']][['Lançamento', 'Nota']], type(df_2022.loc[['ET', 'Klonoa']][['Lançamento', 'Nota']]), '\n', sep = '\n')

print(df_2022.iloc[[0, 3]][['Lançamento', 'Nota']], type(df_2022.iloc[[0, 3]][['Lançamento', 'Nota']]), '\n', sep = '\n')

print(df_2022.loc[['ET', 'Klonoa'], ['Lançamento', 'Nota']], type(df_2022.loc[['ET', 'Klonoa'], ['Lançamento', 'Nota']]), '\n', sep = '\n')

print('Colunas: ', df_2022.columns, df_2022.columns.values, type(df_2022.columns.values), df_2022.columns[0], '\n', sep = '\n')

print('Índice: ', df_2022.index, df_2022.index.values, type(df_2022.index.values), df_2022.index[0], '\n', sep = '\n')
