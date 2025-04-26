#Library Management System Project
#Library Management System keeps track of the books present in the library.It is an important piece of software which should be present in school and colleges.

book_list = list()

#items
menu = """ 
1) Add Book
2) Remove Book
3) View Book
4) Press E to Exit
"""

def add_book(booklist, book):
    book_list.append(book)
    print("Book added Successfully")

def remove_book(booklist, book):
    if book in book_list:
        book_list.remove(book)
        print("Book remove Successfully")   

    else:
        print("book not found in this list.")

#Display all the book result
def display_book(booklist):
    if book_list:
        print("Book added ->", " ,".join(book_list))

    else:
            print("No book in the list")

#Exit programme
def exit_function():
    print("Thank you for visiting Library Management System.")

#Main programme loop
while True:
    print(menu)
    choice = input("Enter your choice: ")

    if choice == '1':
        book_name = input("Enter your book name you want to add: ")
        add_book(book_list, book_name) 

    elif choice == '2':
        book_name = input("Enter a book name you want to remove: ")
        remove_book(book_list, book_name)

    elif choice == '3':
        display_book(book_list)

    elif choice.lower() == 'e': #Exit programme
         exit_function()

    else:
        print("Invalid entry")
        print("Press enter for the main menu.")





