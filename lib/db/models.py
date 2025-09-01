from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Database setup
engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define the many-to-many join table for Book and Genre
book_genre_association = Table(
    'book_genre_association',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', back_populates='author', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

    @classmethod
    def create(cls, name):
        if not name or not isinstance(name, str) or len(name) < 2:
            print("Error: Author name must be a non-empty string of at least 2 characters.")
            return None
        try:
            author = cls(name=name)
            session.add(author)
            session.commit()
            print(f"Author '{name}' created successfully.")
            return author
        except Exception as e:
            session.rollback()
            print(f"Error creating author: {e}")
            return None

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, author_id):
        return session.query(cls).filter_by(id=author_id).first()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    def delete(self):
        session.delete(self)
        session.commit()
        print(f"Author '{self.name}' and all their books have been deleted.")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
    genres = relationship('Genre', secondary=book_genre_association, back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author_id={self.author_id})>"

    @classmethod
    def create(cls, title, author_id, genre_ids=[]):
        if not title or not isinstance(title, str) or len(title) < 1:
            print("Error: Book title must be a non-empty string.")
            return None
        try:
            author = session.query(Author).filter_by(id=author_id).first()
            if not author:
                print("Error: Invalid author ID. Book cannot be created.")
                return None
            genres = session.query(Genre).filter(Genre.id.in_(genre_ids)).all()
            if len(genres) != len(genre_ids):
                print("Error: One or more genre IDs are invalid.")
                return None
            book = cls(title=title, author_id=author_id, genres=genres)
            session.add(book)
            session.commit()
            print(f"Book '{title}' by '{author.name}' created with genres.")
            return book
        except Exception as e:
            session.rollback()
            print(f"Error creating book: {e}")
            return None

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, book_id):
        return session.query(cls).filter_by(id=book_id).first()

    @classmethod
    def find_by_title(cls, title):
        return session.query(cls).filter_by(title=title).first()

    def delete(self):
        session.delete(self)
        session.commit()
        print(f"Book '{self.title}' has been deleted.")

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', secondary=book_genre_association, back_populates='genres')

    def __repr__(self):
        return f"<Genre(id={self.id}, name='{self.name}')>"

    @classmethod
    def create(cls, name):
        if not name or not isinstance(name, str) or len(name) < 2:
            print("Error: Genre name must be a non-empty string of at least 2 characters.")
            return None
        try:
            genre = cls(name=name)
            session.add(genre)
            session.commit()
            print(f"Genre '{name}' created successfully.")
            return genre
        except Exception as e:
            session.rollback()
            print(f"Error creating genre: {e}")
            return None
            
    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, genre_id):
        return session.query(cls).filter_by(id=genre_id).first()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    def delete(self):
        session.delete(self)
        session.commit()
        print(f"Genre '{self.name}' has been deleted.")

# Drop all tables to start fresh before creating a new schema
# NOTE: This is for development only! Use Alembic for production migrations.
if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database schema created successfully.")