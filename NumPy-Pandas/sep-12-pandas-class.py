import pandas as pd

indices = ['ET', 'Klonoa', 'Ookami', 'Dead by daylight', 'Minecraft']
colunas = ['Lançamento', 'Unidades vendidas', 'Nota']
dados = [[1982, 2600000, 6.0], [2000, 1, 10.0], [2007, 600000, 9.5], [2016, 3000000, 7.5], [2011, 200000000, 4.0]]

df_2022 = pd.DataFrame(dados, index = indices, columns = colunas)
print('Dataframe: ', df_2022, sep = '\n')

print('Selection: ')
print(df_2022['Nota'])
print(df_2022.Nota)
print(df_2022[['Nota', 'Lançamento']])
print(df_2022.loc[['ET', 'Klonoa']])
print(df_2022.iloc[[0, 1]])
print(df_2022.loc[['ET', 'Klonoa'], ['Lançamento', 'Nota']])
print(df_2022.loc[:, ['Lançamento', 'Nota']])
print(df_2022.iloc[2:4, [0, 2]])

df_2022['Extra Column'] = df_2022['Nota'] + df_2022['Unidades vendidas']
print(df_2022)

df_2022 = df_2022.drop('Extra Column', axis = 1)
print(df_2022)

df_2022.drop('ET', inplace = True)
print(df_2022)

print(df_2022['Nota']>5)
print(df_2022[df_2022['Nota']>5])
print(df_2022[df_2022['Nota']>5][['Lançamento', 'Unidades vendidas']])
print(df_2022[(df_2022['Nota']>5) & (df_2022['Lançamento'] > 2000)], '\n\n')

print('Multi-Index', '\n')
plataforma = ['CrunchyRoll', 'CrunchyRoll', 'Netflix', 'Netflix']
ano = [2020, 2021, 2020, 2021]
indices = pd.MultiIndex.from_arrays([plataforma, ano], names = ('Plataforma', 'Year'))
print(indices)

df_2022.reset_index(inplace=True)
print(df_2022)

df_2022.rename(columns = {'index' : 'Nome', 'Nota': 'Avaliação'}, inplace = True)
print(df_2022)

df_2022.iloc[1, 1] = 2008
print(df_2022)

df_2022.set_index(indices, inplace = True)
print(df_2022)

print(df_2022.loc['CrunchyRoll'])
print(df_2022.loc['CrunchyRoll'].loc[2020])

print('Cross Selection')
print(df_2022.xs('CrunchyRoll'), '\n\n')
print(df_2022.xs(['CrunchyRoll', 2020]), '\n\n')
print(df_2022.xs(('CrunchyRoll', 2020)), '\n\n')
print(df_2022.xs(2020, level = 'Year'), '\n\n')

print(df_2022.head(2), '\n\n')
print(df_2022.tail(2), '\n\n')
print(df_2022['Lançamento'].unique(), '\n\n')
print(df_2022['Lançamento'].nunique(), '\n\n')
print(df_2022['Lançamento'].count(), '\n\n')
print(df_2022['Lançamento'].value_counts(), '\n\n')

print(df_2022.T, '\n\n')
print(df_2022, '\n\n')
df_2022.at[('CrunchyRoll', 2021), 'Avaliação'] = 5
print(df_2022)