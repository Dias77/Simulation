from creature import Creature

class Herbivore(Creature):
    def __init__(self, positionX, positionY):
        emj = "\U0001F98C"
        super().__init__(self, positionX, positionY, emj)

