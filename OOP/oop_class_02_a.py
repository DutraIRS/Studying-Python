class Movie:
    type = 'audiovisual'
    
    @classmethod
    def get_type(cls):
        return cls.type
    
    def __init__(self, movie_title, year, synopsis=''):
        self.title = movie_title # name doesn't have to be the same
        self._year = year # underscore shows that the attribute should be treated as private
        self.synopsis = synopsis
        
    def __str__(self) -> str:
        return '{title} ({year})'.format(title = self.title, year = self.year)
        
    @property
    def year(self):
        print('Getter!')
        return self._year
    
    @year.setter
    def year(self, new_year):
        print('Setter!')
        if new_year >= 1878:
            self._year = new_year
        else:
            self._year = -1
            print('Invalid year!')
    
    def tell_synopsis(self):
        print('I\'m telling you my synopsis:', self.synopsis)