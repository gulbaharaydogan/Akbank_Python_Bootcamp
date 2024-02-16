class Library:
    def __init__(self, file_name):              #Constructor
        self.file_name = file_name
        self.file = None                        #Instead of using exception-handling we can easly stop when there is no file in __del__
        self.books = self.load_books()

    def load_books(self): 
        self.file = open(self.file_name, "r")   #Creating a file to read
        lines = self.file.read().splitlines()
        # self.file.close()

        books = []                              #Creating a list to store book details and read each line to create list element with splitting
        for line in lines:
            book_details = line.split(',')
            if len(book_details) >= 1:
                books.append(book_details)
        return books
    
    def save_books(self):                      
        self.file = open(self.file_name, "w")   #Creating a file to write also
        self.file.write('\n'.join([','.join(book) for book in self.books]))
        # self.file.close()

    def add_book(self, book):                   #Using inputs from user to add book to file with calling save_book()
        #title = book[0]
        self.books.append(book)
        self.save_books()

    def remove_book_by_title(self, title):      #Using inputs from user to delete book to file
        for book in self.books:
            if len(book) >= 1 and book[0] == title:
                self.books.remove(book)
                self.save_books()
                print(f"Deleted book: {title}")
                return
        print(f"Book {title} not found.")

    def list_books(self):                       
        for book_details in self.books:
            print(','.join(book_details))

    def __del__(self):                          #Destructor
        if self.file is not None:
            self.file.close()


def menu_action():
    print("\n***MENU***\n1)List\n2)Add Book\n3)Remove Book\n4)Quit (q)")
    print("Enter between (1-4)")
    return input("Enter your choice: ")

                                              ### Main program###
lib = Library("books.txt")

while True:
    action = menu_action()

    if action == '2':
        bTitle = input("Enter the book title: ")
        bAuthor = input("Enter the author: ")
        bRelease = input("Enter the release year: ")
        bPage = input("Enter the number of pages: ")

        book = [bTitle, bAuthor, bRelease, bPage]
        lib.add_book(book)
        print(f"Added to library: {book}")

    elif action == '1':
        print("Books that are in the library: \n")
        lib.list_books()

    elif action == '3':
        book_title_to_remove = input("Enter the title of the book to remove: ")

        # Remove the book from the library and update the file
        lib.remove_book_by_title(book_title_to_remove)

        # List the remaining books
        print("\nRemaining Books:")
        lib.list_books()

    elif action == '4' or action == 'q':
        print("Exiting the system.")
        exit()
