class Book:

    __id_Book = 0  # class attribute

    def __init__(self, title,  Author, Num_of_copies_available, Num_of_copies_borrowed, Total_n_of_copies ):

        Book.__id_Book += 1

        self.id = Book.__id_Book

        self.title = title
        self.Author = Author
        self.Num_of_copies_available = Num_of_copies_available
        self.Num_of_copies_borrowed = Num_of_copies_borrowed
        self.Total_n_of_copies = Total_n_of_copies
