import constants
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Enemy(Actor):
    """Creates an instance of the Pickup class which can interact with the player upon collision.
    """
    def __init__(self):
        super().__init__()
        self._text = " "
        self._value = 0
        self._is_destroyed = False
        # ===== Ship Parts ===== #
        self._segments = []
        self._front = "A"
        self._body = "M"
        self._wing_left = "-"
        self._wing_right = "-"

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