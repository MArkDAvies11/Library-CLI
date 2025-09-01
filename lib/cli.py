import sys
from lib.helpers import (
    display_main_menu,
    display_author_menu,
    display_book_menu,
    display_genre_menu, # New import
    create_author_cli,
    view_all_authors_cli,
    find_author_by_id_cli,
    find_author_by_name_cli,
    view_author_books_cli,
    delete_author_cli,
    create_book_cli,
    view_all_books_cli,
    find_book_by_id_cli,
    find_book_by_title_cli,
    delete_book_cli,
    create_genre_cli, # New import
    view_all_genres_cli, # New import
    find_genre_by_id_cli, # New import
    find_genre_by_name_cli, # New import
    delete_genre_cli # New import
)

def main():
    print("Welcome to the Library Management System!")
    while True:
        choice = display_main_menu()
        if choice == '1':
            manage_authors()
        elif choice == '2':
            manage_books()
        elif choice == '3': # New menu option
            manage_genres()
        elif choice == '4':
            print("Exiting application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def manage_authors():
    while True:
        choice = display_author_menu()
        if choice == '1':
            create_author_cli()
        elif choice == '2':
            view_all_authors_cli()
        elif choice == '3':
            find_author_by_id_cli()
        elif choice == '4':
            find_author_by_name_cli()
        elif choice == '5':
            view_author_books_cli()
        elif choice == '6':
            delete_author_cli()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_books():
    while True:
        choice = display_book_menu()
        if choice == '1':
            create_book_cli()
        elif choice == '2':
            view_all_books_cli()
        elif choice == '3':
            find_book_by_id_cli()
        elif choice == '4':
            find_book_by_title_cli()
        elif choice == '5':
            delete_book_cli()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
            
# New: `manage_genres` function
def manage_genres():
    while True:
        choice = display_genre_menu()
        if choice == '1':
            create_genre_cli()
        elif choice == '2':
            view_all_genres_cli()
        elif choice == '3':
            find_genre_by_id_cli()
        elif choice == '4':
            find_genre_by_name_cli()
        elif choice == '5':
            delete_genre_cli()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()