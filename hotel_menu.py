# Creating menu items for user
menu={
    'Pizza':50,
    'Burger':80,
    'Pasta':70,
    'Coffee':90,
    'Salad':100,
}

# Display a greet message for user
print('Welcome to our Python Caffe System')
# Display Menu items for user
print('Pizza : Rs50\nBurger :Rs80\nPasta : RS70\nCoffee : Rs90\nSalad : Rs100')

total_price=0
# Taking first order from user
item_1=input('Please order something...')
# Check if the order is available in our menu system
if item_1 in menu:
    total_price+=menu[item_1]
    print(f'You has been ordered {item_1}')

else:
    print(f'{item_1} is not available yet!...')

# Taking second order from user
another_order=input('Do you want to order something else? (yes/no)')   
if another_order=='yes':
    item_2=input('Please Enter your second order = ') 
    if item_2 in menu:
        total_price+=menu[item_2]
        print(f'You has been ordered {item_2}')
    else:
        print(f'{item_1} is not available yet!...')    

# Finally Display total amount to pay by user
print(f'You have to pay total amount Rs{total_price}')