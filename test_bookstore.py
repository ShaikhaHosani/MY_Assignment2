# Import classes
from bookstore import Bookstore
from ebook import Ebook
from customer import Customer
from payment import Payment

# Function to test e book management feature
def test_ebook_management(store):
    print("\n************ Testing E-book Management ************\n")
    
    # Create sample e books
    ebook1 = Ebook("Python Basics", "Omar", "2024-10-01", "Programming", 29.99, "ISBN001", "Learn Python programming")
    ebook2 = Ebook("Data Science", "Youssef", "2024-10-15", "Programming", 34.99, "ISBN002", "Introduction to Data Science")
    ebook3 = Ebook("Web Development", "Zaid", "2024-10-29", "Programming", 24.99, "ISBN003", "Web Development with HTML/CSS")
    
    # Add e books to the store
    store.add_ebook(ebook1)
    store.add_ebook(ebook2)
    store.add_ebook(ebook3)
    
    # Update the price of an e book
    store.update_ebook_price("ISBN001", 32.99)
    
    # Get and print detail of a specific e book
    book = store.get_ebook("ISBN001")
    print(book)
    
    # Remove an e book from the store
    store.remove_ebook("ISBN002")
    print("\nRemoved ISBN002, remaining books:")
    print(store)

# Function to test customer management feature
def test_customer_management(store):
    print("\n************ Testing Customer Management ************\n")
    
    # Create sample customer
    customer1 = Customer("Khalid", "khalid@gmail.com", "123-456-7890", "123 Dubai", True)
    customer2 = Customer("Salim", "salim@gmail.com", "987-654-3210", "456 Dubai")
    
    # Add customer to the store
    store.add_customer(customer1)
    store.add_customer(customer2)
    
    # Print detail of the first customer
    print("Customer 1 details:")
    print(store.get_customer("khalid@gmail.com"))
    
    # Update the phone number of the first customer
    customer1 = store.get_customer("khalid@gmail.com")
    customer1.set_phone("555-555-5555")
    print("\nUpdated phone number:")
    print(customer1)
    
    # Remove the second customer from the store
    store.remove_customer("salim@gmail.com")
    print("\nRemoved salim@gmail.com, store status:")
    print(store)

# Function to test shopping cart and order processing

def test_shopping_and_ordering(store):
    print("\n************ Testing Shopping and Ordering ************\n")
    
    # Get the first customer
    customer = store.get_customer("khalid@gmail.com")
    
    # Create a shopping cart for the customer
    cart = store.create_cart(customer.get_email())
    
    # Add item to the shopping cart
    cart.add_item(store.get_ebook("ISBN001"), 2)
    cart.add_item(store.get_ebook("ISBN003"), 3)
    
    # Print the content of the shopping cart
    print("Shopping Cart:")
    print(cart)
    
    # Create an order from the shopping cart
    order, invoice = store.create_order(customer.get_email())
    
    # Process payment for the order
    payment = Payment(order.get_order_id(), order.calculate_total(), "Credit Card")
    payment.process_payment()
    
    # Set the payment status in the invoice
    invoice.set_payment_status("Paid")
    
    # Print the final invoice detail
    print("\nFinal Invoice:")
    print(invoice)

# Main function to run test

def main():
    # Create a bookstore instance
    store = Bookstore("Great E books Store")
    
    # Run the Testing
    test_ebook_management(store)
    test_customer_management(store)
    test_shopping_and_ordering(store)

# Main Method Calling
main()

# # Import classes
# from bookstore import Bookstore
# from ebook import Ebook
# from customer import Customer
# from payment import Payment

# # Function to test e-book management feature
# def test_ebook_management(store):
#     print("\n************ Testing E-book Management ************\n")
    
#     # Create sample e-books
#     ebook1 = Ebook("Advanced Java Programming", "Sara", "2024-11-01", "Programming", 49.99, "ISBN004", "Master Java programming with advanced concepts.")
#     ebook2 = Ebook("Artificial Intelligence Basics", "Hassan", "2024-11-15", "Technology", 39.99, "ISBN005", "An introductory guide to Artificial Intelligence.")
#     ebook3 = Ebook("Digital Marketing Essentials", "Fatima", "2024-11-20", "Marketing", 29.99, "ISBN006", "Learn the fundamentals of digital marketing.")
    
#     # Add e-books to the store
#     store.add_ebook(ebook1)
#     store.add_ebook(ebook2)
#     store.add_ebook(ebook3)
    
#     # Update the price of an e-book
#     store.update_ebook_price("ISBN004", 44.99)
    
#     # Get and print detail of a specific e-book
#     book = store.get_ebook("ISBN004")
#     print(book)
    
#     # Remove an e-book from the store
#     store.remove_ebook("ISBN005")
#     print("\nRemoved ISBN005, remaining books:")
#     print(store)

# # Function to test customer management feature
# def test_customer_management(store):
#     print("\n************ Testing Customer Management ************\n")
    
#     # Create sample customers
#     customer1 = Customer("Layla Al-Sabah", "layla.alsabah@gmail.com", "050-123-4567", "789 Sharjah, UAE", True)
#     customer2 = Customer("Omar Al-Jaber", "omar.aljaber@gmail.com", "052-765-4321", "123 Ajman, UAE")
    
#     # Add customers to the store
#     store.add_customer(customer1)
#     store.add_customer(customer2)
    
#     # Print detail of the first customer
#     print("Customer 1 details:")
#     print(store.get_customer("layla.alsabah@gmail.com"))
    
#     # Update the phone number of the first customer
#     customer1 = store.get_customer("layla.alsabah@gmail.com")
#     customer1.set_phone("058-555-5555")
#     print("\nUpdated phone number:")
#     print(customer1)
    
#     # Remove the second customer from the store
#     store.remove_customer("omar.aljaber@gmail.com")
#     print("\nRemoved omar.aljaber@gmail.com, store status:")
#     print(store)

# # Function to test shopping cart and order processing
# def test_shopping_and_ordering(store):
#     print("\n************ Testing Shopping and Ordering ************\n")
    
#     # Get the first customer
#     customer = store.get_customer("layla.alsabah@gmail.com")
    
#     # Create a shopping cart for the customer
#     cart = store.create_cart(customer.get_email())
    
#     # Add items to the shopping cart
#     cart.add_item(store.get_ebook("ISBN004"), 1)
#     cart.add_item(store.get_ebook("ISBN006"), 2)
    
#     # Print the content of the shopping cart
#     print("Shopping Cart:")
#     print(cart)
    
#     # Create an order from the shopping cart
#     order, invoice = store.create_order(customer.get_email())
    
#     # Process payment for the order
#     payment = Payment(order.get_order_id(), order.calculate_total(), "Credit Card")
#     payment.process_payment()
    
#     # Set the payment status in the invoice
#     invoice.set_payment_status("Paid")
    
#     # Print the final invoice detail
#     print("\nFinal Invoice:")
#     print(invoice)

# # Main function to run tests
# def main():
#     # Create a bookstore instance
#     store = Bookstore("Amazing E-books Store")
    
#     # Run the testing functions
#     test_ebook_management(store)
#     test_customer_management(store)
#     test_shopping_and_ordering(store)

# # Main Method Calling
# if __name__ == "__main__":
#     main()

# # Import classes
# from bookstore import Bookstore
# from ebook import Ebook
# from customer import Customer
# from payment import Payment

# # Function to test e-book management feature
# def test_ebook_management_fail(store):
#     print("************ Testing E-book Management (Failing Scenario) ************")
    
#     # Create sample e-books
#     ebook1 = Ebook("Introduction to Data Science", "Ali", "2024-12-01", "Data Science", 45.99, "ISBN007", "A beginner's guide to Data Science.")
#     ebook2 = Ebook("Machine Learning for Beginners", "Zainab", "2024-12-15", "Data Science", 39.99, "ISBN008", "Understanding Machine Learning concepts.")
    
#     # Add e-books to the store
#     store.add_ebook(ebook1)
    
#     # Attempt to update a non-existent e-book (fail condition)
#     print("Attempting to update a non-existent e-book (ISBN008):")
#     if store.update_ebook_price("ISBN008", 34.99):  # This should fail as ISBN008 is not added yet
#         print("Update success: True")
#     else:
#         print("Update success: False")

# # Function to test customer management feature
# def test_customer_management_fail(store):
#     print("************ Testing Customer Management (Failing Scenario) ************")
    
#     # Create a sample customer
#     customer1 = Customer("Amira Al-Farsi", "amira.alfarsi@gmail.com", "056-123-4567", "456 Dubai, UAE", True)
    
#     # Add customer to the store
#     store.add_customer(customer1)
    
#     # Attempt to retrieve a non-existent customer (fail condition)
#     print("Attempting to retrieve a non-existent customer (amal@gmail.com):")
#     non_existent_customer = store.get_customer("amal@gmail.com")  # This should fail as this email is not in the system
#     if non_existent_customer is None:
#         print("Non-existent customer details: None")
#     else:
#         print("Non-existent customer details:", non_existent_customer)

# # Function to test shopping cart and order processing
# def test_shopping_and_ordering_fail(store):
#     print("************ Testing Shopping and Ordering (Failing Scenario) ************")
    
#     # Get the first customer
#     customer = store.get_customer("amira.alfarsi@gmail.com")
    
#     # Create a shopping cart for the customer
#     cart = store.create_cart(customer.get_email())
    
#     # Attempt to add a non-existent e-book to the shopping cart (fail condition)
#     print("Attempting to add a non-existent e-book (ISBN009) to the cart:")
#     ebook = store.get_ebook("ISBN009")  # This should fail as ISBN009 is not added yet
#     if ebook is None:
#         print("Error encountered: E-book ISBN009 does not exist.")
#     else:
#         cart.add_item(ebook, 1)

# # Main function to run failing tests
# def main():
#     # Create a bookstore instance
#     store = Bookstore("UAE E-books Store")
    
#     # Run the failing testing functions
#     test_ebook_management_fail(store)
#     test_customer_management_fail(store)
#     test_shopping_and_ordering_fail(store)

# # Main Method Calling
# if __name__ == "__main__":
#     main()
