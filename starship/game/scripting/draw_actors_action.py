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
        player = cast.get_first_actor("player")
        p1_segments = player.get_segments()
        p1_bullets = player.get_bullets()

        enemies = cast.get_actors("enemy")
        pickups = cast.get_actors("pickup")
        
        score = cast.get_first_actor("score")
        hitpoints = cast.get_first_actor("hitpoints")
        lives = cast.get_first_actor("lives")
        upgrades = cast.get_first_actor("upgrades")
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(player)
        self._video_service.draw_actors(p1_segments)
        self._video_service.draw_actors(p1_bullets, True)

        self._video_service.draw_actors(pickups)
        self._video_service.draw_actors(enemies)

        self._video_service.draw_actor(score)
        self._video_service.draw_actor(hitpoints)
        self._video_service.draw_actor(lives)
        self._video_service.draw_actor(upgrades)

        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()