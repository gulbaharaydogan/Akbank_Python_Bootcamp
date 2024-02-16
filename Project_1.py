class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
        self.books = self.load_books()

    def load_books(self):
        self.file = open(self.file_name, "r")
        lines = self.file.read().splitlines()
        #self.file.close()

        ''' Note to the mentors
    Firstly, I couldn't delete certain book with list so I used with dictionary
    After that, I rearranged and list is also worked but I want to share both file
     ''' 
        books = {}
        for line in lines:
            book_details = line.split(',')
            if len(book_details) >= 1:
                title = book_details[0]
                books[title] = line

        return books
        
    def save_books(self):
        self.file = open(self.file_name, "w")
        self.file.write('\n'.join(self.books.values()))
        #self.file.close()

    def add_book(self, book):
        title = book[0]
        self.books[title] = ','.join(book)
        self.save_books()

    def remove_book_by_title(self, title):
        if title in self.books:
            del self.books[title]
            self.save_books()
            print(f"Deleted book: {title}")
        else:
            print(f"Book {title} not found.")

    def list_books(self):
        for book_details in self.books.values():
            print(book_details)

    def __del__(self):
        if self.file is not None:
            self.file.close()

def greeting():
    print("\n***MENU***\n1)List\n2)Add Book\n3)Remove Book\n4)Quit (q)")
    print("Enter between (1-4)")
    return input("Enter your choice: ")

# Main program
lib = Library("books.txt")

while True:
    action = greeting()

    if action == '2':
        bTitle = input("Enter the book title: ")
        bAuthor = input("Enter the author: ")
        bRelease = input("Enter the release year: ")
        bPage = input("Enter the number of pages: ")

        book = [bTitle, bAuthor, bRelease, bPage]
        lib.add_book(book)
        print(f"Added to library: {book}")

    elif action == '1':
        print("Books that are in library: \n")
        for book_details in lib.books.values():
            book_info = book_details.split(',')

            if len(book_info) >= 1:
                print(f"Book: {book_info[0]}")

                if len(book_info) >= 2:
                    print(f"Author: {book_info[1]}")

                print()  # Add a newline between books
            else:
                print("Invalid format in the file. Please check.")

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
