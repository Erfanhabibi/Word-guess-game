import random
import requests

def generate_word():
    # Add your code here to generate a random word
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word = random.choice(WORDS).decode("utf-8")
    return word

def play_wordle():
    word = generate_word()
    guesses = []
    attempts = 6
    
    while attempts > 0:
        
        # Display the current state of the word and guesses
        print(f"Word: {' '.join([c if c in guesses else '_' for c in word])}")
        print(f"Guesses: {' '.join(guesses)}")
        print(f"Attempts left: {attempts}")

        # Get user input for a guess
        guess = input("Enter a letter: ").lower()

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        # Check if the guess is correct
        if guess in word:
            guesses.append(guess)
            if set(word) == set(guesses):
                print("Congratulations! You guessed the word!")
                break
        else:
            attempts -= 1
            print("Incorrect guess.")

    if attempts == 0:
        print(f"Game over! The word was: {word}")
        

if __name__ == "__main__":
    play_wordle()