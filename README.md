# Wordle Game v1.2

This is a simple implementation of the Wordle game in Python. In Wordle, players have to guess a randomly chosen word within a limited number of attempts.

## How to Play

1. Run the `play_wordle()` function.
2. You have 6 attempts to guess the word.
3. Enter a letter as your guess. Only single alphabetical characters are accepted.
4. If your guess is correct, it will be revealed in its correct position(s) in the word.
5. If your guess is incorrect, the number of attempts will decrease by one.
6. Keep guessing until you either correctly guess the word or run out of attempts.

## Word Source

The game fetches words from [this wordlist](https://www.mit.edu/~ecprice/wordlist.10000) hosted at MIT.

## Dependencies

This code requires the `requests` library to fetch words from the internet. If you don't have it installed, you can install it using pip:

pip install requests

# Wordle Game v1.2

This is a simple implementation of the Wordle game using Flask, HTML, and JavaScript.

## Files

### game.html

This is the main HTML file that displays the game interface to the user. It includes the game board, a form for the user to guess letters, and a reset button to start a new game. The game board is updated dynamically based on the user's guesses and the current state of the game.

### game.js

This JavaScript file handles the reset button's functionality. When the reset button is clicked, it prevents the form from submitting normally, makes an AJAX request to the server to reset the game, and then reloads the page.

### game.py

This is the main server-side Python script that handles the game logic. It includes routes for starting a new game, handling guesses, saving the game state, and resetting the game. The game state is stored in the user's session, and includes the current word, the user's guesses, and the number of remaining attempts.

## How to Run

1. Install the required Python packages: `flask` and `requests`.
2. Run the Python script: `python game.py`.
3. Open a web browser and navigate to `http://localhost:5000`.

## Game Rules

1. The game starts with a randomly chosen word.
2. The player has 6 attempts to guess the word.
3. The player makes guesses by entering a single letter.
4. If the guessed letter is in the word, it is revealed on the game board.
5. If the guessed letter is not in the word, the number of remaining attempts is decreased by one.
6. The game ends when the player has guessed all the letters in the word, or when the player has no more attempts left.

## Future Improvements

1. Add a score system.
2. Add a timer to limit the duration of each game.
3. Add a leaderboard to track the highest scores.
4. Improve the user interface with better styling and animations.
5. Add multiplayer support.
