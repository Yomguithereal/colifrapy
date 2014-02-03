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
from .utilities import is_of_list, is_number, is_string


# Constants
#==========
VAR_RE = r'\{\{(.*?)\}\}'


# Decorators
#===========
def ignoring(func):
    def _ignoring(self, *args, **kwargs):
        text = func(self, *args, **kwargs)
        return re.sub(VAR_RE, '', text) if self.ignore else text

    return _ignoring



# Main Class
#===========
class Renderer(object):
    """ The Renderer take Mustache-styled strings and render their
    variables. """

    # Methods
    def __init__(self, ignore=True):
        self.ignore = bool(ignore)

    def render(self, text, variables):

        # Integers
        if is_number(variables):
            variables = str(variables)

        # If vars are strings
        if is_string(variables):
            return self.__applyString(text, variables)

        # If vars are dict
        if isinstance(variables, dict):
            return self.__applyDict(text, variables)

        # If vars are tuple or array
        if is_of_list(variables):
            return self.__applyList(text, variables)

        return self.__ignoring(text)

    @ignoring
    def __applyString(self, text, variable):
        return re.sub(
            VAR_RE,
            variable,
            text,
            1
        )

    @ignoring
    def __applyList(self, text, variables):
        search = re.findall(VAR_RE, text)
        try:
            for i in range(0, len(variables)):
                text = re.sub(
                    re.compile('\{\{' + search[i] + '\}\}'),
                    str(variables[i]),
                    text
                )
        except IndexError:
            pass
        return text

    @ignoring
    def __applyDict(self, text, variables):
        for k, v in list(variables.items()):
            text = re.sub(
                re.compile('\{\{' + k + '\}\}'),
                str(v),
                text
            )
        return text
