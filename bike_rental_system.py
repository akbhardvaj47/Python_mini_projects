# Define the BikeRent class
class BikeRent:
    def __init__(self, stock):
        # Initialize the stock with the provided value
        self.stock = stock

    def display_bike(self):
        # Display the current number of bikes in stock
        print(f'Total Stocks = {self.stock}')

    def display_qty(self, qty):
        # Check if the entered quantity is valid (greater than or equal to 0 and less than or equal to 100)
        if qty <= 0:
            # If quantity is negative, ask the user to enter correct stock
            print('Please Enter correct stock')
        elif qty > 100:
            # If quantity exceeds 100, inform the user that only 100 bikes are available
            print('We have only 100 stocks are here')  
        else:
            # Update the stock by reducing the number of bikes rented
            self.stock = self.stock - qty
            # Display the total price for the rented bikes (assuming each bike costs 100 units)
            print(f'Total price = {qty * 100}')
            # Display the remaining stock after rental
            print(f'We have available stocks = {self.stock}')

# Start of the rental system loop
while True:
    # Display a welcome message to the user
    print('------Welcome to my Bike Rental System-------')
    # Create an object of BikeRent with an initial stock of 100 bikes
    obj = BikeRent(100)
    # Show options to the user
    user_need = int(input('''
                        1. Total Bikes
                        2. Total Price
                        3. Exit
    '''))
    # If the user selects option 1, show total bikes
    if user_need == 1:
        obj.display_bike()
    # If the user selects option 2, ask for quantity and calculate the price
    elif user_need == 2:
        qty = int(input('Enter how many bikes you want: '))
        obj.display_qty(qty)
    # If the user selects option 3, exit the loop and end the program
    else:
        break