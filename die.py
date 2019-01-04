from random import randint

class Die():
    """Klasa przedstawiająca pojedyńczą kość do gry"""

    def __init__(self, num_sides=6):
        """Przyjęcie założenia że kość do gry ma postać sześcianu"""

        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartości z zakresu od 1 do liczby ścianek, które ma kośc do gry"""

        return randint(1, self.num_sides)
