import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point

class Bullet(Actor):
    """A projectile created by another entity which travels at set velocity.
    """
    def __init__(self):
        super().__init__()
        self._text = "o"
        self._color = constants.YELLOW
        self._range = 10
        self._distance_counter = 0
        self._time_counter = 0
        self._x = 0
        self._y = 0

    def fire(self, pos_x, pos_y, velocity):
        self._x = pos_x
        self._y = pos_y
        self._position = Point(pos_x, pos_y)
        self._velocity = velocity
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

class MultiShot(Bullet):
    """Shoots 3 projectiles which spread out upward.
    """
    def __init__(self):
        super().__init__()
        self._text = "x"
        self._color = constants.PURPLE
        self._range = 10
    
class LongShot(Bullet):
    """A long ranged projectile.
    """
    def __init__(self):
        super().__init__()
        self._text = "x"
        self._color = constants.CYAN
        self._range = 20

class FlameThrower(Bullet):
    def __init__(self):
        super().__init__()
        self._text = "*"
        fire_colors = [constants.FIRE0, constants.FIRE1, constants.FIRE2, constants.FIRE3]
        self._color = random.choice(fire_colors)
        self._range = 10