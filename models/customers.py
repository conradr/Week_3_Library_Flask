from models.customer import *
from models.book import *

customer1 = Customer("Jack Burns", "EH68ES", "jack_burns_eh68es")
customer2 = Customer("Mary Marks", "EH45BY", "mary_marks_eh45by")
customer3 = Customer("Sarah Jones", "EH128BB", "sarah_jones_eh128bb")
customer4 = Customer("Farook Momed", "G16JJ", "farook_momed_g16jj")
customer5 = Customer("Penelope Marka", "BG879JJ", "penelope_marka_bg879jj")

customers = [customer1, customer2, customer3, customer4, customer5]


def add_book_to_customer(customer, book):
    customer.current_book_list.append(book)
    customer.past_book_list.append(book)
    book.lent_to.append(book)


def remove_book_from_customer(customer, book):
    customer.current_book_list.remove(book)
    book.lent_to.remove(book)
