import random
from constants import *

from game.casting.actor import Actor
from game.casting.enemy_spaceship import Enemy
from game.scripting.action import Action
from game.shared.point import Point

#NOTE: This file does not work at this moment. 

class HandleTimedEvents(Action):
    """An update action that increases it's value, acting as a timer. Causes events at certain increments.
    """
    def __init__(self):
        """Constructs a new HandleTimedEvents."""
        half_x = int(MAX_X / 2)
        half_y = int(MAX_Y / 2)
        self.rand_x = random.randrange(0, MAX_X, CELL_SIZE)
        self.rand_y = random.randrange(0, MAX_Y, CELL_SIZE)
        self.mid_x = CELL_SIZE * round(half_x/CELL_SIZE)
        self.mid_y = CELL_SIZE * round(half_y/CELL_SIZE)

    def execute(self, cast, script):
        """Updates the timer by one point.
        """
        player = cast.get_first_actor("player")
        hitpoints = cast.get_first_actor("hitpoints")
        score = cast.get_first_actor("score")
        lives = cast.get_first_actor("lives")
        current_hp = hitpoints.get_value()
        current_score = score.get_value()
        current_lives = lives.get_value()
        
        timer_infinite = cast.get_first_actor("timer_inf")
        timer_loop = cast.get_first_actor("timer_loop")
        timer_respawn = cast.get_first_actor("timer_respawn")
        loop_time = timer_loop.get_value()
        inf_growing_time = timer_infinite.get_value()
        respawn_time = timer_respawn.get_value()

        timer_infinite._add(1)

        if loop_time < 10:
            timer_loop._add(1)
        else:
            timer_loop._reset_value()
            score._add(5)
            
        # EVENT - Player is destroyed) lock health, score, and lives values until player is repaired.
        if player._is_destroyed == True:
            print(f"Destroyed {respawn_time}")
            player.toggle_fire(False)
            hitpoints._lock_value(True)
            score._lock_value(True)
            lives._lock_value(True)
            timer_respawn._add(1)
            # once the counter reaches 10, the player is restored back to their original state.
            if respawn_time > 10:
                print(f"Repaired {respawn_time}")
                timer_respawn._reset_value()
                timer_respawn._lock_value(True)
                player.toggle_fire(True)
                hitpoints._lock_value(False)
                score._lock_value(False)
                lives._lock_value(False)
                lives._subtract(1)
                hitpoints._add(RESPAWN_HITPOINTS)
                player.repair_self()
        else:
            timer_respawn._lock_value(False)

        # EVENT 1) creates an enemy when 100 time has passed. 
        if inf_growing_time == 100:
            # create an enemy.
            enemy = Enemy()
            cast.add_actor("enemy", enemy)
            # set the positon and color of the enemy. 
            enemy._build_ship(self.rand_x, 2*CELL_SIZE, RED)