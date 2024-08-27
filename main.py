from word_guess_game import WordGuessGame
from caretaker import Caretaker

def main():
    game = WordGuessGame("python")
    caretaker = Caretaker()

    while not game.is_game_over():
        print("\nMenu:")
        print("1. Guess a letter")
        print("2. Save game")
        print("3. Load game")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            letter = input("Enter a letter to guess: ")
            game.guess(letter)
        elif choice == "2":
            caretaker.save_game(game)
        elif choice == "3":
            caretaker.load_game(game)
        elif choice == "4":
            break
        else:
            print("Invalid option, please try again.")

    if game.is_game_over():
        if "_" not in game._guessed_word:
            print("Congratulations! You guessed the word!")
        else:
            print("Game Over! You've run out of attempts.")

if __name__ == "__main__":
    main()
