from constants import *
import time
import random
from game.casting.actor import Actor
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
        self.unpaused = True

class ResetActorPositions(ControlActorsAction):
    """Reset the positions of both players when pressing ' '.

    NOTE: does not work at this time.
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

        if self._keyboard_service.is_key_down('e'):
            # pause the game when 'e' is pressed.
            self.pause_game(cast, True)
            self.unpaused = False
        
        if self._keyboard_service.is_key_down("r"):
            # if game is paused, unpase the game when 'r' is pressed.
            if self.unpaused == False:
                self.pause_game(cast, False)
                self.unpaused == True

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
            if self._keyboard_service.is_key_down('q'):
                player._cycle_mode()
    
    def pause_game(self, cast, boolean):
        """Pauses all movement in the game until function is called again.
        """
        pause_game = boolean

        # get display elements
        score = cast.get_first_actor("score")
        hitpoints = cast.get_first_actor("hitpoints")
        lives = cast.get_first_actor("lives")
        # get ship objects
        player = cast.get_first_actor("player")
        enemies = cast.get_actors("enemy")
        particles = cast.get_actors("particle")
        # get timers
        timer_infinite = cast.get_first_actor("timer_inf")
        timer_loop = cast.get_first_actor("timer_loop")
        timer_respawn = cast.get_first_actor("timer_respawn")

        if pause_game == True:
            # lock score, hitpoints, and lives
            score._lock_value(True)
            hitpoints._lock_value(True)
            lives._lock_value(True)
            # lock player, enemy, and particle movement 
            player.toggle_movement(False)
            player.toggle_fire(False)
            for enemy in enemies:
                enemy.toggle_movement(False)
            for particle in particles:
                particle.toggle_movement(False)
            # lock timers
            timer_infinite._lock_value(True)
            timer_loop._lock_value(True)
            timer_respawn._lock_value(True)

            # create a message annoucing the game is paused.
            x = int(MAX_X / 2)
            y = int(MAX_Y / 2)
            position = Point(x, y)
            message = Actor()
            message.set_text("Paused")
            message.set_position(position)
            message.set_color(YELLOW)
            cast.add_actor("messages", message)
        

        if pause_game == False:
            # unlock score, hitpoints, and lives
            score._lock_value(False)
            hitpoints._lock_value(False)
            lives._lock_value(False)
            # unlock player, enemy, and particle movement 
            player.toggle_movement(True)
            player.toggle_fire(True)
            for enemy in enemies:
                enemy.toggle_movement(True)
            for particle in particles:
                particle.toggle_movement(True)
            # unlock timers
            timer_infinite._lock_value(False)
            timer_loop._lock_value(False)
            timer_respawn._lock_value(False)

            # remove the pause game message.
            all_messages = cast.get_actors("messages")
            if len(all_messages) > 0:
                game_message = cast.get_first_actor("messages")
                cast.remove_actor("messages", game_message)