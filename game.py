from flask import Flask, render_template, request, session, flash, jsonify, redirect, url_for
import random
import requests
import json

app = Flask(__name__)
app.secret_key = 'secret'

def generate_word():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word = random.choice(WORDS).decode("utf-8")
    return word

def render_word(word, guesses):
    word_html = ''
    for c in word:
        if c in guesses:
            word_html += f'<span class="letter correct">{c}</span>'
        else:
            word_html += f'<span class="letter incorrect">_</span>'
    return word_html

@app.route('/', methods=['GET'])
def play_wordle():
    start_new_game()
    game_state = session['game_state']
    word_html = render_word(game_state['word'], game_state['guesses'])
    return render_template('game.html', word_html=word_html, guesses=game_state['guesses'], attempts=game_state['attempts'])


def start_new_game():
    word = generate_word()
    session['game_state'] = {
        'word': word,
        'guesses': [],
        'attempts': 6
    }

@app.route('/guess', methods=['POST'])
def handle_guess():
    guess = request.form['guess'].lower()
    game_state = session['game_state']

    if len(guess) != 1 or not guess.isalpha():
        flash("Invalid guess. Please enter a single letter.")
    elif guess in game_state['word']:
        game_state['guesses'].append(guess)
        if set(game_state['word']) == set(game_state['guesses']):
            flash("Congratulations! You guessed the word!")
            return redirect(url_for('play_wordle'))
    else:
        game_state['attempts'] -= 1
        if game_state['attempts'] == 0:
            flash(f"Game over! The word was: {game_state['word']}")
            return redirect(url_for('play_wordle'))

    session['game_state'] = game_state
    word_html = render_word(game_state['word'], game_state['guesses'])
    return render_template('game.html', word_html=word_html, guesses=game_state['guesses'], attempts=game_state['attempts'])

@app.route('/save_game', methods=['GET'])
def save_game():
    if 'game_state' in session:
        game_state = session['game_state']
        with open('game_state.json', 'w') as f:
            json.dump(game_state, f)
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route('/reset_game', methods=['POST'])
def reset_game():
    session.pop('game_state', None)
    return redirect(url_for('play_wordle'))

if __name__ == '__main__':
    app.run(debug=True)