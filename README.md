# Wordle Game

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

```bash
pip install requests
