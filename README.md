# Library-CLI
Library Management CLI
This is a command-line interface (CLI) for managing a library's book, author, and genre data. It uses SQLAlchemy for object-relational mapping (ORM) and Alembic for database migrations.

Features
Author Management: Create, view, find, and delete authors.

Book Management: Create, view, find, and delete books.

Genre Management: Create, view, find, and delete genres.

Relationships: Connect books to authors and multiple genres.

Installation
To get the project up and running, follow these steps:

Clone the repository:

Bash

git clone https://github.com/mark-davies/Library-CLI.git
cd Library-CLI
Set up the virtual environment with Pipenv:

Bash

pipenv install
pipenv shell
Run migrations to create the database tables:

Bash

alembic upgrade head
Usage
Start the application:
From your project's root directory, and with your pipenv shell active, run the main script.

Bash

python -m lib.cli
Navigate the menus:
The CLI will present a main menu with options to manage authors, books, and genres. Follow the prompts to interact with your data.

Data Model
The application's data is organized using a relational database with three main tables and a fourth association table to handle a many-to-many relationship.

authors table: Stores information about authors. Each author can be associated with multiple books.

books table: Stores information about books. Each book is associated with one author and one or more genres.

genres table: Stores information about book genres. Each genre can be associated with multiple books.

book_genre_association table: A join table that connects books and genres to establish a many-to-many relationship.