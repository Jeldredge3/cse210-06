import random
from constants import *
from game.casting.actor import Actor
from game.casting.spaceship import Spaceship
from game.casting.projectiles import Bullet, MultiShot, LongShot, FlameThrower
from game.shared.point import Point

class Player(Spaceship):
    """A Spaceship object which is controlled by the player. The player can pickup upgrades which provide new firing modes.
    Please see the parent class Spaceship for inherited methods and attributes.
    """
    def __init__(self):
        super().__init__()
        self._name = "Player"
        ship_blueprint_x_wing = ["V", "| |", "A", "", "|_", "\\", "", "_|", "/"]
        self._selected_blueprint = ship_blueprint_x_wing
        self._firing_modes = [0, 1, 2, 3]
        self._fire_mode = 0
        self._index = 0

    def get_fire_mode(self):
        return self._fire_mode

    def reset_fire_mode(self):
        self._fire_mode = self._firing_modes[0]
        
    def _cycle_mode(self):
        max_index = len(self._firing_modes) -1
        print(f"{self._fire_mode} / {max_index}")
        if self._fire_mode < max_index: 
            self._index += 1
            self._fire_mode = self._firing_modes[self._index]
        else:
            self._index = 0
            self._fire_mode = self._firing_modes[self._index]

    def shoot(self, pos_x, pos_y):
        """Shoots a projectiles based on the fire_mode setting."""
        x_direction = 0
        y_direction = -CELL_SIZE
        rand_x_direction = random.randint(-10, 10)
        # check if player is allowed to shoot.
        if self._can_shoot:
            # BasicShot
            if self._fire_mode == 0:
                if len(self._bullets) < 1:
                    bullet = Bullet()
                    self._bullets.append(bullet)
                    velocity = Point(x_direction, y_direction)
                    bullet.fire(pos_x, pos_y, velocity)
            # MultiShot
            elif self._fire_mode == 1:
                directions = [-15, 0, 15]
                if len(self._bullets) < 3:
                    for x_direction in directions:
                        bullet = MultiShot()
                        self._bullets.append(bullet)
                        velocity = Point(x_direction, y_direction)
                        bullet.fire(pos_x, pos_y, velocity)
            # LongShot
            elif self._fire_mode == 2:
                if len(self._bullets) < 1:
                    bullet = LongShot()
                    self._bullets.append(bullet)
                    velocity = Point(0, y_direction * 2)
                    bullet.fire(pos_x, pos_y, velocity)
            # FlameThrower
            elif self._fire_mode == 3:
                if len(self._bullets) < MAX_BULLETS:
                    bullet = FlameThrower()
                    self._bullets.append(bullet)
                    velocity = Point(rand_x_direction, y_direction)
                    bullet.fire(pos_x, pos_y, velocity)