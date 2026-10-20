"""Console-based Hangman game using a small list of predefined words."""
import random

WORDS = ["python", "computer", "developer", "keyboard", "internet"]
MAX_WRONG_GUESSES = 6


def play():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n=== Hangman Game ===")
    print(f"Guess the word one letter at a time. You have {MAX_WRONG_GUESSES} wrong guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Wrong guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "none")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return

        guess = input("Enter one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)
        if guess not in word:
            wrong_guesses += 1
            print("Incorrect guess.")
        else:
            print("Good guess!")

    print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    play()
