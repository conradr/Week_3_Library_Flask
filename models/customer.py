class Customer():
    def __init__(self, name, postcode, urn):
        self.name = name
        self.past_book_list = []
        self.postcode = postcode
        self.current_book_list = []
        self.urn = urn
