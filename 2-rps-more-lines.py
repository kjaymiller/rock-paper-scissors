import random

user_choice = input('Choose rock, paper, or scissors:')
computer_choice = random.choice(['rock', 'paper', 'scissors'])

print(
    f"""The computer chose: {computer_choice}
You chose: {user_choice}""")
