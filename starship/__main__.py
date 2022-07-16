import random
from constants import *

from game.casting.cast import Cast
from game.casting.player_spaceship import Player
from game.casting.enemy_spaceship import Enemy
from game.casting.display import Display, BooleanDisplay, VariableDisplay, ListDisplay
from game.casting.particle_effects import Particle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorPlayer, ResetActorPositions
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.handle_game_updates import HandleGameUpdates
from game.scripting.handle_out_of_bounds import HandleOutofBounds
from game.scripting.handle_timed_events import HandleTimedEvents
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
    half_x = int(MAX_X / 2)
    half_y = int(MAX_Y / 2)
    # set the position for random locations, but only in increments of the cell size.
    increment = CELL_SIZE
    rand_x = random.randrange(0, MAX_X, increment)
    rand_y = random.randrange(0, MAX_Y, increment)
    x = increment * round(half_x/increment)
    y = increment * round(half_y/increment)

    # create the players.
    player = Player()
    cast.add_actor("player", player)
    # set the positon and color of the player. 
    player._build_ship(x, y, WHITE)
    
    """
    # create an enemy.
    enemy = Enemy()
    cast.add_actor("enemy", enemy)
    # set the positon and color of the enemy. 
    enemy._build_ship(rand_x, 2*CELL_SIZE, RED)
    """
    
    # create background star particle effects
    for i in range(BACKGROUND_STAR_AMOUNT):
        star = Particle()
        cast.add_actor("particle", star)
        star.randomize()

    # create the scoreboard and other HUD elements.
    score = VariableDisplay()
    hitpoints = VariableDisplay()
    lives = VariableDisplay()
    upgrades = ListDisplay()
    log_position = Display()
    log_bullet_position = Display()
    log_collision = Display()
    timer_infinite = VariableDisplay()
    timer_loop = VariableDisplay()
    timer_respawn = VariableDisplay()
    # add each new object to the cast to allow retrieval outside of this file.
    cast.add_actor("score", score)
    cast.add_actor("hitpoints", hitpoints)
    cast.add_actor("lives", lives)
    cast.add_actor("upgrades", upgrades)
    cast.add_actor("log_pos", log_position)
    cast.add_actor("log_bul", log_bullet_position)
    cast.add_actor("log_col", log_collision)
    cast.add_actor("timer_inf", timer_infinite)
    cast.add_actor("timer_loop", timer_loop)
    cast.add_actor("timer_respawn", timer_respawn)
    # set the positon and color of the HUD elements. 
    lives.prepare_self(20, 4, BLUE, "Lives")
    hitpoints.prepare_self(540, 4, RED, "Hitpoints")
    score.prepare_self(1040, 4, GREEN, "Score")
    upgrades.prepare_self(20, 40, GOLD, "Upgrades")
    # set up the console log visual tools.
    log_position.prepare_self(980, MAX_Y - 40, BLACK, "log_Pos")
    log_bullet_position.prepare_self(980, MAX_Y - 80, BLACK, "log_Bul")
    log_collision.prepare_self(980, MAX_Y - 120, BLACK, "log_Col")
    # set up the timers.
    timer_infinite.prepare_self(20, MAX_Y - 40, BLACK, "timer_inf")
    timer_loop.prepare_self(20, MAX_Y - 80, BLACK, "timer_loop")

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorPlayer(keyboard_service))
    script.add_action("input", ResetActorPositions(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", HandleGameUpdates())
    script.add_action("update", HandleOutofBounds())
    script.add_action("update", HandleTimedEvents())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()