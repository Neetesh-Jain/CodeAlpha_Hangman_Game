import random

# Expanded list of words for the game
words_list = [
    'python', 'hangman', 'challenge', 'programming', 'developer', 
    'computer', 'algorithm', 'data', 'structure', 'variable',
    'function', 'object', 'inheritance', 'polymorphism', 'interface',
    'recursion', 'compilation', 'syntax', 'exception', 'debugging',
    'framework', 'database', 'application', 'hardware', 'software'
]

# Hangman stages to draw based on incorrect guesses
hangman_stages = [
    """
      ------
      |    |
           |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
           |
    =========
    """  # This is the final stage when the player loses
]

def get_random_word(words):
    """Selects a random word from the list."""
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for the rest."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word(words_list)  # Get a random word
    guessed_letters = set()  # Keep track of guessed letters
    incorrect_guesses = 0
    max_incorrect_guesses = len(hangman_stages) - 1  # Limit on incorrect guesses

    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect_guesses:
        print(hangman_stages[incorrect_guesses])  # Display the current hangman stage
        print("Current word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} tries left.")

        # Check if the player has guessed the whole word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print(hangman_stages[incorrect_guesses])  # Display the final hangman stage
        print("\nGame over! The word was:", word)

# Run the Hangman game
hangman()
