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
            text = re.sub(r'\{\{%s\}\}' % key, '%(var)s', text) % \
              {'var': str(value)}
        if not self.ignore:
            text = re.sub(r'\{\{(.*?)\}\}', r'', text)
        return text

    def __applyList(self, text, variables):
        search = re.findall(r'\{\{(.*?)\}\}', text)
        for i in range(0, len(variables)):
            try:
                text = re.sub(
                    r'\{\{%s\}\}' % search[i],
                    r'%s',
                    text
                ) % str(variables[i])
            except Exception:
                pass
        return text

    def __applyString(self, text, variable):
        return re.sub(r'\{\{(.*?)\}\}', r'%(var)s', text) % \
          {'var': variable}
