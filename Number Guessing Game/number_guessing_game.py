import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        print("\nI'm thinking of a number between 1 and 100.")
        number_to_guess = random.randint(1, 100)
        attempts = 0
        
        # Game loop
        while True:
            try:
                player_guess = int(input("Enter your guess: "))
                attempts += 1

                if player_guess < number_to_guess:
                    print("Too low! Try again.")
                elif player_guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                    break  # Exit the loop when the player guesses correctly

            except ValueError:
                print("Please enter a valid number.")
        
        # Ask player if they want to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    start_game()
