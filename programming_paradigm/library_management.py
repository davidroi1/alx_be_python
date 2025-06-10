class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self._is_checked_out = 0

    def return_book(self) -> bool:
        return True


class Library:
    def __init__(self):
        self._books = [Book]

    def add_book(self, book):
        book._is_checked_out = 1
        self._books.append(book)
    
    def check_out_book(self, title):
        for el in range(1, len(self._books)):
            title_of = self._books[el].title
            if title_of == title:
                self._books[el]._is_checked_out = 0

    
    def return_book(self, title):
        for el in range(1, len(self._books)):
            title_of = self._books[el].title
            if title_of == title:
                self._books[el]._is_checked_out = 1
    
    def list_available_books(self):
        for book_ in range(1, len(self._books)):
            if self._books[book_]._is_checked_out:
                book_info = ''.join((self._books[book_].title,' by ', self._books[book_].author))
                print(book_info)