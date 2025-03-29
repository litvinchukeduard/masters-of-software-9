'''
Створити структуру, яка дозволить керувати бібліотекою
'''

{
    "title": "The Hobbit",
    "author": "J.R.R Tolkien",
    "publishing_year": 1960
}

def print_book(book: dict):
    print(f'{book['title']} of {book['author']}')


class Book:
    def __init__(self, title: str, author: str, publishing_year: int):
        self.title = title
        self.author = author
        self.publishing_year = publishing_year

    def print_book_info(self):
        print(f'{self.title} of {self.author}')

hobbit_book = Book("The Hobbit", "J.R.R Tolkien", 1960)
# print(dir(hobbit_book))
# int, dict, str, set

str_list = ["hello world", "hello people"]
book_list = [Book("The Hobbit", "J.R.R Tolkien", 1960), Book("Lord of the Rings", "J.R.R Tolkien", 1970)]

for my_str in str_list:
    print(my_str)

for book in book_list:
    print(book)


