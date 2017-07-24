''' This module contains a class which is used to represent the participating players in a game.'''

import telegram

import godfather.role

class Player:
    ''' Every instance of the class Player represents one player in the game.
        The instance is initialized with information about the user itself;
        game related information is added later.
        
        Attributes:
            user (telegram.user.User) -- Specific information about the actual user
            role (role.Role)          -- All game related information is saved here
            
        Methods:
            assignrole(self, role)    -- Sets self.role to a given role
    '''

    def __init__(self, telegram_user):

        if isinstance(id, telegram.user.User): 
            self.user = telegram_user
            ''' telegram.user.User Objects contain the following arguments:

                id              -- unique ID that is required to send text messages
                language_code   -- language code chosen by the given user
                first_name      -- first name of user
                last_name       -- last name of user (optional)
                username        -- unique Telegram tag (optional)
                name            -- equals username if available (with @ sign), 
                                   otherwise first name + last name
            '''
        else:
            raise TypeError("A telegram-user object must be delivered")

        self.role = None

    def assignrole(self, role):
        ''' Sets self.role to a given role. 
        
            Is triggered in the pre-game phase for every single player and might be used by certain
            abilities within games.
        ''' 

        if isinstance(role, godfather.role.Role):
            self.role = role
        else:
            raise TypeError("Roles must be of type Role")