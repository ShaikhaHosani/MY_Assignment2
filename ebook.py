 # This is a class that represent an e book

class Ebook: 

    # Constructor to initialize e book properties

    def __init__(self, title, author, publication_date, genre, price, isbn, description=""):
        # Title of the book
        self._title = title  
        # Author of the book
        self._author = author  
        # When the book was published
        self._publication_date = publication_date  
        # Genre of the book
        self._genre = genre  
        # Price of the e-book
        self._price = price  
        # ISBN for the book
        self._isbn = isbn  
        # Description of the book
        self._description = description  

    # Getter for title
    def get_title(self):  
        # Return the title
        return self._title  

    # Getter for author
    def get_author(self):  
        # Return the author
        return self._author  

    # Getter for publication date
    def get_publication_date(self):  
        # Return the publication date
        return self._publication_date  

    # Getter for genre
    def get_genre(self):  
        # Return the genre
        return self._genre  

    # Getter for price
    def get_price(self):  
        # Return the price
        return self._price  

    # Getter for ISBN
    def get_isbn(self):  
        # Return the ISBN
        return self._isbn  

    # Getter for description
    def get_description(self):  
        # Return the description
        return self._description  

    # Setter for price
    def set_price(self, price: float):  
        # Check if price is non negative
        if price >= 0:  
            # Update the price
            self._price = price  

    # Setter for description
    def set_description(self, description: str):  
        # Update the description
        self._description = description  

    # Return e book
    def __str__(self):  
        return ("Title: " + self._title + "\n" +  # Title
                "Author: " + self._author + "\n" +  # Author
                "Genre: " + self._genre + "\n" +  # Genre
                "ISBN: " + self._isbn + "\n" +  # ISBN
                "Price: $" + str(self._price) + "\n" +  # Price
                "Published: " + self._publication_date)  # Publication date
