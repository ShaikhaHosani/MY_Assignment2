from datetime import datetime  

# This class represents a payment for an order

class Payment:  

    # Class variable to keep track of transaction ID
    transaction_counter = 1  

    # Constructor to initialize payment properties

    def __init__(self, order_id, amount, payment_method):  
        # Unique variable for the order associate with the payment
        self.__order_id = order_id  
        # Amount to be paid
        self.__amount = amount  
        # Date and time of the payment
        self.__payment_date = datetime.now()  
        # Method used for payment credit card
        self.__payment_method = payment_method  
        # Status of the payment initialize with panding at start
        self.__status = "Pending"  
        # Transaction ID generated for this payment with also fix string TXN
        self.__transaction_id = "TXN" + str(Payment.transaction_counter)  
        # Increment the transaction counter for the next payment
        Payment.transaction_counter += 1  

    # Getter method
    # Method to get the order ID
    def get_order_id(self):  
        return self.__order_id  

    # Method to get the payment amount
    def get_amount(self):  
        return self.__amount  

    # Method to get the payment date
    def get_payment_date(self): 
        return self.__payment_date  
    
    # Method to get the payment method
    def get_payment_method(self):  
        return self.__payment_method  

    # Method to get the payment status
    def get_status(self):  
        return self.__status  

     # Method to get the transaction ID
    def get_transaction_id(self): 
        return self.__transaction_id  

    # Setter methods
    # Method to set the payment status
    def set_status(self, status):  
        self.__status = status  

    # Method to process the payment
    def process_payment(self):
        # Update status to Completed  
        self.__status = "Completed"  
        # Return True this mean successful processing
        return True  

    # Return the payment
    def __str__(self):  
        return ("Payment Details:\n" + 
                # Transaction ID
                "Transaction ID: " + self.__transaction_id + "\n" + 
                # Order ID 
                "Order ID: " + self.__order_id + "\n" +  
                # Payment amount
                "Amount: $" + str(round(self.__amount, 2)) + "\n" +  
                # Payment method
                "Method: " + self.__payment_method + "\n" +  
                # Payment status
                "Status: " + self.__status + "\n" +  
                # Payment date
                "Date: " + str(self.__payment_date))  
