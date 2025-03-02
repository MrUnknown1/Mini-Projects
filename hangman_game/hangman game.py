import random as rd
import json

# 🎯 Categorized words for difficulty levels
words = {
    "easy": [
        "apple", "banana", "cherry", "grape", "lemon", "mango", "orange", "peach", "pear", "plum",
        "car", "bus", "train", "boat", "plane", "bike", "truck", "van", "jeep", "scooter",
        "dog", "cat", "fish", "bird", "horse", "mouse", "rabbit", "turtle", "frog", "sheep",
        "red", "blue", "green", "yellow", "pink", "purple", "black", "white", "brown", "gray"
    ],
    "medium": [
        "guitar", "puzzle", "rocket", "oxygen", "quantum", "notebook", "mystery", "elephant", "lighthouse", "kangaroo",
        "tornado", "computer", "firework", "language", "painting", "diamond", "universe", "magnet", "history", "journey",
        "captain", "adventure", "treasure", "pyramid", "volcano", "invisible", "harmony", "whisper", "shimmer", "twilight",
        "illusion", "moonlight", "crystal", "midnight", "galaxy", "symphony", "carnival", "mechanic", "satellite", "glacier"
    ],
    "hard": [
        "encyclopedia", "photosynthesis", "extraterrestrial", "hallucination", "unbelievable", "xylophone", "acquaintance", "transcendent", "juxtaposition", "microscope",
        "exaggeration", "parliament", "psychiatrist", "sophisticated", "circumference", "metamorphosis", "cryptography", "hypothetical", "irreplaceable", "inconspicuous",
        "mathematics", "pneumonia", "zoologist", "fluorescent", "approximate", "constellation", "handkerchief", "aesthetics", "magnificent", "unanimous",
        "philosophy", "radiation", "temperature", "ambassador", "descendant", "vocabulary", "celebration", "appreciation", "consequence", "biodiversity"
    ]
}


# 🎨 Hangman ASCII Art
hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
      ========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
      ========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
      ========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
      ========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
      ========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
      ========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
      ========
    """
]

win_ascii = """
    😃  YOU WON! 🎉  
     \\O/  
      |   
     / \\   
"""

lose_ascii = """
    ☠ GAME OVER ☠
     (X_X)
     / | \\
     /   \\ 
"""

def display_hangman(wrong_guesses):
    print(hangman_stages[wrong_guesses])

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        print("Invalid input! Please type 'yes' or 'no'.")

def main():
    score = 0
    playing = True
    
    while playing:
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        if difficulty not in words:
            print("Invalid difficulty! Choose from easy, medium, or hard.")
            continue
        
        answer = rd.choice(words[difficulty])
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        max_attempts = 6

        while True:
            display_hangman(wrong_guesses)
            display_hint(hint)
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Enter a single letter.")
                continue

            if guess in guessed_letters:
                print(f"{guess} is already guessed.")
                continue

            guessed_letters.add(guess)

            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
                score += 10  # Add points for correct guesses
            else:
                wrong_guesses += 1
                
            if "_" not in hint:
                display_hangman(wrong_guesses)
                display_answer(answer)
                print(win_ascii)
                score += 50  # Bonus for winning
                break

            elif wrong_guesses >= max_attempts:
                display_hangman(wrong_guesses)
                display_answer(answer)
                print(lose_ascii)
                break
        
        print(f"Your current score: {score}")
        playing = play_again()

    print("Thanks for playing Hangman! Your final score: ", score)

if __name__ == '__main__':
    main()

