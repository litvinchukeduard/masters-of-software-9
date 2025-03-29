from dataclasses import dataclass
import random
'''
Створити структуру, яка дозволить керувати бібліотекою

- можливість створити випадклву книгу
'''

{
    "title": "The Hobbit",
    "author": "J.R.R Tolkien",
    "publishing_year": 1960
}

def print_book(book: dict):
    print(f'{book['title']} of {book['author']}')


titles = ["The Hobbit", "Lord of the Rings", "1984"]
authors = ["J.R.R Tolkien", 'J.R.R Martin']

def generate_random_book():
    title = random.choice(titles)
    author = random.choice(authors)
    publishing_year = random.randint(1950, 2025)
    return Book(title, author, publishing_year)

def generate_random_online_book():
    title = random.choice(titles)
    author = random.choice(authors)
    publishing_year = random.randint(1950, 2025)
    return OnlineBook(title, author, publishing_year)


class Book:
    def __init__(self, title: str, author: str, publishing_year: int, pages: int):
        print("Base constructor")
        self.title = title
        self.author = author
        Book.check_publishing_year(publishing_year)
        self.publishing_year = publishing_year
        self.pages = pages
        # self.page_marker = 200

    @staticmethod
    # @input_error
    def check_publishing_year(publishing_year):
        if (publishing_year > 2025):
            raise ValueError("Book is not published yet")
        
    @classmethod
    def generate_random_book(cls):
        title = random.choice(titles)
        author = random.choice(authors)
        publishing_year = random.randint(1950, 2025)
        return cls(title, author, publishing_year)

    # def
    def __str__(self) -> str:
        return f'{self.title} by {self.author} {self.__class__}'
    
    def __eq__(self, value):
        if not isinstance(value, Book):
            return False
        return self.title == value.title and self.author == value.author and self.pages == self.pages
        # return self.__dict__ == value.__dict__

    def __repr__(self):
        return str(self)

    def print_book_info(self):
        print(f'{self.title} by {self.author}')


class OnlineBook(Book):
    def get_web_page(self):
        return f'www.example.com/book/{self.title}'

# @dataclass
# class AudioBook(Book):
#     title: str
#     author: str
#     publishing_year: int
#     length: int

class AudioBook(Book):
    def __init__(self, title, author, publishing_year, pages, length):
        self.length = length
        super().__init__(title, author, publishing_year, pages)

@dataclass(frozen=True)
class DataBook:
    title: str
    author: str
    publishing_year: int

    # def __init__

    def __post_init__(self):
        if self.publishing_year > 2025:
            raise ValueError("Book is not published yet")
        
# AudioBook("The Hobbit", "J.R.R Tolkien", 1960, 180)

# hobbit_book = DataBook("The Hobbit", "J.R.R Tolkien", 1960)

# hobbit_book.author = 'J.R.R Martin'
# print(hobbit_book)

hobbit_book = Book("The Hobbit", "J.R.R Tolkien", 1960, 300)
hobbit_book_two = Book("The Hobbit", "J.R.R Tolkien", 1970, 300)

print(hobbit_book == hobbit_book_two)

# hobbit_book = Book("The Hobbit", "J.R.R Tolkien", 2027)
# print(generate_random_book())
# print(OnlineBook.generate_random_book())
# print(dir(hobbit_book))
# int, dict, str, set

# str_list = ["hello world", "hello people"]
# book_list = [Book("The Hobbit", "J.R.R Tolkien", 1960), Book("Lord of the Rings", "J.R.R Tolkien", 1970)]

# for my_str in str_list:
    # print(my_str)

# for book in book_list:
    # print(book)


