from map import Map

class Render():
    def __init__(self, map_object):
        self.map = map_object
        
    def render_map(self):
        for height in range(self.map.height):
            for width in range(self.map.width):
                print(self.map.map[height, width], end=" ")
            print()
        
        
map1 = Map(5, 5)
renderer = Render(map1)
renderer.render_map()
