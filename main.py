# LIBRARY PROJECT :

from Book import Book
from library import User

lib = User()

book1 = Book("legend", 'nagib', 12, 5, 7)
book2 = Book("love", 'ahmed', 12, 5, 6)
book3 = Book("trees", 'mousa', 12, 5, 15)
book4 = Book("Work", 'donia', 5, 2, 15)

lib.add_Book(book1)
lib.add_Book(book2)
lib.add_Book(book3)
lib.add_Book(book4)

# to detect added books :
for book in lib.Book:
    print('title :', book.title, '   author :', book.Author, '    num_of_copies_available :', book.Num_of_copies_available, '   num_of_copies_borrowed :', book.Num_of_copies_borrowed, '   total copies :', book.Total_n_of_copies)



# lib.Remove_book(book2.id)

# to detect removed books :
# for book in lib.Book:
#     print('title :', book.title, '   author :', book.Author, '    num_of_copies_available :', book.Num_of_copies_available, '   num_of_copies_borrowed :', book.Num_of_copies_borrowed, '   total copies :', book.Total_n_of_copies)


lib.Search_book(book3.id)
lib.return_book(book1.id)
lib.Borrow_book(book3.id)
