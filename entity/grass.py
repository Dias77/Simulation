from entity import Entity

class Grass(Entity):
    def __init__(self, positionX, positionY):
        emj = "\U0001F331"
        super().__init__(self, positionX, positionY, emj)
    