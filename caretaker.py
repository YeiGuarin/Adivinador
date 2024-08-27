class Caretaker:
    def __init__(self):
        self._memento = None

    def save_game(self, game):
        self._memento = game.save()
        print("Game saved.")

    def load_game(self, game):
        if self._memento:
            game.restore(self._memento)
        else:
            print("No saved game to load.")

