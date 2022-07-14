from constants import *
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Pickup(Actor):
    """Creates an instance of the Pickup class which can interact with the player upon collision. Pickups are stored within a list called 'inventory'.
    """
    def __init__(self):
        super().__init__()
        self._text = " "
        self._value = 0
        self.set_text(self._text)
        # ===== Temporary Lists ===== #
        pickups_example = ["Extra Life", "Health Pickup", "Ammo", "Upgrades"]

    def _prepare_self(self, pos_x, pos_y, set_color):
        """Sets the 
        Arg:
            pos_x = The x position of the object.  
            pos_y = The y position of the object.    
            color = The color of the object.
        """
        self._position = Point(pos_x, pos_y)
        self._color = set_color
        self.set_position(self._position)

class Upgrade(Pickup):
    """A pickup object that gives the player a special ability.
    """
    def __init__(self):
        super().__init__()
        self._text = " "
        self._value = 0
        upgrades = {0: "BasicShot", 1: "MultiShot", 2: "LongShot", 3: "FlameThrower"}
        
    
        