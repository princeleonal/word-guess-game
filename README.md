# 🎮 Crafting a Word Guess Game with Python + Amazon Q CLI

## 🚀 Introduction

Game development, even in its simplest forms, offers a great way to practice logic, creativity, and programming fundamentals. In this post, I’ll walk you through building a minimalist, terminal-based **Word Guess Game** using **Python** and the **Amazon Q CLI**.

## 🧠 Project Summary

The **Word Guess Game** is a CLI-based game where the player tries to guess a randomly selected word within a set number of attempts. Each guess returns feedback, nudging the player toward the correct answer.

* **Tech**: Python, GitHub, Amazon Q CLI
* **Genre**: Puzzle / Word
* **Mode**: Single-player (CLI)

## 🛠️ Development Steps

### 1. ⚙️ Environment Setup

I used:

* A local Python 3 environment
* GitHub for version control ([repo here](https://github.com/princeleonal/word-guess-game))
* **Amazon Q CLI** to quickly scaffold the initial codebase, get function suggestions, and debug logic in real-time.

The Amazon Q CLI made it extremely efficient to:

* Generate basic input/output loops
* Refactor repetitive code
* Catch small logical errors before testing

### 2. 🧩 Game Logic Breakdown

#### 📝 Word Selection

```python
import random
words = ['python', 'cli', 'guess', 'openai', 'developer']
word_to_guess = random.choice(words)
```

#### 🎮 Game Loop

```python
attempts = 6
guessed_letters = []

while attempts > 0:
    display = ''.join([ch if ch in guessed_letters else '_' for ch in word_to_guess])
    print(f"Word: {display}")

    guess = input("Enter your guess: ").strip().lower()

    if len(guess) == 1:
        if guess in guessed_letters:
            print("Already guessed.")
        elif guess in word_to_guess:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts left.")
    elif guess == word_to_guess:
        print("🎉 You win!")
        break
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")
```

### 3. 🌟 Features

* Customizable word list
* Letter tracking
* Guess-by-letter or full word
* CLI feedback after every move

## ✨ What I Learned

* **Quick prototyping** with Amazon Q CLI saved a ton of time.
* Importance of **state management** in games.
* Clean CLI UX boosts player engagement.

## 🧵 Wrap Up

This was a light but rewarding project—perfect to test your logic, and even better with an AI coding assistant like **Amazon Q CLI** in the loop.

---

👕 \[Redeemed the Amazon Q T-shirt?] You bet.

Got ideas for game #2? Ping me!
