import random

score: int = 0

while True:
    user_choice = input('Choose rock, paper, or scissors:')
    computer_choice = random.choice(['rock', 'paper', 'scissors']))
    result = "You lose!"

    if computer_choice == user_choice:
        result = "It's a tie!"

    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        score += 1
    
    else:
        score -= 1

    print(result)
    print(
        f"""The computer chose: {computer_choice}
    You chose: {user_choice}
    Your score: {score}"""
    )
