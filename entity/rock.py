from entity import Entity

class Rock(Entity):
    def __init__(self, positionX, positionY):
        emj = "\U0001FAA8"
        super().__init__(self, positionX, positionY, emj)