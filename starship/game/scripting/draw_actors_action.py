from constants import *
from game.scripting.action import Action

class DrawActorsAction(Action):
    """An output action that draws all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # ===== Get Player: Bullets, Segments ===== #
        player = cast.get_first_actor("player")
        p_segments = player.get_segments()
        p_bullets = player.get_bullets()

        # ===== Get Enemies: Segments ===== #
        enemies = cast.get_actors("enemy")
        for enemy in enemies:
            e_segments = enemy.get_segments()

        pickups = cast.get_actors("pickup")
        # ===== Get HUD Elements ===== #
        score = cast.get_first_actor("score")
        hitpoints = cast.get_first_actor("hitpoints")
        lives = cast.get_first_actor("lives")
        upgrades = cast.get_first_actor("upgrades")
        log_positon = cast.get_first_actor("log_pos")
        log_bullet_position = cast.get_first_actor("log_bul")
        log_collision = cast.get_first_actor("log_col")
        timer = cast.get_first_actor("timer")
        messages = cast.get_actors("messages")

        # ===== Clear Screen & Draw Actors ===== #
        # ---
        self._video_service.clear_buffer()
        # player related actors
        self._video_service.draw_actor(player)
        self._video_service.draw_actors(p_segments)
        self._video_service.draw_actors(p_bullets, True)
        # other actors
        self._video_service.draw_actors(enemies)
        self._video_service.draw_actors(e_segments)
        self._video_service.draw_actors(pickups)
        # interface actors
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(hitpoints)
        self._video_service.draw_actor(lives)
        self._video_service.draw_actor(upgrades)
        self._video_service.draw_actors(messages, True)
        # console log actors
        if SHOW_CONSOLE_LOG == True:
            self._video_service.draw_actor(log_positon)
            self._video_service.draw_actor(log_bullet_position)
            self._video_service.draw_actor(log_collision)
            self._video_service.draw_actor(timer)
        # ---
        self._video_service.flush_buffer()