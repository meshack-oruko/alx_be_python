class Book:
    """Represents a book with a title, author, and checkout status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    """Manages a collection of books and their availability."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f'"{title}" has been checked out.'
        return f'"{title}" is not available.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f'"{title}" has been returned.'
        return f'"{title}" was not checked out.'

    def list_available_books(self):
        available = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        return available if available else ["No books available."]
