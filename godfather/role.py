''' This module contains the class Role which is used to save 
    all game related information about a player '''


class Role:
    ''' Every instance of the class Role represents a role a player has.
        All information, i.e. abilties, victory conditions, rolenames etc.,
        is included as arguments. 

        Arguments:
            faction_name (str)     -- Name of the faction (e.g. "Mafia")
            role_name    (str)     -- Name of the role (e.g. "Vigilante")
            win_con      (n/a yet) -- Implementation of the victory condition of a player
            abilities    (list)    -- Each element represents an ability a player has

        Methods:
            set_faction_name(self, faction_name) -- Sets the faction_name of a role
            set_role        (self, role_name)    -- Sets the role_name of a role
            set_win_con     (self, win_con)      -- Sets the win_con of a role
            add_ability     (self, ability)      -- Adds an ability to a role
    '''

    def __init__(self, win_con):
        self.faction_name = None
        self.role_name = None
        self.win_con = None
        self.abilities = []

    def set_faction_name(self, faction_name):
        ''' Sets the faction_name of a role '''

        if isinstance(faction_name, str):
            self.faction_name = faction_name
        else:
            raise TypeError("Rolenames must be Strings")

    def set_role_name(self, role_name):
        ''' Sets the role_name of a role '''

        if isinstance(role_name, str):
            self.role_name = role_name
        else:
            raise TypeError("Rolenames must be Strings")

    def set_win_con(self, win_con):
        ''' Sets the victory condition of a role.

            To be implemented
        '''
        pass

    def add_ability(self, ability):
        ''' Adds an ability to a role.
        
            Abbility class not implemented yet.
        '''
        self.abilities.append(ability)
    