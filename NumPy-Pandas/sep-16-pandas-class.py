import pandas as pd

indices = ['Anime 1', 'Anime 2', 'Anime 3', 'Anime 4', 'Anime 5']
columns = ['Rating', 'Seasons', 'Episodes', 'Comment']
data = [[5, 5, 120, 'A'], [5, 3, 39, 'B'], [7, 2, 12, 'C'], [9, 50, 1200, 'D'], [3, 1, 10, 'E']]

df = pd.DataFrame(data, index = indices, columns = columns)

print(df, '\n\n')

platform = ['CrunchyRoll', 'CrunchyRoll', 'CrunchyRoll', 'Netflix', 'Netflix']
release = [2000, 2020, 2012, 2021, 2016]
new_indices = pd.MultiIndex.from_arrays([platform, release], names = ('Platform', 'Release Year'))

print(new_indices, '\n\n')

df.reset_index(inplace = True)
df.rename(columns = {'index' : 'Name'}, inplace = True)

print(df, '\n\n')

df.set_index(new_indices, inplace = True)

print(df, '\n\n')

print('Presenting by Platform:', df.groupby('Platform'), '\n', sep = '\n')

print('Presenting by Platform:', df.groupby('Platform').min(), '\n', sep = '\n')
print('Presenting by Platform:', df.groupby('Platform').max()['Rating'], '\n', sep = '\n')
print('Presenting by Platform:', df.groupby('Platform')['Rating'].max(), '\n', sep = '\n')
print('Presenting by Platform:', df.groupby('Platform').max()['Rating'].max(), '\n', sep = '\n')
print('Presenting by Platform:', df.groupby('Platform').std(), '\n', sep = '\n')