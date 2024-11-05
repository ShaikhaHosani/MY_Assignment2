from datetime import datetime  

# This class represents a customer order
class Order:  
    
    # Variable for VAT rate that is 0.08
    VAT_RATE = 0.08  
    # Variable for loyalty discount rate that is 0.10
    LOYALTY_DISCOUNT = 0.10  
    # Variable for bulk purchase discount rate that is 0.20
    BULK_DISCOUNT = 0.20  
    # Minimum quantity for bulk discount
    BULK_MINIMUM = 5  
    # Order counter for id by default it is 1
    order_counter = 1  
    
    # Constructor to initialize order properties
    def __init__(self, customer, cart):
        # Order id that always starts from ORD but it always increments by 1
        self.__order_id = "ORD" + str(Order.order_counter)  
        # Increment order counter 
        Order.order_counter += 1  
        # The customer placing the order
        self.__customer = customer  
        # Items in the order from the shopping cart
        self.__items = cart.get_items()  
        # Date and time when the order was placed
        self.__order_date = datetime.now()  
        # Initial status of the order
        self.__status = "Pending"  

    # Method to get the order ID
    def get_order_id(self):
        return self.__order_id  

    # Method to get the customer who placed the order
    def get_customer(self):
        return self.__customer  

    # Method to get the items in the order
    def get_items(self):
        return self.__items.copy()  

    # Method to get the order date
    def get_order_date(self):
        return self.__order_date  

    # Method to get the current status of the order
    def get_status(self):
        return self.__status  

    # Method to set the status of the order
    def set_status(self, status):
        self.__status = status  

    # Method to calculate the subtotal of the order
    def calculate_subtotal(self):
        total_price = 0  
        
        for book, quantity in self.__items.items():
            # price for the book and quantity
            total_price += book.get_price() * quantity  
        
        # Return calculated subtotal price
        return total_price  

    # Method to calculate applicable discounts on the order
    def calculate_discount(self):
        subtotal = self.calculate_subtotal()  
        discount = 0  
        
        # Check for loyalty discount eligibility
        if self.__customer.is_loyalty_member():  
            discount = max(discount, subtotal * self.LOYALTY_DISCOUNT)  
            
        total_items = 0

        # Check for bulk purchase discount eligibility
        for quantity in self.__items.values():
            total_items += quantity

        if total_items >= self.BULK_MINIMUM:  
            discount = max(discount, subtotal * self.BULK_DISCOUNT) 
            
        return discount  

    # Method to calculate VAT on the order
    def calculate_vat(self):
        return (self.calculate_subtotal() - self.calculate_discount()) * self.VAT_RATE  

    # Method to calculate the total amount due for the order
    def calculate_total(self):
        subtotal = self.calculate_subtotal()  
        discount = self.calculate_discount()  
        vat = self.calculate_vat()  
        return subtotal - discount + vat  

    # Method to process the order
    def process_order(self):
        # Update order status
        self.__status = "Completed"  
        # Add order to customer purchase history
        self.__customer.add_to_purchase_history(self)  
        return True  

    # Return order details
    def __str__(self):
        order_details = "Order Details:\n"  
        order_details += "Order ID: " + self.__order_id + "\n"  
        order_details += "Date: " + self.__order_date.strftime('%Y-%m-%d %H:%M:%S') + "\n"  
        order_details += "Status: " + self.__status + "\n"  
        order_details += "Customer: " + self.__customer.get_name() + "\n"  
        order_details += "Total Items: " + str(sum(self.__items.values())) + "\n"  
        order_details += "Total Amount: $" + str(round(self.calculate_total(), 2))  
        return order_details  
