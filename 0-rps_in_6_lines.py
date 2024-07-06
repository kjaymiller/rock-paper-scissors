import random

options = ['rock', 'paper', 'scissors']

cpu_choice = random.choice(options)

user_choice = input('Choose rock, paper, or scissors:')

print("The computer chose: " + cpu_choice + "You chose: " + user_choice)
