from models.library import Library
from models.book import Book
from exceptions import BookNotFoundError, MemberNotFoundError


def show_menu():
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Register Member")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")
    print("===============================================")


def main():
    library = Library("SMIU")

    # Load existing data when program starts
    library.load_library_data()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                # Register Member
                name = input("Enter member name: ")
                member = library.register_member(name)
                print(
                    f"\nMember ID: {member.ID}"
                    f"\nName: {member.name}"
                )

            elif choice == "2":
                # Add Book
                title = input("Enter book title: ")
                author = input("Enter book author: ")

                book = Book(title, author)
                library.add_book(book)
                print(
                    f"Book added successfully!"
                    f"\nTitle: {book.title}"
                )

            elif choice == "3":
                # Search Book
                title = input("Enter book title to search: ")

                library.search_book(title)

            elif choice == "4":
                # Display Books
                library.display_books()

            elif choice == "5":
                # Borrow Book
                member_id = int(input("Enter Member ID: "))
                book_id = int(input("Enter Book ID: "))

                library.borrow_book(member_id, book_id)
                print("Book borrowed successfully!")

            elif choice == "6":
                # Return Book
                member_id = int(input("Enter Member ID: "))
                book_id = int(input("Enter Book ID: "))

                library.return_book(member_id, book_id)
                print("Book returned successfully!")

            elif choice == "7":
                # Save and Exit
                library.save_library_data()
                print("Library data saved successfully.")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 8.")

        except ValueError:
            print("Please enter a valid number.")

        except (BookNotFoundError, MemberNotFoundError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()