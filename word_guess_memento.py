# Clase Memento que guarda el estado del juego.
class WordGuessMemento:
    def __init__(self, guessed_word, attempts_left):
        self._guessed_word = guessed_word
        self._attempts_left = attempts_left

    def get_guessed_word(self):
        return self._guessed_word

    def get_attempts_left(self):
        return self._attempts_left