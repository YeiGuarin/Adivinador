from word_guess_memento import WordGuessMemento
class WordGuessGame:
    def __init__(self, word_to_guess):
        self._word_to_guess = word_to_guess
        self._guessed_word = ["_"] * len(word_to_guess)
        self._attempts_left = 3

    def guess(self, letter):
        if letter in self._word_to_guess:
            for i, char in enumerate(self._word_to_guess):
                if char == letter:
                    self._guessed_word[i] = letter
        else:
            self._attempts_left -= 1

        self.show_status()

    def save(self):
        return WordGuessMemento(self._guessed_word.copy(), self._attempts_left)  # Usa la clase importada correctamente

    def restore(self, memento):
        self._guessed_word = memento.get_guessed_word()
        self._attempts_left = memento.get_attempts_left()
        print("Game state restored.")
        self.show_status()

    def show_status(self):
        print(f"Word: {''.join(self._guessed_word)}, Attempts left: {self._attempts_left}")

    def is_game_over(self):
        return self._attempts_left <= 0 or "_" not in self._guessed_word
