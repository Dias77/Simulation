from abc import ABC

class Entity(ABC): 
    def __init__(self, positionX, positionY, emj):
        self._positionX = positionX
        self._positionY = positionY
        self.emj = emj
        
