# -------------------------------------------------------------------
# String Rendering Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import re
from .utilities import *

# Main Class
#===========
class Renderer:
    """ The Renderer take Mustache-styled strings and compute their
    variables. """

    # Properties
    ignore = True

    # Methods
    def __init__(self, ignore=True):
        self.ignore = bool(ignore)

    def render(self, text, variables):

        # Integers
        if is_number(variables):
            variables = str(variables)

        # If vars are dict
        if isinstance(variables, dict):
            return self.__applyDict(text, variables)

        # If vars are tuple or array
        if is_of_list(variables):
            return self.__applyList(text, variables)

        # If vars are strings
        if is_string(variables):
            return self.__applyString(text, variables)

        return text


    def __applyDict(self, text, variables):
        for key, value in list(variables.items()):
            text = re.sub('\{\{'+key+'\}\}', str(value), text)
        if not self.ignore:
            text = re.sub('\{\{[^}]+\}\}', '', text)
        return text

    def __applyList(self, text, variables):
        search = re.findall('\{\{([^}]+)\}\}', text)
        for i in range(0, len(variables)):
            try:
                text = re.sub('\{\{'+search[i]+'\}\}', str(variables[i]), text)
            except IndexError:
                pass
        return text

    def __applyString(self, text, variable):
        return re.sub('\{\{[^}]+\}\}', variable, text)