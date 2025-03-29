from main import Book

'''
В нас є список обʼєктів Book, потрібно написати код, який буде приймати book та видаляти усі схожі
'''

def remove_book_from_list(book_list: list[Book], book: Book):
    # for list_book in book_list:
    #     if list_book == book:
    #         book_list.remove(list_book)
    book_list.remove(book)

def remove_book_from_list_alternative(book_list: list[Book], book: Book):
    for list_book in book_list:
        # list_book_str = list_book.title + list_book.author + list_book.publishing_year + list_book.pages
        # book_str = book.title + book.author + book.publishing_year + book.pages
        if list_book.__dict__ == book.__dict__:
            book_list.remove(list_book)

book_list = [Book("The Hobbit", "J.R.R Tolkien", 1960, 300), Book("The Hobbit", "J.R.R Tolkien", 1960, 300), Book("The Hobbit", "J.R.R Tolkien", 1960, 300)]

remove_book_from_list(book_list, Book("The Hobbit", "J.R.R Tolkien", 1960, 300))
remove_book_from_list(book_list, Book("The Hobbit", "J.R.R Tolkien", 1960, 300))
remove_book_from_list(book_list, Book("The Hobbit", "J.R.R Tolkien", 1960, 300))

print(book_list)
# book_one = Book("The Hobbit", "J.R.R Tolkien", 1960, 300)
# print(dir(book_one))
# print(book_one.__dict__)

# book_two = Book("The Hobbit", "J.R.R Tolkien", 1960, 300)

# print(book_one)
# print(book_two)
# print(book_one == book_two)


