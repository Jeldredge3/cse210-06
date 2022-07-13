import constants
import random

from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.enemies import Enemy
from game.casting.display import Display, VariableDisplay, ListDisplay
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
    half_x = int(constants.MAX_X / 2)
    half_y = int(constants.MAX_Y / 2)
    # set the position for random locations, but only in increments of the cell size.
    increment = constants.CELL_SIZE
    rand_x = random.randrange(0, constants.MAX_X, increment)
    rand_y = random.randrange(0, constants.MAX_Y, increment)
    # round the half-way points to the nearest increment.
    x = increment * round(half_x/increment)
    y = increment * round(half_y/increment)

    # create the players.
    player = Player()
    cast.add_actor("player", player)
    # set the positon and color of the player. 
    player._build_ship(x, y, constants.WHITE)
    
    # create an enemy.
    enemy = Enemy()
    cast.add_actor("enemy", enemy)
    # set the positon and color of the enemy. 
    enemy._build_ship(rand_x, 2*constants.CELL_SIZE, constants.RED)

    # create the scoreboard and other HUD elements.
    score = VariableDisplay()
    hitpoints = VariableDisplay()
    lives = VariableDisplay()
    upgrades = ListDisplay()
    log_position = Display()
    log_collision = Display()
    cast.add_actor("score", score)
    cast.add_actor("hitpoints", hitpoints)
    cast.add_actor("lives", lives)
    cast.add_actor("upgrades", upgrades)
    cast.add_actor("log_pos", log_position)
    cast.add_actor("log_col", log_collision)
    # set the positon and color of the HUD elements. 
    lives.prepare_self(20, 4, constants.BLUE, "Lives")
    hitpoints.prepare_self(540, 4, constants.RED, "Hitpoints")
    score.prepare_self(1040, 4, constants.GREEN, "Score")
    upgrades.prepare_self(20, 40, constants.GOLD, "Upgrades")
    log_position.prepare_self(980, 40, constants.BLACK, "log_Pos")
    log_collision.prepare_self(980, 80, constants.BLACK, "log_Col")

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