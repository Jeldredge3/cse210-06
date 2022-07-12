import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """An update action that handles interactions between the actors.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_destroyed = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_destroyed:
            self._handle_segment_collision(cast)
            ###self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        """
        player = cast.get_first_actor("player")
        p_body = player.get_segments()[0]
        p_segments = player.get_segments()[1:]

    def _handle_pickup_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        """
        player = cast.get_first_actor("player")
        p_body = player.get_segments()[0]
        p_segments = player.get_segments()[1:]
        


