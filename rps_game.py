import random

user_wins = 0
computer_wins = 0

MAPPER = {
    'S': 'Scissors',
    'R': 'Rock',
    'P': 'Paper'
}

def battle(user_choice, comp_choice):
    global computer_wins
    global user_wins
    if user_choice == comp_choice:
        return f'Your choice: {MAPPER[user_choice]}\nComputer choice: {MAPPER[comp_choice]}\n\nTie!'
    if user_choice == 'S':
        if comp_choice == 'R':
            computer_wins += 1
            return f'Your choice: {MAPPER[user_choice]}\nComputer choice: {MAPPER[comp_choice]}\n\nRock beats scissors! Computer wins!'
        elif comp_choice == 'P':
            user_wins += 1
            return f'Your choice: {MAPPER[user_choice]}\nComputer choice: {MAPPER[comp_choice]}\n\nScissors beats paper! You win!'

    elif user_choice == 'R':
        if comp_choice == 'S':
            user_wins += 1
            return f'Your choice: {MAPPER[user_choice]}\nComputer choice: {MAPPER[comp_choice]}\n\nRock beats scissors! You win!'
        elif comp_choice == 'P':
            computer_wins += 1
            return f'Your choice: {MAPPER[user_choice]}\nComputer choice: {MAPPER[comp_choice]}\n\nPaper beats rock! Computer wins!'

    elif user_choice == 'P':
        if comp_choice == 'R':
            user_wins += 1
            return f'Your choice: {MAPPER[user_choice]}\nComputer choice: {MAPPER[comp_choice]}\n\nPaper beats rock! You win!'
        elif comp_choice == 'S':
            computer_wins += 1
            return f'Your choice: {MAPPER[user_choice]}\nComputer choice: {MAPPER[comp_choice]}\n\nScissors beats paper! Computer wins!'

def input_validation(choice):
    if choice not in choices:
        print(f'Try again')
        return False
    return True


choices = ['R', 'S', 'P']

while True:
    user_choice = input('Choose your weapon: [R]ock, [S]cissors, [P]aper:\n').upper()
    if user_choice == "END":
        print(f'End of the game\nYou win: {user_wins} battle\nComputer wins: {computer_wins} battle')
        break
    if input_validation( user_choice ):
        computer_choice = random.choice(choices)
        print(battle(user_choice, computer_choice))

