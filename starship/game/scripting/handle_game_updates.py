import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleGameUpdates(Action):
    """An update action that checks the players health and lives to see if the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """
    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._victory = False

    def execute(self, cast, script):
        player = cast.get_first_actor("player")
        hitpoints = cast.get_first_actor("hitpoints")
        lives = cast.get_first_actor("lives")
        current_hp = hitpoints.get_value()
        current_lives = lives.get_value()

        if not self._is_game_over:
            # check if player hitpoints have fallen to zero.
            if current_hp <= 0:
                # change the player's ship to black.
                ship_parts = player.get_segments()
                for part in ship_parts:
                    part.set_color(constants.BLACK)
                # reset the player's hitpoints to full, subtract one life from the player.
                hitpoints._add(constants.RESPAWN_HITPOINTS)
                lives._subtract(1)
            else:
                # restore the player's ship's color to white.
                ship_parts = player.get_segments()
                for part in ship_parts:
                    part.set_color(constants.WHITE)

            # check if the player's lives and hitpoints have fallen to zero.
            if current_lives <= 0 and current_hp <= 0:
                self._is_game_over = True
                self._handle_game_over(cast)
                # change the player's ship to black.
                ship_parts = player.get_segments()
                for part in ship_parts:
                    part.set_color(constants.BLACK)
                player.toggle_fire(False)

    def _handle_game_over(self, cast):
        """Shows the 'game over' message when the player loses all lives.
        """
        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            player = cast.get_first_actor("player")
            player.set_color = constants.BLACK

            if self._victory == True:
                message.set_text(f"Victory!")

