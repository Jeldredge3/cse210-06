import constants
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Enemy(Actor):
    """Creates an instance of the Pickup class which can interact with the player upon collision.
    """
    def __init__(self):
        super().__init__()
        self._value = 0
        self._is_destroyed = False
        # ===== Ship Parts ===== #
        """Ship segments goes in this order: 
        [Center, Middle, Front, Top-Left, Middle-left, Bottom-Left, Top-Right, Middle-Right, Bottom-Right]
        """
        self._ship_blueprint_fighter = ["", "O", "", "/", "|-", "\\", "\\", "-|", "/"]
        self._segments = []

    def _build_ship(self, pos_x, pos_y, set_color):
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
        for ship_part in self._ship_blueprint_fighter:
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
    
    def get_segments(self):
        return self._segments

    def get_body(self):
        return self._segments[0]

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