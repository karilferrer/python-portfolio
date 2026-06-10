books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")

    books.append({
        'title' : title,
        'author' : author,
        'available' : True
    })

    print("Book added successfully!")

def view_book():
    if len(books) == 0:
        print("No books found.")
        return
    
    print("==== BOOK LIST ====")

    for i in books:
        print(f"Title: {i['title']}")
        print(f"Author: {i['author']}")
        if i['available'] == True:
            print("Status: Available\n")
        
        else:
            print("Status Borrowed\n")



def search_book():
    book_title = input("Enter book title: ")

    for book in books:
        if book['title'].lower() == book_title.lower():

            print("Book Found!")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")

            if book['available']:
                print("Status: Available")
            else:
                print("Status: Borrowed")

            return

    print("Book not found.")

       
def borrow_book():
    borrow_title = input("Enter book title to borrow: ")

    for book in books:
        if book['title'].lower() == borrow_title.lower():

            if book['available']:
                book['available'] = False
                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed.")

            return

    print("Book not found.")



def return_book():
    return_title = input("Enter book title to return: ")

    for book in books:
        if book['title'].lower() == return_title.lower():

            if not book['available']:
                book['available'] = True
                print("Book returned successfully!")
            else:
                print("Book is already available.")

            return

    print("Book not found.")

while True:

    print("==== LIBRARY MANAGEMENT SYSTEM ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":
        add_book()
        

    elif choice == "2":
        view_book()
        

    elif choice == "3":
        search_book()
        
    
    elif choice == "4":
        borrow_book()
        

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("\nGoodbye!")
        
        
    else:
        print("Invalid choice. Please try again.")