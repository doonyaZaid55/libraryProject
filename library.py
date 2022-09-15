class User:

    Book = []

    def add_Book(self, book):
        self.Book.append(book)     # BOOK => List , book => object



    def Remove_book(self, id):
        for book in self.Book:
            if book.id == id:
                self.Book.remove(book)

                return
        print("Book with id :", id, "is not found.")



    def Search_book(self, id):
        for book in self.Book:
            if book.id == id:
                # print('title :', book.title, '   author :', book.Author, '    num_of_copies_available :',
                #       book.Num_of_copies_available, '   num_of_copies_borrowed :', book.Num_of_copies_borrowed,
                #       '   total copies :', book.Total_n_of_copies)

                print("Book with id :", id, "information.")
                print("Title :", book.title)
                print("Author :", book.Author)
                print("Number of copies available :", book.Num_of_copies_available)
                print("Number of copies borrowed :", book.Num_of_copies_borrowed)
                print("Total number of copies", book.Total_n_of_copies)

                return
        print("Book with id :", id, "is not found")

        print('-' * 50)


    def Borrow_book(self, id):
        for book in self.Book:
            if book.id == id:
                print("Book with id:", id, "has been borrowed.")
                print("Wish you the best  ")
            else:
                pass

        print('-' * 50)




    def return_book(self, id):
        for book in self.Book:
            if book.id == id:

                print("Book with id :", id, "is returned (:")
                print("Thanks for your honesty ..")

            else:
                pass

        print('-' * 50)

