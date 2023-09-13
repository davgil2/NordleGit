from flask import Flask, request, jsonify, session, render_template

from flask_session import Session
import Nordle
import os
import random
app = Flask(__name__, static_url_path='', static_folder='static')

# Configure session
app.config['SESSION_TYPE'] = 'filesystem'  # use filesystem to store sessions
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SECRET_KEY'] = os.urandom(24)  # for session signing (change to a stable key for production)
Session(app)

@app.route('/')
def index():
    words = Nordle.load_words()
    session['chosen_word'] = random.choice(words)
    session['attempts'] = 0  # Resetting the attempts
    # Reset other session variables if needed
    return render_template('index.html')



@app.route('/guess', methods=['POST'])
def guess_word():
    data = request.get_json()
    guess = data.get('word', '').lower()
    words = Nordle.load_words()    
    # Get attempts from session
    attempts = session.get('attempts', 0)
    if attempts >= 6:
        return jsonify({
            'status': 'gameover',
            'chosen_word': session.get('chosen_word', '')
        })

    if len(guess) != 5 or guess not in words:
        return jsonify({
            'status': 'fail',
            'message': 'Ordet er ikke i ordlisten'
        })

    feedback = Nordle.compare_guess(session['chosen_word'], guess)

    attempts += 1
    session['attempts'] = attempts

    return jsonify({
        'status': 'success',
        'feedback': feedback
    })

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)