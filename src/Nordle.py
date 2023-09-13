import random  # To select random words.

def load_words():
    """Load words from 5lw.txt and return a list of words."""
    word_list_path = "src/static/5lw.txt"  # Path to the word file
    with open(word_list_path, 'r', encoding="utf-8") as file:
        # Split the file content into lines to get individual words
        words = file.read().splitlines()
    return words




def get_valid_guess(word_list):
    """Prompt the user for a guess and validate against the word list."""
    while True:
        guess = input("Gjett ordet: ").lower()  # Get the user's guess
        if guess in word_list:
            return guess
        else:
            print("Ordet finnes ikke i databasen.")


def compare_guess(chosen_word, user_guess):
    """Compare the user's guess with the chosen word and return feedback."""
    
    feedback = []
    
    # Step 1: Exact Matches
    for cw_letter, ug_letter in zip(chosen_word, user_guess):
        if cw_letter == ug_letter:
            feedback.append('green')
        else:
            feedback.append('grey')
    
    # Step 2: Count Letters
    chosen_word_counts = {}
    user_guess_counts = {}
    for i, (cw_letter, ug_letter) in enumerate(zip(chosen_word, user_guess)):
        if feedback[i] == 'grey':
            chosen_word_counts[cw_letter] = chosen_word_counts.get(cw_letter, 0) + 1
            user_guess_counts[ug_letter] = user_guess_counts.get(ug_letter, 0) + 1
    
    # Step 3: Determine L Feedback
    for i, ug_letter in enumerate(user_guess):
        if feedback[i] == 'grey' and user_guess_counts[ug_letter] > 0 and chosen_word_counts.get(ug_letter, 0) > 0:
            feedback[i] = 'yellow'
            user_guess_counts[ug_letter] -= 1
            chosen_word_counts[ug_letter] -= 1

    return feedback




def main_game():
    words = load_words() 
    chosen_word = random.choice(words)
    MAX_GUESSES = 6
    guess_count = 0

    print(chosen_word)
    print("Velkommen til Nordle!")
    while guess_count < MAX_GUESSES:
        user_guess = get_valid_guess(words)  # This will validate the word is in your list

        feedback = compare_guess(chosen_word, user_guess)
        print(" ".join(feedback))

        if user_guess == chosen_word:
            print("Gratulerer! Du gjettet riktig.")
            return  # Exit the function, ending the game
        else:
            guess_count += 1
            print(f"Du har {6- guess_count} forsøk igjen.")

    print(f"GAME OVER! Beklager, ingen flere forsøk. Det riktige svaret var '{chosen_word}'.")

# Start the game

