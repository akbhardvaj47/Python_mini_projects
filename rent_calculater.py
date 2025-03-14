# <------------------- We need ------------->
# 1-> Input from user
# 2-> Total rent 
# 3-> Total electricity to spend
# 4-> Charge per unit
# 5-> Order food in a month

room_rent=int(input('Enter total Room/Hostel rent : '))
ordered_food=int(input('Enter total ordered food : '))
total_electricity_bill=int(input('Enter total electricity bill spend in a month : ')) # spend total electricity in months
charge_per_unit=int(input('Enter the charge per unit bill : '))
number_of_persons=int(input('Enter total number of person living in room : '))

total_bill=total_electricity_bill*charge_per_unit

payable_amount=(room_rent+ordered_food+total_bill)//number_of_persons
print(f'One person have to pay {payable_amount}')

