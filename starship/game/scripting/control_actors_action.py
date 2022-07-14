from constants import *
import time
import random
from game.scripting.action import Action
from game.shared.point import Point

class ControlActorsAction(Action):
    """An input action that controls movement of an actor.
    The responsibility of ControlActorsAction is to get the direction and move the player's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(CELL_SIZE, 0)
            
class ResetActorPositions(ControlActorsAction):
    """Reset the positions of both players when pressing 'space'.
    """
    def execute(self, cast, script):
        # ============ PLAYER ONE ============ #

        if self._keyboard_service.is_key_down('p'):
            p1 = cast.get_first_actor("player")
            p1_segments = p1.get_segments()

            # Reposition Player back to their starting positon.
            p1_body = p1.get_body()
            p1_start = p1.get_start_position()
            p1_body.set_position(p1_start)

        if self._keyboard_service.is_key_up('e'):
            p1 = cast.get_first_actor("player")

class ControlActorPlayer(ControlActorsAction):
    """Conrols the movement of the Player with W, A, S, D.
    """
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # ===== PLAYER MOVEMENT KEYS ===== #
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-CELL_SIZE, 0)
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(CELL_SIZE, 0)
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -CELL_SIZE)
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, CELL_SIZE)

        # change direction based on key press.
        player = cast.get_first_actor("player")
        player.turn_ship(self._direction)
        # move the player only when a movement key is being pressed.
        if self._keyboard_service.is_key_down('a') or self._keyboard_service.is_key_down('d') or self._keyboard_service.is_key_down('w') or self._keyboard_service.is_key_down('s'):
            player.move_next()

        # ===== PLAYER ACTION KEYS ===== #
        # shoot with 'space', creates a projectile at the ship's location.
        if self._keyboard_service.is_key_down('space'):
            player = cast.get_first_actor("player")
            ship = player.get_body()
            ship_pos = ship.get_position()
            pos_x = ship_pos.get_x()
            pos_y = ship_pos.get_y()
            player.shoot(pos_x, pos_y - 2*CELL_SIZE)

        # ===== PROGRAM TESTING COMMANDS ===== #
        score = cast.get_first_actor("score")
        hitpoints = cast.get_first_actor("hitpoints")
        lives = cast.get_first_actor("lives")
        upgrades = cast.get_first_actor("upgrades")

        if ALLOW_CHEATS == True:
            # lives - add
            if self._keyboard_service.is_key_down('i'):
                lives._add(1)
            # lives - subtract
            if self._keyboard_service.is_key_down('j'):
                lives._subtract(1)
            # hitpoints - add
            if self._keyboard_service.is_key_down('o'):
                hitpoints._add(10)
            # hitponts - subtract
            if self._keyboard_service.is_key_down('k'):
                hitpoints._subtract(10)
            # score - add
            if self._keyboard_service.is_key_down('p'):
                score._add(15)
            # score - subtract
            if self._keyboard_service.is_key_down('l'):
                score._subtract(15)

            # inventory - append random item to list
            upgrades_list = ["Laser Cannon", "Multi-Shot", "Rapid-Fire", "Overshield"]
            rand_selection = random.choice(upgrades_list)
            if self._keyboard_service.is_key_down(']'):
                player._cycle_mode()
            # inventory - remove last item from list
            if self._keyboard_service.is_key_down('['):
                pass
