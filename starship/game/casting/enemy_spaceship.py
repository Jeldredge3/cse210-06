import random
from constants import *
from game.casting.actor import Actor
from game.casting.spaceship import Spaceship
from game.casting.projectiles import Bullet
from game.shared.point import Point

class Enemy(Spaceship):
    """A Spaceship object that gets moved automatically, meant as an opponent for the player.
    """
    def __init__(self):
        super().__init__()
        self._name = "Enemy"
        ship_blueprint_fighter    = ["", "O", "", "/", "|-", "\\", "\\", "-|", "/"]
        self._selected_blueprint = ship_blueprint_fighter
        self._direction = Point(0, CELL_SIZE)

    def get_direction(self):
        """ Returns the direction the ship is traveling.
        
        Guide:
        ( x, 0) = right
        (-x, 0) = left
        (0,  y) = down
        (0, -y) = up
        """
        return self._direction

    def shoot(self, pos_x, pos_y):
        """Shoots a projectiles based on the fire_mode setting."""
        x_direction = 0
        y_direction = CELL_SIZE
        rand_x_direction = random.randint(-10, 10)
        # check if enemy is allowed to shoot.
        if self._can_shoot:
            if len(self._bullets) < 1:
                bullet = Bullet()
                self._bullets.append(bullet)
                velocity = Point(x_direction, y_direction)
                bullet.fire(pos_x, pos_y, velocity)

class BonusEnemy(Enemy):
    """A Spaceship object that gets moved automatically, meant as an opponent for the player.
    """
    def __init__(self):
        super().__init__()
        self._name = "Enemy"
        ship_blueprint_fighter2    = ["", "-0", "", "/", "|-0", "\\", "\\", "-|", "/"]
        self._selected_blueprint = ship_blueprint_fighter2
        self._direction = Point(CELL_SIZE, CELL_SIZE)