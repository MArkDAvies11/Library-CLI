from models import Author, Book, Genre, session
import sys

def display_main_menu():
    print("\n--- Main Menu ---")
    print("1. Manage Authors")
    print("2. Manage Books")
    print("3. Manage Genres")
    print("4. Exit")
    return input("Enter your choice: ")

def display_author_menu():
    print("\n--- Author Management ---")
    print("1. Create new author")
    print("2. View all authors")
    print("3. Find author by ID")
    print("4. Find author by name")
    print("5. View an author's books")
    print("6. Delete an author")
    print("7. Back to main menu")
    return input("Enter your choice: ")

def display_book_menu():
    print("\n--- Book Management ---")
    print("1. Create new book")
    print("2. View all books")
    print("3. Find book by ID")
    print("4. Find book by title")
    print("5. Delete a book")
    print("6. Back to main menu")
    return input("Enter your choice: ")

def display_genre_menu():
    print("\n--- Genre Management ---")
    print("1. Create new genre")
    print("2. View all genres")
    print("3. Find genre by ID")
    print("4. Find genre by name")
    print("5. Delete a genre")
    print("6. Back to main menu")
    return input("Enter your choice: ")

# Author CLI functions
def create_author_cli():
    name = input("Enter author name: ")
    Author.create(name)

def view_all_authors_cli():
    authors = Author.get_all()
    if not authors:
        print("No authors found.")
    else:
        print("\n--- All Authors ---")
        for author in authors:
            print(f"ID: {author.id}, Name: {author.name}")

def find_author_by_id_cli():
    try:
        author_id = int(input("Enter author ID: "))
        author = Author.find_by_id(author_id)
        if author:
            print(f"ID: {author.id}, Name: {author.name}")
        else:
            print("Author not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def find_author_by_name_cli():
    name = input("Enter author name: ")
    author = Author.find_by_name(name)
    if author:
        print(f"ID: {author.id}, Name: {author.name}")
    else:
        print("Author not found.")

def view_author_books_cli():
    try:
        author_id = int(input("Enter author ID: "))
        author = Author.find_by_id(author_id)
        if author:
            print(f"\n--- Books by {author.name} ---")
            for book in author.books:
                genres_list = ", ".join([g.name for g in book.genres])
                print(f"ID: {book.id}, Title: {book.title}, Genres: [{genres_list}]")
        else:
            print("Author not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_author_cli():
    try:
        author_id = int(input("Enter author ID to delete: "))
        author = Author.find_by_id(author_id)
        if author:
            author.delete()
        else:
            print("Author not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Book CLI functions
def create_book_cli():
    title = input("Enter book title: ")
    try:
        author_id = int(input("Enter author ID for the book: "))
        view_all_genres_cli()
        genre_input = input("Enter genre IDs (comma-separated, e.g., 1,2): ")
        genre_ids = [int(id) for id in genre_input.split(',') if id.strip()]
        
        Book.create(title, author_id, genre_ids)
    except ValueError:
        print("Invalid input. Please enter a number for the author ID and comma-separated numbers for genre IDs.")

def view_all_books_cli():
    books = Book.get_all()
    if not books:
        print("No books found.")
    else:
        print("\n--- All Books ---")
        for book in books:
            author_name = book.author.name if book.author else "Unknown"
            genres_list = ", ".join([g.name for g in book.genres])
            print(f"ID: {book.id}, Title: {book.title}, Author: {author_name}, Genres: [{genres_list}]")

def find_book_by_id_cli():
    try:
        book_id = int(input("Enter book ID: "))
        book = Book.find_by_id(book_id)
        if book:
            author_name = book.author.name if book.author else "Unknown"
            genres_list = ", ".join([g.name for g in book.genres])
            print(f"ID: {book.id}, Title: {book.title}, Author: {author_name}, Genres: [{genres_list}]")
        else:
            print("Book not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def find_book_by_title_cli():
    title = input("Enter book title: ")
    book = Book.find_by_title(title)
    if book:
        author_name = book.author.name if book.author else "Unknown"
        genres_list = ", ".join([g.name for g in book.genres])
        print(f"ID: {book.id}, Title: {book.title}, Author: {author_name}, Genres: [{genres_list}]")
    else:
        print("Book not found.")

def delete_book_cli():
    try:
        book_id = int(input("Enter book ID to delete: "))
        book = Book.find_by_id(book_id)
        if book:
            book.delete()
        else:
            print("Book not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Genre CLI functions
def create_genre_cli():
    name = input("Enter genre name: ")
    Genre.create(name)

def view_all_genres_cli():
    genres = Genre.get_all()
    if not genres:
        print("No genres found.")
    else:
        print("\n--- All Genres ---")
        for genre in genres:
            print(f"ID: {genre.id}, Name: {genre.name}")

def find_genre_by_id_cli():
    try:
        genre_id = int(input("Enter genre ID: "))
        genre = Genre.find_by_id(genre_id)
        if genre:
            print(f"ID: {genre.id}, Name: {genre.name}")
        else:
            print("Genre not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def find_genre_by_name_cli():
    name = input("Enter genre name: ")
    genre = Genre.find_by_name(name)
    if genre:
        print(f"ID: {genre.id}, Name: {genre.name}")
    else:
        print("Genre not found.")

def delete_genre_cli():
    try:
        genre_id = int(input("Enter genre ID to delete: "))
        genre = Genre.find_by_id(genre_id)
        if genre:
            genre.delete()
        else:
            print("Genre not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")