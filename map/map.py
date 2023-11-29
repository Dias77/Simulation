class Map:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.map = self.generate_map()
        
    def generate_map(self):
        newMap = {}
        for height in range(self.height):
            for width in range(self.width):
                newMap[height, width] = ""
        return newMap
    
    def set_position(self, x, y, title):
        self.map[y, x] = title
        
    def get_position(self, x, y):
        return self.map[y, x]
    