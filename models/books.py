from models.book import *

book1 = Book(
    "The Help",
    "Three ordinary women are about to take one extraordinary step.",
    "Kathryn Stockett",
    "Fiction",
    False,
    "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1622355533i/4667024.jpg",
    "the_help_kathryn_stockett"
)
book2 = Book(
    "To Kill a Mockingbird",
    "The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it.",
    "Harper Lee",
    "Classics",
    True,
    "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657.jpg",
    "to_kill_a_mocking_bird_harper_lee"
)

book3 = Book(
    "The Hunger Games",
    "Could you survive on your own in the wild, with every one out to make sure you don't live to see the morning?",
    "Suzanne Collins",
    "Young Adult",
    True,
    "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg",
    "the_hunger_games_suzanne_collins"
)
book4 = Book(
    "Harry Potter and the Sorcerer's Stone",
    "Harry Potter's life is miserable. His parents are dead and he's stuck with his heartless relatives, who force him to live in a tiny closet under the stairs.",
    "J.K Rowling",
    "Fantasy",
    False,
    "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1474154022i/3.jpg",
    "harry_potter_j_k_rowling"
)

book5 = Book(
    "The Lightning Thief",
    "Percy Jackson is a good kid, but he can't seem to focus on his schoolwork or control his temper. And lately, being away at boarding school is only getting worse - Percy could have sworn his pre-algebra teacher turned into a monster and tried to kill him.",
    "Rick Riordan",
    "Fantasy",
    False,
    "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1400602609i/28187.jpg",
    "the_lightning_thief_rick_riordan"
)

books = [book1, book2, book3, book4, book5]


def add_new_book(book):
    books.append(book)


def return_book_by_urn(book_urn):
    for book in books:
        if book.urn == book_urn:
            return book


def delete_book_by_urn(book_urn):
    book_to_delete = None
    book_to_delete = return_book_by_urn(book_urn)
    books.remove(book_to_delete)


def check_book_in_or_out(book_urn):
    book_to_check = None
    book_to_check = return_book_by_urn(book_urn)
    if book_to_check.checked_out == False:
        book_to_check.checked_out = True
    else:
        book_to_check.checked_out = False
