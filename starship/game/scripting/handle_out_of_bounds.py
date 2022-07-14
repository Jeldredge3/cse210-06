from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

#NOTE: This file does not work at this moment. 

class HandleOutofBounds(Action):
    """An update action that checks if objects go off the screen.
    """
    def __init__(self):
        """Constructs a new HandleOutofBounds."""
        self.boundary_right = MAX_X - CELL_SIZE
        self.boundary_left = 0 + CELL_SIZE
        self.boundary_top = 0 + CELL_SIZE
        self.boundary_bottom = MAX_Y - CELL_SIZE

    def execute(self, cast, script):
        """Destroys objects that move out of bounds.
        """
        player = cast.get_first_actor("player")
        p_bullets = player.get_bullets()

        # bullets are destroyed if they travel out of boundary.
        for bullet in p_bullets:
            bullet_x = bullet.get_x()
            bullet_y = bullet.get_y()
            if bullet_y <= self.boundary_top and bullet_y >= self.boundary_bottom:
                p_bullets.pop()
            elif bullet_x <= self.boundary_left and bullet_x >= self.boundary_right:
                p_bullets.pop()