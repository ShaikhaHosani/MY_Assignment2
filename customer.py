# This class represents a customer

class Customer:  

    # Constructor to initialize customer properties
    
    def __init__(self, name, email, phone, address, is_loyalty_member: bool = False):  
        # Customer name
        self.__name = name  
        # Customer email
        self.__email = email  
        # Customer phone number
        self.__phone = phone  
        # Customer address
        self.__address = address  
        # Is the customer a loyalty member? Default is False
        self.__is_loyalty_member = is_loyalty_member  
        # List to store the Customer purchase history
        self.__purchase_history = []  

    # Getter method for name
    def get_name(self):  
        # Returns the Customer name
        return self.__name  

    # Getter method for email
    def get_email(self):  
        # Returns the Customer email
        return self.__email  

    # Getter method for phone
    def get_phone(self):  
        # Returns the Customer phone number
        return self.__phone  

    # Getter method for address
    def get_address(self):  
        # Returns the Customer address
        return self.__address  

    # Getter method to check loyalty membership status
    def is_loyalty_member(self):  
        # Returns whether the customer is a loyalty member
        return self.__is_loyalty_member  

    # Getter method for purchase history
    def get_purchase_history(self): 
        # Returns the Customer purchase history
        return self.__purchase_history  

    # Setter method for phone
    def set_phone(self, phone):  
        # Updates the Customer phone number
        self.__phone = phone  

    # Setter method for address
    def set_address(self, address):  
        # Updates the Customer address
        self.__address = address  

    # Setter method for loyalty membership status
    def set_loyalty_member(self, status: bool):  
        # Updates the Customer loyalty membership status
        self.__is_loyalty_member = status  

    # Method to add an order to purchase history
    def add_to_purchase_history(self, order):  
        # Appends an order to the Customer purchase history
        self.__purchase_history.append(order)  

    # Return the customer
    def __str__(self):  
        # Determine loyalty status as a string
        if self.__is_loyalty_member:  
            loyalty_status = "Yes"  
        else:  
            loyalty_status = "No"  
        
        # Return customer details 
        return ("Customer Details:\n" +  
                "Name: " + self.__name + "\n" +  
                "Email: " + self.__email + "\n" +  
                "Phone: " + self.__phone + "\n" +  
                "Address: " + self.__address + "\n" +  
                "Loyalty Member: " + loyalty_status)  
