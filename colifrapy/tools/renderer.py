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
try:
    unistring = unicode
except NameError:
    unistring = str

# Main Class
#===========
class Renderer:

    def render(self, text, variables):

        # Integers
        if isinstance(variables, int) | isinstance(variables, float):
            variables = str(variables)

        # If vars are dict
        if isinstance(variables, dict):
            return self.__apply_dict(text, variables)

        # If vars are tuple or array
        if isinstance(variables, tuple) | isinstance(variables, list):
            return self.__apply_list(text, variables)

        # If vars are strings
        if isinstance(variables, str) | isinstance(variables, unistring):
            return self.__apply_string(text, variables)

        return text

        
    def __apply_dict(self, text, variables):
        for key, value in list(variables.items()):
            text = re.sub('\{\{'+key+'\}\}', str(value), text)
        return text

    def __apply_list(self, text, variables):
        search = re.findall('\{\{([^}]+)\}\}', text)
        for i in range(0, len(variables)):
            try:
                text = re.sub('\{\{'+search[i]+'\}\}', str(variables[i]), text)
            except IndexError:
                pass
        return text

    def __apply_string(self, text, variable):
        return re.sub('\{\{[^}]+\}\}', variable, text)