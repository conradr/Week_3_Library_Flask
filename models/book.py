class Book():
    def __init__(self, title, description, author, genre, checked_out, cover_url, urn):
        self.title = title
        self.description = description
        self.author = author
        self.genre = genre
        self.checked_out = checked_out
        self.cover_url = cover_url
        self.lent_to = []
        self.urn = urn
