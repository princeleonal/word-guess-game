import random

def word_guess_game(predefined_inputs=None):
    words = ["apple", "banana", "cherry", "date", "elder", "fig", "grape", "honeydew"]
    word_to_guess = random.choice(words)
    attempts = 6
    guessed_letters = set()

    print("\n🎮 Welcome to the Word Guess Game!")
    print(f"🔢 You have {attempts} attempts to guess the word.\n")

    input_index = 0

    while attempts > 0:
        display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(f"Word: {display_word}")

        if predefined_inputs is not None:
            if input_index >= len(predefined_inputs):
                print("⚠️ No more inputs provided.")
                break
            guess = predefined_inputs[input_index]
            input_index += 1
            print(f"Auto-input: {guess}")
        else:
            try:
                guess = input("Enter your guess (letter or full word): ").strip().lower()
            except OSError:
                print("⚠️ Input not supported in this environment.")
                break

        if not guess:
            print("⚠️ Please enter a valid guess.\n")
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print("⏳ Already guessed that letter.\n")
            elif guess in word_to_guess:
                guessed_letters.add(guess)
                print("✅ Correct guess!\n")
            else:
                attempts -= 1
                guessed_letters.add(guess)
                print(f"❌ Wrong guess! Attempts left: {attempts}\n")
        elif guess == word_to_guess:
            print(f"🎉 You guessed it right! The word was '{word_to_guess}'.")
            return
        else:
            attempts -= 1
            print(f"❌ Wrong word! Attempts left: {attempts}\n")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"🎉 Well done! The word was: {word_to_guess}")
            return

    print(f"💀 Out of attempts! The word was: '{word_to_guess}'.")

if __name__ == "__main__":
    # Example predefined inputs for testing
    test_inputs = ["a", "e", "i", "o", "u", "grape"]
    word_guess_game(predefined_inputs=test_inputs)
