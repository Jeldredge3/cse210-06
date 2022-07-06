import constants
from game.scripting.action import Action
from game.shared.point import Point

class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        player = cast.get_first_actor("player")

        # ===== Move Bullets ===== #
        bullets = player.get_bullets()
        for bullet in bullets:
            bullet._distance_counter += 1
            # bullets are destroyed after reaching their max range.
            if bullet._distance_counter < bullet._range:
                bullet.move_next()
            else:
                bullets.pop(0)
                
            