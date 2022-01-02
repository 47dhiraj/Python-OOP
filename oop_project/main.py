class Library:
    original_books = []
    def __init__(self, originalBooks ,listOfBooks):                    # constructor
        self.books = listOfBooks                        # listOfBooks chai auta list ho jaha books haru huncha
        Library.original_books = originalBooks

    def displayAvailableBooks(self):                    # just auta void function ho which doesn't return anything
        print("Books present in this library are: ")
        for book in self.books:                         # list ma for loop lagayeko.
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)                 # user le request gareko book lai books list batw remove gareko.
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        if bookName in Library.original_books:
            if bookName in self.books:
                print(f"Oops ! you haven't borrowed {bookName}. No worry of returning it. Thanks !")
            else:
                self.books.append(bookName)                     # user le return gareko book lai books list ma append gareko.
                print(f"Thanks for returning {bookName}. Hope you enjoyed reading it. Have a great day ahead!")
        else:
            print(f'Invalid returning of the {bookName}. This book has never been in our library.')

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book                                # self.book vannale string ho jasma auta book ko naam cha.


    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book                                # self.book vannale string ho jasma auta book ko naam cha.





if __name__ == "__main__":
    originalBooks = ["Algorithms", "Django", "Clrs", "Python Notes"]

    listOfBooks = []
    for book in originalBooks:
        listOfBooks.append(book)


    centraLibrary = Library(originalBooks, listOfBooks)       # creating a Library object(i.e centraLibrary) and calling the constructor of Library class.

    student = Student()                                                             # creating a student object

    # centraLibrary.displayAvailableBooks()
    while (True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)

        try:
            a = int(input("Enter a choice: "))

            if a == 1:
                centraLibrary.displayAvailableBooks()               # centraLibrary object le displayAvailableBooks() vanni method lai call gareko cha
            elif a == 2:
                centraLibrary.borrowBook(student.requestBook())     # sabai vanda pahila student object le requestBook() vanni method lai call garcha & yaha user le request gareko book return vayera aaucha ,,, and again tyo book as a parameter liyera Library class ko borrowBook() vanni method call huncha
            elif a == 3:
                centraLibrary.returnBook(student.returnBook())      # sabai vanda pahila student object le returnBook() vanni method lai call garcha & yaha user le return garna lageko book return vayera aaucha ,,, and again tyo book as a parameter liyera Library class ko returnBook() vanni method call huncha
            elif a == 4:
                print("Thanks for choosing Central Library. Have a great day ahead!")
                exit()                  # exit() le program lai terminate garcha.
            else:
                print("Invalid Choice! Please Choose from 1 to 4 .")

        except ValueError as e:
            print('Oops!  That was no valid number choice. Please Choose again.')
