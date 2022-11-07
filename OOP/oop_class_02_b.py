from oop_class_02_a import Movie

movie_a = Movie('Back to the Future', 1985, 'Very Nice')
movie_b = Movie('Back to the Future: Part 2', 1989)
movie_c = Movie('Back to the Future', 1985, 'Very Nice')

print(movie_a == movie_c, '\n')
print(id(movie_a), '\n')
print(id(movie_c), '\n')
print(type(movie_a), '\n')

#del movie_a

print(movie_a.title, '\n')
print(movie_a.year, '\n')
print(movie_a.type, '\n')
print(Movie.type, '\n')
print(Movie.get_type(), '\n\n', ':) '*42, '\n', sep = '')

movie_a.type = 'movie'
print(movie_a.type, '\n')
print(type(movie_a), '\n')
print(Movie.type, '\n')

movie_a.director = 'Robert'
print(movie_a.director, '\n')
print(type(movie_a), '\n')
#print(Movie.director, '\n')
del movie_a.director
#print(movie_a.director, '\n')

movie_a.tell_synopsis()

print(movie_a)

movie_a.year = 1800