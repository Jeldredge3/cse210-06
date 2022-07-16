import random
from constants import *
from game.casting.actor import Actor
from game.casting.projectiles import Bullet, MultiShot, LongShot, FlameThrower
from game.shared.point import Point

class Spaceship(Actor):
    """An instance of a Spaceship object. A Spaceship is a list object, with each list element as a part of the ship.
    To get the position of the ship, reference the ship's center in position [0] of the list.
    """
    def __init__(self):
        super().__init__()
        self._name = "UFO"
        self._value = 0
        # ===== Default Positioning ===== #
        x = int(MAX_X / 2)
        y = int(MAX_Y / 2)
        self._start_position = Point(x, y)
        self._position = Point(x, y)
        # ===== Boolean Attributes ===== #
        self._can_shoot = True
        self._can_move = True
        self._is_destroyed = False
        # ===== Ship Parts ===== #
        """Ship segments goes in this order: 
        [Center, Middle, Front, Top-Left, Middle-left, Bottom-Left, Top-Right, Middle-Right, Bottom-Right]
        """
        empty_blueprint           = ["", "", "", "", "", "", "", "", ""]
        ship_blueprint            = ["C", "M", "F", "TL", "ML", "BL", "TR", "MR", "BR"]
        ship_blueprint_rocket     = ["X", "| |", "A", "", "/", "|/", "", "\\", "\\|"]
        ship_blueprint_glider     = ["V", "| |", "i i", "", "|/", "|/", "", "\\|", "\\|"]
        ship_blueprint_stinger    = ["M", "| |", "U", "i", "|\\", "\\", "  i", "/|", "/"]
        ship_blueprint_falcon     = ["V", "| |", "U", "", "/", "\\", "", "\\|", "/"]
        ship_blueprint_x_wing     = ["V", "| |", "A", "", "|_", "\\", "", "_|", "/"]
        ship_blueprint_fighter    = ["", "O", "", "/", "|-", "\\", "\\", "-|", "/"]
        self._selected_blueprint = ship_blueprint
        self._segments = []
        # ===== Bullets ===== #
        self._bullets = []
        self._bullet_velocity = Point(0, -CELL_SIZE)

    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value

    def get_segments(self):
        return self._segments
        
    def get_bullets(self):
        return self._bullets

    def get_body(self):
        return self._segments[0]

    def get_start_position(self):
        return self._start_position
    
    def toggle_fire(self, boolean):
        if boolean == False:
            self._can_shoot = False
        else:
            self._can_shoot = True

    def toggle_movement(self, boolean):
        if boolean == False:
            self._can_move = False
        else:
            self._can_move = True

    def destroy_self(self):
        self._is_destroyed = True
    
    def repair_self(self):
        self._is_destroyed = False

    def move_next(self):
        if self._can_move:
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
        """Changes the velocity of the ship, which is stored as a Point() object. 
        Loops through each segment and updates each item's velocity.

        Guide:
        ( x, 0) = right
        (-x, 0) = left
        (0,  y) = down
        (0, -y) = up
        """
        list_length = len(self._segments)
        # updates the position of each part of the ship.
        for i in range(list_length):
            self._segments[i].set_velocity(velocity)

    def _build_ship(self, pos_x, pos_y, set_color):
        """Create the body of the spaceship. All parts of the ship are relevant to the position of the ship's center.
        Arg:
            pos_x = The x position of the object.  
            pos_y = The y position of the object.    
            color = The color of the object.
        """
        color = set_color
        self._color = set_color
        self._start_position = Point(pos_x, pos_y)

        index = 0
        # store each part of the ship to the segments list.
        for ship_part in self._selected_blueprint:
            if index == 0: # Center
                position = Point(pos_x, pos_y)
            elif index == 1: # Middle
                position = Point(pos_x, pos_y - CELL_SIZE)
            elif index == 2: # Front
                position = Point(pos_x, pos_y - 2*CELL_SIZE)
            elif index == 3: # Top_left
                position = Point(pos_x - CELL_SIZE, pos_y - 2*CELL_SIZE)
            elif index == 4: # Middle_Left
                position = Point(pos_x - CELL_SIZE, pos_y - CELL_SIZE)
            elif index == 5: # Bottom_Left
                position = Point(pos_x - CELL_SIZE, pos_y)
            elif index == 6: # Top_Right
                position = Point(pos_x + CELL_SIZE, pos_y - 2*CELL_SIZE)
            elif index == 7: # Middle_Right
                position = Point(pos_x + CELL_SIZE, pos_y - CELL_SIZE)
            elif index == 8: # Bottom_Right
                position = Point(pos_x + CELL_SIZE, pos_y)
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

