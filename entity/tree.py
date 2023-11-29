from entity import Entity

class Tree(Entity):
    def __init__(self, positionX, positionY):
        emj = "\U0001F333"
        super().__init__(self, positionX, positionY, emj)
