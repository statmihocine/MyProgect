class Book:
    def __init__(self,id_Book,title,author,year):
        self._id_Book=id_Book
        self.title=title
        self._author=author
        self.year=year
        self.available=True