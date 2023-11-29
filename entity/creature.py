from entity import Entity

class Creature(Entity):
    def __init__(self, pace, healthPoints):
        self._pace = pace
        self._healthPoints = healthPoints
        
    def make_move(self):
        pass