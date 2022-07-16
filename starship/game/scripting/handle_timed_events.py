import random
from constants import *

from game.casting.actor import Actor
from game.casting.enemy_spaceship import Enemy, BonusEnemy
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
        
        enemies = cast.get_actors("enemy")

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
            player.toggle_fire(False)
            hitpoints._lock_value(True)
            score._lock_value(True)
            lives._lock_value(True)
            timer_respawn._add(1)
            # once the counter reaches 10, the player is restored back to their original state.
            if respawn_time >= 10:
                timer_respawn._reset_value()
                timer_respawn._lock_value(True)
                player.toggle_fire(True)
                hitpoints._lock_value(False)
                score._lock_value(False)
                lives._lock_value(False)
                # subtract one life from the player, restore the player to full health.
                lives._subtract(1)
                hitpoints._add(RESPAWN_HITPOINTS)
                player.repair_self()
        else:
            timer_respawn._lock_value(False)

        # EVENT 1) creates an enemy when each time event has passed. 
        timer_event_list = [0]
        timer_event_frequency = 50
        timer_event_length = 3000
        counter = 0

        # add time events to the time_event_list up until the maximum set length of the timer.
        while counter < timer_event_length:
            counter += timer_event_frequency
            timer_event_list.append(counter)

        if inf_growing_time in timer_event_list:
            for time_event in timer_event_list:
                if inf_growing_time == time_event: 
                    # create an enemy.
                    enemy = Enemy()
                    cast.add_actor("enemy", enemy)
                    # set the positon and color of the enemy. 
                    self.rand_x = random.randrange(0, MAX_X, CELL_SIZE)
                    enemy._build_ship(self.rand_x, 2*CELL_SIZE, RED)

        # EVENT 2) creates special enemies when each time event has passed.
        timer_event_list2 = [300, 900, 1200, 1500, 1800]
        if inf_growing_time in timer_event_list2:
            for time_event in timer_event_list2:
                if inf_growing_time == time_event: 
                    # create an enemy.
                    enemy = BonusEnemy()
                    cast.add_actor("enemy", enemy)
                    # set the positon and color of the enemy. 
                    self.rand_x = random.randrange(0, MAX_X, CELL_SIZE)
                    enemy._build_ship(self.rand_x, 2*CELL_SIZE, PURPLE)