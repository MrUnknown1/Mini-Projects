import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice(allow_quit=False):
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    if allow_quit:
        choices['q'] = 'quit'
    
    choice = input("Enter r for rock, p for paper, s for scissors" + (", or q to quit" if allow_quit else "") + ": ").lower()
    while choice not in choices:
        print("Invalid choice. Try again.")
        choice = input("Enter r for rock, p for paper, s for scissors" + (", or q to quit" if allow_quit else "") + ": ").lower()
    return choices[choice]

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score, computer_score = 0, 0
    first_round = True
    while True:
        user_choice = get_user_choice(allow_quit=not first_round)
        first_round = False
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        while user_choice in ['rock', 'paper', 'scissors']:
            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = determine_winner(user_choice, computer_choice)
            print(result)

            if "You win" in result:
                user_score += 1
            elif "Computer wins" in result:
                computer_score += 1

            print(f"Score -> You: {user_score}, Computer: {computer_score}")
            
            user_choice = get_user_choice(allow_quit=True)
            if user_choice == 'quit':
                print("Thanks for playing!")
                return

if __name__ == "__main__":
    play_game()

