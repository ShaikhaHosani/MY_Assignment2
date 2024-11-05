from datetime import datetime  

# Class represent an invoice for an order
class Invoice:  
    
    # Variable for transaction counter every time transaction occur it is increment by 1 but by default it is 1
    transaction_counter = 1  
    
    # Constructor to initialize invoice properties
    def __init__(self, order):
        # Inovice Id but every invoice id start with string INV
        self.__invoice_id = "INV" + str(Invoice.transaction_counter)  
        # Increment counter for the next invoice
        Invoice.transaction_counter += 1  
        # Order associated with this invoice
        self.__order = order  
        # Date and time when the invoice was created
        self.__creation_date = datetime.now()  
        # Payment status of the invoice in start it is Pending
        self.__payment_status = "Pending"  

    # Method to get the invoice ID
    def get_invoice_id(self):
        return self.__invoice_id  

    # Method to get the associated order
    def get_order(self):
        return self.__order  

    # Method to get the creation date of the invoice
    def get_creation_date(self):
        return self.__creation_date  

    # Method to get the payment status
    def get_payment_status(self):
        return self.__payment_status  

    # Method to set the payment status
    def set_payment_status(self, status):
        self.__payment_status = status  

    # Method to calculate the total amount due on the invoice
    def calculate_total(self):
        return self.__order.calculate_total()  

    # Inovice Details
    def __str__(self):
        # Getting the associated order
        order = self.__order  
        # Get items from the order
        items = order.get_items()  
        
        invoice_str = "\nINVOICE #" + self.__invoice_id + "\n"  
        # Formatting the creation date
        invoice_str += "Date: " + self.__creation_date.strftime('%Y-%m-%d %H:%M:%S') + "\n\n"  
        # Adding customer detail to the invoice
        invoice_str += str(order.get_customer()) + "\n\n"  
        # Heading for ordered items
        invoice_str += "Ordered Items:\n"  
        
        # Loop each item in the order to calculate subtotal
        for book, quantity in items.items():  
            # Subtotal for each book after calculation
            subtotal = book.get_price() * quantity  
            # Item detail in the invoice
            invoice_str += (book.get_title() + " x " + str(quantity) + " @ $" + str(round(book.get_price(), 2)) + " = $" + str(round(subtotal, 2)) + "\n")  
        
        # Subtotal in the invoice
        invoice_str += "\nSubtotal: $" + str(round(order.calculate_subtotal(), 2))  
        # Calculate any applicable discount
        discount = order.calculate_discount()  
        # If there is a discount add it to the invoice
        if discount > 0:  
            invoice_str += "\nDiscount: -$" + str(round(discount, 2))  
        
        # Calculating VAT
        vat = order.calculate_vat()  
        # VAT in the invoice
        invoice_str += "\nVAT (8%): $" + str(round(vat, 2))  
        # Adding the total amount due after calculation
        invoice_str += "\nTotal: $" + str(round(self.calculate_total(), 2))  
        # Payment status to the invoice
        invoice_str += "\nPayment Status: " + self.__payment_status  
        
        # Return the invoice
        return invoice_str  
