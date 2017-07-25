""" This module contains a class which is used to represent the participating players in a game."""

import telegram

import godfather.role


class Player:
    """ Every instance of the class Player represents one player in the game.

    The instance is initialized with information about the user itself;
    game related information is added later.

    Args:
        telegram_user (telegram.user.User): An object from the Telegram API
            to identify the Telegram account of the player
        
    Attributes:
        user (telegram.user.User): Specific information about the actual user
        role (role.Role): All game related information is saved here
    """
    def __init__(self, telegram_user, role = None):
        #  telegram.user.User Objects contain the following arguments:

        # id              -- unique ID that is required to send text messages
        # language_code   -- language code chosen by the given user
        # first_name      -- first name of user
        # last_name       -- last name of user (optional)
        # username        -- unique Telegram tag (optional)
        # name            -- equals username if available (with @ sign),  
        #                    otherwise first name + last name
        self.user = telegram_user
        self.role = role
