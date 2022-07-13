import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        # ===== Default Kebindings ===== #
        self._keys['up'] = pyray.KEY_UP 
        self._keys['left'] = pyray.KEY_LEFT 
        self._keys['down'] = pyray.KEY_DOWN 
        self._keys['right'] = pyray.KEY_RIGHT
        # ===== Temporary Kebindings ===== #
        # ===== Temporary Kebindings ===== #
        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['o'] = pyray.KEY_O
        self._keys['k'] = pyray.KEY_K
        self._keys['p'] = pyray.KEY_P
        self._keys['l'] = pyray.KEY_L
        self._keys['['] = pyray.KEY_LEFT_BRACKET
        self._keys[']'] = pyray.KEY_RIGHT_BRACKET
        # ===== Player Movement Kebindings ===== #
        self._keys['w'] = pyray.KEY_W # Player Up
        self._keys['a'] = pyray.KEY_A # Player Left
        self._keys['s'] = pyray.KEY_S # Player Down
        self._keys['d'] = pyray.KEY_D # Player Right 
        # ===== Player Action Kebindings ===== #
        self._keys['space'] = pyray.KEY_SPACE # Player Shoot
        self._keys['e'] = pyray.KEY_E
        self._keys['p'] = pyray.KEY_P # Pause Game
        self._keys['tab'] = pyray.KEY_TAB # ConsoleLog Help - Print Player

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)