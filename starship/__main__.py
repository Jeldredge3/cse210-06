import constants

from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.enemies import Enemy
from game.casting.display import Score, Hitpoints, Lives, Upgrades 
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorPlayer
from game.scripting.control_actors_action import ResetActorPositions
from game.scripting.control_actors_action import PrintPlayer
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.handle_game_updates import HandleGameUpdates
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    # define the half-way point on the grid.
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    # create the players.
    player = Player()
    cast.add_actor("player", player)
    # set the positon and color of the player. 
    player._prepare_body(x, y, constants.WHITE)
    
    # create the scoreboard and other HUD elements.
    score = Score()
    hitpoints = Hitpoints()
    lives = Lives()
    upgrades = Upgrades()
    cast.add_actor("score", score)
    cast.add_actor("hitpoints", hitpoints)
    cast.add_actor("lives", lives)
    cast.add_actor("upgrades", upgrades)
    # set the positon and color of the HUD elements. 

    lives._prepare_self(20, 4, constants.BLUE)
    hitpoints._prepare_self(540, 4, constants.RED)
    score._prepare_self(1040, 4, constants.GREEN)
    upgrades._prepare_self(20, 40, constants.GOLD)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorPlayer(keyboard_service))
    script.add_action("input", ResetActorPositions(keyboard_service))
    script.add_action("input", PrintPlayer(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", HandleGameUpdates())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()