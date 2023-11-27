class Entity: 
    def __init__(self, positionX, positionY, name):
        self._positionX = positionX
        self._positionY = positionY
        self._name = name
        
    def get_positionX(self):
        return self._positionX
    
    def set_positionX(self, x):
        self._positionX = x
        
    def get_positionY(self):
        return self._positionY
    
    def set_positionY(self, y):
        self._positionY = y
        
    def get_name(self):
        return self._name