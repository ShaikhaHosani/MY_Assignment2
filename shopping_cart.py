# This class represents a shopping cart for a customer

class ShoppingCart:  

    # datetime library to manage dates and times

    from datetime import datetime  

    # Constructor to initialize shopping cart properties

    def __init__(self, customer):  
        # Customer associated with the shopping cart
        self.__customer = customer  
        # Dictionary to store items in the cart
        self.__items = {}  
        # Creation date of the shopping cart
        self.__creation_date = self.datetime.now()  
        # Last modified date of the shopping cart
        self.__last_modified = self.__creation_date  

    # Method to add an item to the cart
    def add_item(self, ebook, quantity = 1): 
        # If quantity is less than or equal to zero than nothing
        if quantity <= 0:  
            return  
        
        # If the ebook is already in the cart increase the quantity
        if ebook in self.__items:  
            self.__items[ebook] += quantity  
        else:  
            # If the ebook is not in the cart add it with the specified quantity
            self.__items[ebook] = quantity  
        # Update the last modified date
        self.__last_modified = self.datetime.now()  

    # Method to remove an item from the cart
    def remove_item(self, ebook): 
        # If the ebook is in the cart remove it
        if ebook in self.__items:  
            del self.__items[ebook]  
            # Update the last modified date
            self.__last_modified = self.datetime.now()  
            # Return True indicating successful removal
            return True  
        # Return False if the ebook was not found
        return False  

    # Method to update the quantity of an item in the cart
    def update_quantity(self, ebook, quantity): 
        # If quantity is less than or equal to zero remove the item
        if quantity <= 0:  
            return self.remove_item(ebook)  
        # If the ebook is in the cart update its quantity
        elif ebook in self.__items:  
            self.__items[ebook] = quantity  
            # Update the last modified date
            self.__last_modified = self.datetime.now()  
             # Return True indicating successful update
            return True 
        # Return False if the ebook was not found
        return False  

    # Method to get the items in the cart
    def get_items(self):  
        # Returns a copy of the items in the cart
        return self.__items.copy()  

    # Method to get the associated customer
    def get_customer(self):  
        # Returns the customer associated with the cart
        return self.__customer  

    # Method to get the total number of items in the cart
    def get_total_items(self):  
        # Returns the sum of all item quantities in the cart
        return sum(self.__items.values())  

    # Method to clear all items from the cart
    def clear(self): 
        # Clears all items from the cart
        self.__items.clear()  
        # Update the last modified date
        self.__last_modified = self.datetime.now()  

    # Return shopping cart
    def __str__(self):  
        # If the cart is empty return a message means print the message
        if not self.__items:  
            return "Shopping Cart is empty"  
        
        # Cart string with its name
        cart_str = "Shopping Cart for " + self.__customer.get_name() + ":\n"  
        # Initialize total price
        total = 0  
        # Loop through items in the cart to create a string
        for ebook, quantity in self.__items.items(): 
            # Calculate subtotal for each ebook 
            subtotal = ebook.get_price() * quantity  
            # Add to the total price
            total += subtotal  
            cart_str += (ebook.get_title() + " - Qty: " + str(quantity) + " - $" + str(round(subtotal, 2)) + "\n")  # Add ebook details to the cart string
        # Add total price to the cart
        cart_str += "\nTotal: $" + str(round(total, 2))  
        # Return the cart
        return cart_str  
