from oop_class_04_a import Library

library_a = Library('My Shelf')
library_a.add_book('Meditations')
library_a.add_book('Enchiridion')
library_a.add_book('Nicomachean Ethics')

library_a.show_books()
print(library_a.books)

library_b = Library('Your Shelf')
library_b.add_book('Linear Algebra')
library_b.add_book('Linear Algebra and Its Applications')
library_b.add_book('Introduction to Linear Algebra')

library_b.show_books()
print(library_b.books)

library_c = Library('Their Shelf')

library_c.show_books()
print(library_c.books)

print('\n:)\n')

print(len(library_a))
print(len(library_b))
print(len(library_c))

if library_a:
    print('Passed 1')
    
if library_b:
    print('Passed 2')
    
if library_c:
    print('Passed 3')
    
print('\n:)\n')

library_a + library_b

library_a.show_books()
print(3 + library_a)