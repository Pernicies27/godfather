"""This module is responsible for managing the passage of time in form of phases
    as well as provide the possibility to store and manage specific points in time in a game.
"""
import collections
from abc import ABC, abstractmethod


Timestamp = collections.namedtuple('Timestamp', ['phase_number', 'cycle_number'])
Timestamp.__doc__ = """A timestamp represents one specific point in time in a game.
It consists of a phase as well as the number of completed cycles.

Attributes:
    phase_number (int): The index of the current phase (beginning with 0)
    cycle_number (int): The number of completed cycles

Args:
    phase_number (int): The index of the current phase (beginning with 0)
    cycle_number (int): The number of completed cycles
"""


class Phase(ABC):
    """A Phase is a section of a complete day/night cycle.
    With each phase is associated a list of abilities that can be used during that phase.

    Attributes:
        timeout (int): The number of seconds after which the phase will be forced to end

    Args:
        timeout (int): The number of seconds after which the phase will be forced to end.
            0 means disabled (phase will continue until end condition is met)
    """
    def __init__(self, timeout=0):
        self.timeout = timeout

    @abstractmethod
    def is_finished(game_state, abilities):
        """Check whether the phase is finished and the next phase can be started.

        This method uses the entire game_state and the list of abilities associated with the phase
        to check whether all actions have been completed.

        Returns:
            bool: True if the phase is completed, false if it's still ongoing

        Args:
            game_state (godfather.game_state.GameState): The entire state of the current game
            abilities (list of abilities): A list of abilities that can be used during the phase
        """
        pass
