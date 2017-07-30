"""This module is responsible for representing the entire state of a game"""


class GameState:
    """Represent the state of a game.

    The state of a game includes everything you would need to know
    if you wanted to continue a game previously paused.

    This includes the list of players with all their attributes,
    the current game phase (not just day/night, but also information
    about which abilities were already used in this phase)
    and the number of completed day/night cycles.

    It does not include a complete history of the game.

    Args:
        players (godfather.player.Player[]): The complete list of players participating,
            including dead players.
        timestamp (n/a yet): A timestamp containing the current phase
            as well as the total number of days/nights played
    """
    def __init__(self, players, timestamp):
        self.players = players
        self.timestamp = timestamp
