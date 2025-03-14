'''
1-> Take input from user like 
[Rock, Paper, Scissor]
2-> Take computer choice 

Cases of game to win:-
scissor cuts the paper -> scissor won
rock breaks the scissor -> rock won
paper covers the rock -> paper won
'''
# Import random module to use random function
import random
choices=['Rock', 'Paper', 'Scissor']
user_choice=input('Enter your move : ')
computer_choice=random.choice(choices)

# condition to check the user and computer choice is same
if user_choice==computer_choice:
    print(f"Your choice is {user_choice} and computer choice is {computer_choice} is same :\nIt's a Tie")

# condition to check -> In how many cases to won the match for the user    
elif (user_choice=='Rock' and computer_choice=='Paper') or (user_choice=='Scissor' and computer_choice=='Paper') or (user_choice=='Paper' and computer_choice=='Rock'):
    print(f'Your choice is {user_choice} and computer choice is {computer_choice} : \nCongratulations! You won the match') 

# if not meets the cases to won the match for user then computer will Win the match    
else:
    print(f'Your choice is {user_choice} and computer choice is {computer_choice} : \nOops! You lost the match')    