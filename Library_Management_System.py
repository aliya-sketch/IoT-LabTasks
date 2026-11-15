# LIBRARY MANAGEMENT SYSTEM

print("LIBRARY MANAGEMENT SYSTEM")
print("========================================")
print("Welcome to Library Management System!")


class Library:
    def __init__(self):
        # List to store all books
        self.books = []

        # List to store issued book records
        self.issued_books = []

    # 1. Add Book
    def add_book(self):
        print("\n--- ADD BOOK ---")

        book_id = input("Enter Book ID: ").strip()

        # Check whether Book ID already exists
        for book in self.books:
            if book["id"] == book_id:
                print("Error: Book ID already exists!")
                return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        try:
            quantity = int(input("Enter Quantity: "))
            if quantity <= 0:
                print("Error: Quantity must be greater than zero!")
                return
        except ValueError:
            print("Error: Please enter a valid number for quantity!")
            return

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "quantity": quantity
        }

        self.books.append(book)
        print("Book added successfully!")

    # 2. View All Books
    def view_all_books(self):
        print("\n--- ALL BOOKS ---")

        if len(self.books) == 0:
            print("No books available!")
            return

        for book in self.books:
            print("--------------------")
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Quantity:", book["quantity"])

    # 3. Search Book
    def search_book(self):
        print("\n--- SEARCH BOOK ---")
        book_id = input("Enter Book ID to search: ").strip()

        for book in self.books:
            if book["id"] == book_id:
                print("Book Found!")
                print("Book ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Quantity:", book["quantity"])
                return

        print("Error: Book not found!")

    # 4. Issue Book
    def issue_book(self):
        print("\n--- ISSUE BOOK ---")
        book_id = input("Enter Book ID: ").strip()
        student_name = input("Enter Student Name: ").strip()

        for book in self.books:
            if book["id"] == book_id:
                if book["quantity"] > 0:
                    issue_record = {
                        "id": book["id"],
                        "title": book["title"],
                        "student": student_name
                    }

                    self.issued_books.append(issue_record)
                    book["quantity"] -= 1
                    print("Book issued successfully!")
                else:
                    print("Error: Book is not available!")
                return

        print("Error: Book not found!")

    # 5. Return Book
    def return_book(self):
        print("\n--- RETURN BOOK ---")
        book_id = input("Enter Book ID: ").strip()
        student_name = input("Enter Student Name: ").strip()

        for record in self.issued_books:
            if record["id"] == book_id and record["student"].lower() == student_name.lower():
                self.issued_books.remove(record)

                for book in self.books:
                    if book["id"] == book_id:
                        book["quantity"] += 1
                        break

                print("Book returned successfully!")
                return

        print("Error: Issued book or student record not found!")

    # 6. Delete Book
    def delete_book(self):
        print("\n--- DELETE BOOK ---")
        book_id = input("Enter Book ID to delete: ").strip()

        for book in self.books:
            if book["id"] == book_id:
                # Do not delete a book that is currently issued
                for record in self.issued_books:
                    if record["id"] == book_id:
                        print("Error: This book is currently issued!")
                        return

                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Error: Book not found!")

    # 7. View Issued Books
    def view_issued_books(self):
        print("\n--- ISSUED BOOKS ---")

        if len(self.issued_books) == 0:
            print("No books are currently issued!")
            return

        for record in self.issued_books:
            print("--------------------")
            print("Book ID:", record["id"])
            print("Book Title:", record["title"])
            print("Student Name:", record["student"])

    # 8. Exit
    def exit_system(self):
        print("Thank you for using Library Management System!")
        print("Program closed successfully.")


# Create Library object
library = Library()

# Main Menu
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")
    print("================================")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.view_all_books()
    elif choice == "3":
        library.search_book()
    elif choice == "4":
        library.issue_book()
    elif choice == "5":
        library.return_book()
    elif choice == "6":
        library.delete_book()
    elif choice == "7":
        library.view_issued_books()
    elif choice == "8":
        library.exit_system()
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 8.")
