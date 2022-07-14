from constants import *
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Display(Actor):
    """Represents a heads-up display (HUD). Displays the name of a statistic along with it's value. 

    Attributes:
        _name:              The name of the HUD element which is displayed.
        _value:             The string value that is displayed next to the text.
    """
    def __init__(self):
        super().__init__()
        self._name = "Unknown"
        self._value = None
        self.update_display()

    def update_display(self):
        self.set_text(f"{self._name}: {self._value}")

    def prepare_self(self, pos_x, pos_y, color, name):
        """Places the element at the position that was passed through.
        """
        self._position = Point(pos_x, pos_y)
        self._color = color
        self._name = name
        self.set_position(self._position)
        self.update_display()

    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value

    def set_name(self, name):
        self._name = name
        self.update_display()

    def set_value(self, value):
        self._value = value
        self.update_display()

class VariableDisplay(Display):
    """A heads-up display (HUD) element in the game which displays an integer value.

    Attributes:
        _name:              The name of the HUD element which is displayed.
        _value:             The string value that is displayed next to the text.
        _max_limit:         An integer value which is updated with the add() & subtract() methods.
        _lock:              A boolean variable which determines whether or not the objects value can be changed.
    """
    def __init__(self):
        super().__init__()
        self._name = "Integer"
        self._value = 0
        self._max_limit = float('inf')
        self._lock = False
        self.update_display()

    def prepare_self(self, pos_x, pos_y, set_color, name):
        """Places the element at the position that was passed through.
        """
        self._position = Point(pos_x, pos_y)
        self._color = set_color
        self._name = name
        if name == "Lives":
            self._value = START_LIVES
            self._max_limit = MAX_LIVES
        elif name == "Hitpoints":
            self._value = START_HITPOINTS
            self._max_limit = MAX_HITPOINTS
        elif name == "Score":
            self._value = 0
            self._max_limit = float('inf')

        self.set_position(self._position)
        self.update_display()
        
    def get_max_limit(self):
        return self._max_limit

    def _lock_value(self):
        self._lock = True

    def _unlock_value(self):
        self._lock = False

    def _add(self, points):
        """Adds the given points to the element's total points.
        """
        max_limit = self.get_max_limit()
        if self._lock == False:
            if self._value < max_limit:
                old_value = self._value
                self._value += points
                new_value = self._value
                if SHOW_UPDATES_IN_TERMINAL == True:
                    print(f"{self._name}: {old_value} => {new_value}")
                # update display tracker
                self.update_display()
            else:
                if SHOW_UPDATES_IN_TERMINAL == True:
                    print(f"{self._name}: {max_limit}")
        else:
            pass

    def _subtract(self, points):
        """Subracts the given points to the element's total points.
        """
        if self._lock == False:
            if self._value > 0:
                old_value = self._value
                self._value -= points
                new_value = self._value
                if SHOW_UPDATES_IN_TERMINAL == True:
                    print(f"{self._name}: {old_value} => {new_value}")
                # update display tracker
                self.update_display()
            else:
                if SHOW_UPDATES_IN_TERMINAL == True:
                    print(f"{self._name}: 0")
        else:
            pass

class ListDisplay(Display):
    """A heads-up display (HUD) element in the game which displays an list for it's value.

    Attributes:
        _name:              The name of the HUD element which is displayed.
        _value:             The string value that is displayed next to the text.
    """
    def __init__(self):
        super().__init__()
        self._name = "List"
        self._value = []
        self.update_display()

    def _add(self, list_element):
        """Appends a new element to the list.
        """
        list_length = len(self._value)
        if list_length < MAX_UPGRADES:
            self._value.append(list_element)
            self.update_display()

    def _subtract(self, amount_removed):
        """Removes a number of elements from the list.
        """
        list_length = len(self._value)
        for i in range(amount_removed): 
            if list_length > 0:
                self._value.pop(-1)
                self.update_display()
            else:
                break

    def _update_mode(self, mode):
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
        self.update_display()