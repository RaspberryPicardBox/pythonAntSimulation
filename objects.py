from graphics import *

# Define all the types of objects available in the world
TYPES = {"air": (0, 0, 0), "ant": (255, 255, 255), "pheromone": (255, 0, 0), "food": (0, 255, 0), "colony": (0, 0, 255)}


class WorldObject: # Abstract WorldObject class
    # Takes: window object, type of object (for colour), and co-ords (0, 0)
    def __init__(self, window: GraphWin, object_type: str, x=0, y=0):
        self.point = Point(x, y)
        if object_type in TYPES:
            self.object_type = object_type
        else:
            raise ValueError("object_type not valid type")
        self.window = window

    def draw(self):
        self.point.draw(self.window)


class Air(WorldObject):
    def __init__(self, window: GraphWin, object_type: str):
        super().__init__(window, object_type)
        self.point.setOutline(color_rgb(TYPES["air"][0], TYPES["air"][1], TYPES["air"][2]))  # Set color of object
