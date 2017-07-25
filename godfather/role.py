""" This module contains the class Role which is used to save 
    all game related information about a player
"""


class Role:
    """A combination of abilities, names and victory conditions of a player

    Args:
        faction_name (str)     -- Name of the faction (e.g. "Mafia")
        role_name    (str)     -- Name of the role (e.g. "Vigilante")
        win_con      (n/a yet) -- Implementation of the victory condition of a player
        abilities    (list)    -- Each element represents an ability a player has
    """
    def __init__(self, faction_name, role_name, win_con, abilities):
        self.faction_name = faction_name
        self.role_name = role_name
        self.win_con = win_con
        self.abilities = abilities


    def set_faction_name(self, faction_name):
        """Set the faction_name of a role"""
        self.faction_name = faction_name


    def set_role_name(self, role_name):
        """Set the role_name of a role"""
        self.role_name = role_name


    def set_win_con(self, win_con):
        """Set the victory condition of a role.

        To be implemented
        """
        pass


    def add_ability(self, ability):
        """ Adds an ability to a role"""
        self.abilities.append(ability)
    