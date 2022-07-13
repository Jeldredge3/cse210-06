from constants import *
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
        p_body = player.get_segments()[0:]
        score = cast.get_first_actor("score") 

        hitpoints = cast.get_first_actor("hitpoints")
        health = hitpoints.get_value()
        
        enemies = cast.get_actors("enemy")
        for enemy in enemies:
            e_body = enemy.get_segments()[0:]
            for e_segment in e_body:
                for p_segment in p_body:
                    if p_segment.get_position().equals(e_segment.get_position()):
                        
                        hitpoints._subtract(health)
                        score._add(100)
        #cast.remove_actor("player", player)


                
    def _handle_pickup_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        """
        player = cast.get_first_actor("player")
        p_body = player.get_segments()[0]
        p_segments = player.get_segments()[1:]

    def _handle_game_over(self, cast):
        """Shows the 'game over' message.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        if self._is_game_over:
            player = cast.get_first_actor("player")
            enemy = cast.get_actors("enemy")
            p_body = player.get_segments()[0]

            player.set




