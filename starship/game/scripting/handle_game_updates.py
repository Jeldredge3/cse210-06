from constants import *
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
        self._allow_log_updates = True

    def execute(self, cast, script):
        player = cast.get_first_actor("player")
        p_bullets = player.get_bullets()
        p_segments = player.get_segments()
        hitpoints = cast.get_first_actor("hitpoints")
        score = cast.get_first_actor("score")
        lives = cast.get_first_actor("lives")
        current_hp = hitpoints.get_value()
        current_score = score.get_value()
        current_lives = lives.get_value()
        enemies = cast.get_actors("enemy")

        if not self._is_game_over:
            # check if player hitpoints have fallen to zero.
            if current_hp <= 0:
                # change the player's ship to black.
                for segment in p_segments:
                    segment.set_color(BLACK)
                player.destroy_self()
            else:
                # restore the player's ship's color to white.
                for segment in p_segments:
                    segment.set_color(WHITE)
                    

            # check if the player's lives and hitpoints have fallen to zero.
            if current_lives <= 0 and current_hp <= 0:
                self._is_game_over = True
                self._handle_game_over(cast)
                # change the player's ship to gray.
                for segment in p_segments:
                    segment.set_color(BLACK)
            
            if current_score >= SCORE_TO_WIN:
                self._victory = True
                self._is_game_over = True
                self._handle_game_over(cast)

            # check if an enemy is destroyed.
            for enemy in enemies:
                if enemy._is_destroyed == True:
                    cast.remove_actor("enemy", enemy)

            # updates the console log display features meant to help with testing.
            if SHOW_CONSOLE_LOG == True:
                log_position = cast.get_first_actor("log_pos")
                p_coord = p_segments[0].get_position()
                player_x = p_coord.get_x()
                player_y = p_coord.get_y()
                log_position.set_value(f"({player_x}, {player_y})")
                if len(p_bullets) > 0:
                    log_bullet_position = cast.get_first_actor("log_bul")
                    bullet_pos = p_bullets[0].get_position()
                    bullet_x = bullet_pos.get_x()
                    bullet_y = bullet_pos.get_y()
                    log_bullet_position.set_value(f"({bullet_x}, {bullet_y})")

    def _handle_game_over(self, cast):
        """Shows the 'game over' message when the player loses all lives.
        """
        player = cast.get_first_actor("player")
        p_segments = player.get_segments()
        hitpoints = cast.get_first_actor("hitpoints")
        score = cast.get_first_actor("score")
        lives = cast.get_first_actor("lives")

        if self._is_game_over:
            x = int(MAX_X / 2)
            y = int(MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            if self._victory == True:
                message.set_text(f"Victory!")
                
        player.toggle_fire(False)
        for segment in p_segments:
            segment.set_color(BLACK)

        score._lock_value(True)
        hitpoints._lock_value(True)
        lives._lock_value(True)