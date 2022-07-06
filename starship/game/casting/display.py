import constants
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Display(Actor):
    """A heads-up display (HUD) element in the game. Displays the name of the element along with it's value. 

    Attributes:
        _name:
        _text:              The name of the HUD element which is displayed.
        _value:             The string value that is displayed next to the text.
        _total_points:      An integer value which is updated with the add() & subtract() methods.
        _self.set_text():   String display containing the element's text and value.
    """
    def __init__(self):
        super().__init__()
        self._name = " "
        self._value = 0
        self._max_limit = float('inf')
        self.set_text(f"{self._name}: {self._value}")

    def _prepare_self(self, pos_x, pos_y, set_color):
        """Places the element at the position that was passed through.
        """
        self._position = Point(pos_x, pos_y)
        self._color = set_color
        self.set_position(self._position)

    def _get_name(self):
        return self._name

    def _get_value(self):
        return self._value

    def _get_max_limit(self):
        return self._max_limit

    def _add(self, points):
        """Adds the given points to the element's total points.
        """
        max_limit = self._get_max_limit()
        if self._value < max_limit:
            old_value = self._value
            self._value += points
            new_value = self._value
            print(f"{self._name}: {old_value} => {new_value}")
            # update display tracker
            self.set_text(f"{self._name}: {self._value}")
        else:
            print(f"{self._name}: {max_limit}")
        

    def _subtract(self, points):
        """Subracts the given points to the element's total points.
        """
        if self._value > 0:
            old_value = self._value
            self._value -= points
            new_value = self._value
            print(f"{self._name}: {old_value} => {new_value}")
            # update display tracker
            self.set_text(f"{self._name}: {self._value}")
        else:
            print(f"{self._name}: 0")
        #self.set_text(f"{self._text}: {self._total_points}")

class Lives(Display):
    """Keeps track of how many attempts the player has left.
    """
    def __init__(self):
        super().__init__()
        self._name = "Lives"
        self._value = constants.START_LIVES
        self._max_limit = constants.MAX_LIVES
        self.set_text(f"{self._name}: {self._value}")

class Hitpoints(Display):
    """Displays the player's health.
    """
    def __init__(self):
        super().__init__()
        self._name = "Hitpoints"
        self._value = constants.START_HITPOINTS
        self._max_limit = constants.MAX_HITPOINTS
        self.set_text(f"{self._name}: {self._value}")

class Score(Display):
    """A record of points made or lost. 
    """
    def __init__(self):
        super().__init__()
        self._name = "Score"
        self._points = 0
        self.set_text(f"{self._name}: {self._value}")

class Upgrades(Display):
    """Keeps track of the items picked up by the player.
    """
    def __init__(self):
        super().__init__()
        self._position = Point(0, 0)
        self._color = Color(30, 30, 30)
        self._name = "Upgrades"
        self._value = []
        self.set_text(f"{self._name}: {self._value}")

    def _add(self, list_element):
        """Appends a new element to the list.
        """
        list_length = len(self._value)
        if list_length < constants.MAX_UPGRADES:
            self._value.append(list_element)
            self.set_text(f"{self._name}: {self._value}")

    def _subtract(self, amount_removed):
        """Removes a number of elements from the list.
        """
        list_length = len(self._value)
        for i in range(amount_removed): 
            if list_length > 0:
                self._value.pop(-1)
                self.set_text(f"{self._name}: {self._value}")
            else:
                break
    
    def _remove(self, list_element):
        """Removes a specific element from the list.
        """
        self._value.remove(list_element)
        self.set_text(f"{self._name}: {self._value}")

    def _update(self, mode):
        """Updates the display to reflect correct information.
        """
        if mode == 0:
            self._value.append("BasicShot")
        elif mode == 1:
            self._value.append("MultiShot")
        elif mode == 2:
            self._value.append("LongShot")
        elif mode == 3:
            self._value.append("FlameThrower")
        self.set_text(f"{self._name}: {self._value}")