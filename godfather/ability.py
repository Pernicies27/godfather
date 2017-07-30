"""This module provides abilities which are essentially anything a player can do."""
from abc import ABC, abstractmethod


class Ability(ABC):
    """An ability is something a player can do during a specific phase.

    Even very common actions such as voting are abilities.

    Note that there must be one instance of an ability per player.

    Args:
        store (n/a yet): An object which allows retrieving and changing the game state
        send_message (function): A function which can be used to send a message to the player
            who has this ability
    """
    def __init__(self, store, send_message):
        self._store = store
        self._send_message = send_message

    @abstractmethod
    def _is_executable(self, game_state):
        """Check whether the current game state allows this ability to be used.

        Note that this method is not responsible for making sure the current phase
        is one in which the ability can be used.

        Args:
            game_state (godfather.game_state.GameState): The current state of the game

        Returns:
            bool: True if the ability can be used, otherwise false
        """
        pass

    @abstractmethod
    def _execute(self):
        """Use the ability.
        This must not be called unless the ability may actually be used.
        """
        pass

    def call(self):
        """Use the ability if possible.
        This method must not be called in a phase in which the ability can't be used.
        """
        if self._is_executable(self._store.get_state()):
            self._execute()

    def on_input(input):
        """Handle user input."""
