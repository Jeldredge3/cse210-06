import random
from constants import *
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Particle(Actor):
    """A visual effect which is does not interact with the enviroment.
    """
    def __init__(self):
        super().__init__()
        self._text = "*"
        self._color = WHITE
        self._speed = CELL_SIZE
        self._x = 0
        self._y = 0
        self.set_text(self._text)
        self._can_move = True

    def toggle_movement(self, boolean):
        if boolean == False:
            self._can_move = False
        else:
            self._can_move = True
            
    def prepare_self(self, pos_x, pos_y, text, color):
        self._x = pos_x
        self._y = pos_y
        self._position = Point(pos_x, pos_y)
        self._text = text
        self._color = color
    
    def randomize(self):
        """Sets a random position, text, color, and speed for the particle.
        """
        rand_value = random.randrange(5, 200)
        rand_shade = Color(rand_value, rand_value, rand_value)

        all_text = ["*", ".", "+"]
        rand_text = random.choice(all_text)
        rand_x = random.randrange(0, MAX_X, CELL_SIZE)
        rand_y = random.randrange(0, MAX_Y, CELL_SIZE)
        rand_speed = random.randrange(2, CELL_SIZE)
        self.prepare_self(rand_x, rand_y, rand_text, rand_shade)
        self.set_speed(rand_speed)

    def set_speed(self, speed):
        self._speed = speed

    def _falling(self):
        """Causes the particle to decend from the top of the screen. Once the particle reaches the bottom, it reappears at the top.
        Passes through the speed of the object which determines the rate which it falls.
        """
        if self._can_move:
            obj_position = self.get_position()
            obj_x = obj_position.get_x()
            obj_y = obj_position.get_y()
            obj_y += self._speed
            pos_new = Point(obj_x, obj_y)
            self.set_position(pos_new)
            if obj_y >= MAX_Y:
                rand_x = random.randrange(0, MAX_X, CELL_SIZE)
                pos_reset = Point(rand_x, 0)
                self.set_position(pos_reset)

    def _explosion(self):
        """Causes particles to travel in random directions.
        """
        pass

