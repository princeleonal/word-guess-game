# Word Guess Game: A Fun and Challenging CLI Experience

import random

def word_guess_game():
    words = ["apple", "banana", "cherry", "date", "elder", "fig", "grape", "honeydew"]
    word_to_guess = random.choice(words)
    attempts = 6
    guessed_letters = []

    print("Welcome to the Word Guessing Game!")
    print(f"You have {attempts} attempts to guess the word.")

    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(f"Word: {display_word}")
        
        guess = input("Enter your guess (single letter or full word): ").strip().lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                attempts -= 1
                print(f"Incorrect! You have {attempts} attempts left.")
        elif guess == word_to_guess:
            print("Congratulations! You've guessed the word correctly.")
            break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    word_guess_game()
