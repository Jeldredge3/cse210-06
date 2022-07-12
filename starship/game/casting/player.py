
import constants
import random
import math
from game.casting.actor import Actor
from game.casting.projectiles import Bullet, MultiShot, LongShot, FlameThrower
from game.shared.point import Point

class Player(Actor):
    """An instance of a Players class. Contains the code for the trail segments.
    """
    def __init__(self):
        super().__init__()
        # ===== Default Positioning ===== #
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        self._start_position = Point(x, y)
        self._position = Point(x, y)
        # ===== Boolean Attributes ===== #
        self._out_of_lives = False
        self._is_destroyed = False
        # ===== Ship Parts ===== #
        """Ship segments goes in this order: 
        [Center, Middle, Front, Top-Left, Middle-left, Bottom-Left, Top-Right, Middle-Right, Bottom-Right]
        """
        ship_blueprint_rocket     = ["X", "| |", "A", "", "/", "|/", "", "\\", "\\|"]
        ship_blueprint_glider     = ["V", "| |", "i i", "", "|/", "|/", "", "\\|", "\\|"]
        ship_blueprint_stinger    = ["M", "| |", "U", "i", "|\\", "\\", "  i", "/|", "/"]
        ship_blueprint_falcon     = ["V", "| |", "U", "", "/", "\\", "", "\\|", "/"]
        ship_blueprint_x_wing     = ["V", "| |", "A", "", "|_", "\\", "", "_|", "/"]
        self._selected_blueprint = ship_blueprint_x_wing
        self._segments = []
        # ===== Bullets ===== #
        self._can_shoot = True
        self._firing_modes = [0, 1, 2, 3]
        self._fire_mode = 0
        self._index = 0
        self._bullets = []
        self._bullet_velocity = Point(0, -constants.CELL_SIZE)

    def get_segments(self):
        return self._segments

    def get_bullets(self):
        return self._bullets

    def get_body(self):
        return self._segments[0]

    def get_start_position(self):
        return self._start_position

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

    def toggle_fire(self, Boolean):
        if Boolean == False:
            self._can_shoot = False
        else:
            self._can_shoot = True

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def turn_ship(self, velocity):
        list_length = len(self._segments)
        # updates the position of each part of the ship.
        for i in range(list_length):
            self._segments[i].set_velocity(velocity)

    def _prepare_body(self, pos_x, pos_y, set_color):
        """Create the body of the spaceship. All parts of the ship are relevant to the position of the ship's center.
        Arg:
            pos_x = The x position of the object.  
            pos_y = The y position of the object.    
            color = The color of the object.
        """
        cell_size = constants.CELL_SIZE
        color = set_color
        self._color = set_color
        self._start_position = Point(pos_x, pos_y)

        index = 0
        # store each part of the ship to the segments list.
        for ship_part in self._selected_blueprint:
            if index == 0: # Center
                position = Point(pos_x, pos_y)
            elif index == 1: # Middle
                position = Point(pos_x, pos_y - cell_size)
            elif index == 2: # Front
                position = Point(pos_x, pos_y - 2*cell_size)
            elif index == 3: # Top_left
                position = Point(pos_x - cell_size, pos_y - 2*cell_size)
            elif index == 4: # Middle_Left
                position = Point(pos_x - cell_size, pos_y - cell_size)
            elif index == 5: # Bottom_Left
                position = Point(pos_x - cell_size, pos_y)
            elif index == 6: # Top_Right
                position = Point(pos_x + cell_size, pos_y - 2*cell_size)
            elif index == 7: # Middle_Right
                position = Point(pos_x + cell_size, pos_y - cell_size)
            elif index == 8: # Bottom_Right
                position = Point(pos_x + cell_size, pos_y)
            else:
                break
            # create an object for each segment of the ship.
            text = str(ship_part)
            ship_part = Actor()
            ship_part.set_position(position)
            ship_part.set_text(text)
            ship_part.set_color(color)
            self._segments.append(ship_part)
            index += 1

    def shoot(self, pos_x, pos_y):
        """Shoots a projectiles based on the fire_mode setting."""
        x_direction = 0
        y_direction = -constants.CELL_SIZE
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
                if len(self._bullets) < constants.MAX_BULLETS:
                    bullet = FlameThrower()
                    self._bullets.append(bullet)
                    velocity = Point(rand_x_direction, y_direction)
                    bullet.fire(pos_x, pos_y, velocity)
                    