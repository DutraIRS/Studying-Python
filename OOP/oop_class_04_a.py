class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def show_books(self):
        for book in self.books:
            print(book)

    @property            
    def name(self):
        return self.__name
    
    @property            
    def books(self):
        return self.__books
    
    def __del__(self):
        print(f'The library {self.name} has been destroyed.')
        
    def __len__(self):
        return len(self.books)
    
    def __bool__(self):
        return len(self.books) > 0
    
    def __add__(self, other):
        for book in other.books:
            self.books.append(book)
            
    def __radd__(self, other):
        return other + len(self)