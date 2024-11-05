from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice

# Bookstore class

class Bookstore:
    
    # Name of the bookstore
    def __init__(self, name):
        self.__name = name
        
        # E-book catalog dictionary
        self.__ebook_catalog = {} 
        
        # Customer dictionary
        self.__customers = {}     
        
        # Orders dictionary
        self.__orders = {}        
        
        # Active shopping carts dictionary
        self.__active_carts = {}   
    
    # Add an e book to the catalog
    def add_ebook(self, ebook):
        isbn = ebook.get_isbn()
        
        # Check if the e book is already in the catalog
        if isbn not in self.__ebook_catalog:
            self.__ebook_catalog[isbn] = ebook
            return True
        return False
        
    # Remove an e book from the catalog
    def remove_ebook(self, isbn):
        if isbn in self.__ebook_catalog:
            del self.__ebook_catalog[isbn]
            return True
        return False
        
    # Get an e book by its ISBN
    def get_ebook(self, isbn):
        return self.__ebook_catalog.get(isbn)
        
    # Update the price of an e book
    def update_ebook_price(self, isbn, new_price):
        if isbn in self.__ebook_catalog:
            self.__ebook_catalog[isbn].set_price(new_price)
            return True
        return False
        
    # Add a customer to the store
    def add_customer(self, customer):
        email = customer.get_email()
        
        # Check if the customer is already in the store
        if email not in self.__customers:
            self.__customers[email] = customer
            return True
        return False
        
    # Remove a customer from the store
    def remove_customer(self, email):
        if email in self.__customers:
            del self.__customers[email]
            return True
        return False
        
    # Get a customer by their email
    def get_customer(self, email):
        return self.__customers.get(email)
        
    # Create a shopping cart for a customer
    def create_cart(self, customer_email):
        customer = self.get_customer(customer_email)
        
        # Check if the customer exist and if they have no active cart
        if customer and customer_email not in self.__active_carts:
            self.__active_carts[customer_email] = ShoppingCart(customer)
            return self.__active_carts[customer_email]
        return None
        
    # Get the active shopping cart for a customer
    def get_cart(self, customer_email):
        return self.__active_carts.get(customer_email)
        
    # Create an order from a customer shopping cart
    def create_order(self, customer_email):
        cart = self.__active_carts.get(customer_email)
        
        # Check if the cart is empty or does not exist
        if not cart or not cart.get_items():
            return None, 
        
        customer = self.get_customer(customer_email)
        
        # Check if the customer exist
        if not customer:
            return None, "Customer not found"
        
        order = Order(customer, cart)
        
        # Store the order
        self.__orders[order.get_order_id()] = order
        
        # Create an invoice for the order
        invoice = Invoice(order)
        
        # Remove the active cart after creating the order
        del self.__active_carts[customer_email]
        
        return order, invoice
        
    # Get an order by its ID
    def get_order(self, order_id):
        return self.__orders.get(order_id)
        
    # Search for e books by title
    def search_ebooks_by_title(self, title):
        result = []
        
        # Find e books that match the title
        for book in self.__ebook_catalog.values():
            if title.lower() in book.get_title().lower():
                result.append(book)
        return result
        
    # Get e books by genre
    def get_ebooks_by_genre(self, genre):
        result = []
        
        # Find e books that match the genre
        for book in self.__ebook_catalog.values():
            if genre.lower() == book.get_genre().lower():
                result.append(book)
        return result
        
    # Return bookstore
    def __str__(self):
        store_info = self.__name + " E-bookstore\n"
        store_info += "Total E-books: " + str(len(self.__ebook_catalog)) + "\n"
        store_info += "Total Customers: " + str(len(self.__customers)) + "\n"
        store_info += "Active Shopping Carts: " + str(len(self.__active_carts)) + "\n"
        store_info += "Total Orders: " + str(len(self.__orders))
        return store_info
