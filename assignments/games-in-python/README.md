
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a classic Hangman word-guessing game using Python. You'll practice working with strings, loops, conditionals, and user input to create an interactive command-line game that's both fun and challenging.

## 📝 Tasks

### 🛠️ Task 1: Set Up Word Selection

#### Description
Create the foundation for your Hangman game by building a word bank and implementing random word selection.

#### Requirements
Completed program should:

- Create a list containing at least 10 different words for the game
- Use Python's `random` module to randomly select a word at game start
- Initialize variables to track game state (guessed letters, remaining attempts)
- Set maximum number of incorrect guesses allowed (recommend 6 attempts)


### 🛠️ Task 2: Display Game Progress

#### Description
Implement the display system that shows players their current progress in guessing the word.

#### Requirements
Completed program should:

- Show the word using underscores for unguessed letters (e.g., `_ _ a _ _`)
- Update display after each guess to reveal correctly guessed letters
- Display list of previously guessed letters
- Show remaining attempts available to the player


### 🛠️ Task 3: Handle Player Input

#### Description
Create a robust input system that accepts and validates player guesses throughout the game.

#### Requirements
Completed program should:

- Prompt player to enter a single letter guess
- Validate that input is exactly one alphabetic character
- Convert input to consistent case (lowercase or uppercase)
- Prevent duplicate guesses and notify player if letter was already guessed
- Provide clear error messages for invalid input


### 🛠️ Task 4: Implement Game Logic

#### Description
Build the core game mechanics that determine correct/incorrect guesses and win/lose conditions.

#### Requirements
Completed program should:

- Check if guessed letter appears in the selected word
- Update word display when correct letter is guessed
- Decrease remaining attempts for incorrect guesses
- Detect win condition (all letters guessed correctly)
- Detect lose condition (no attempts remaining)
- Display appropriate win or lose message with the revealed word
