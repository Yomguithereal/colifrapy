# -------------------------------------------------------------------
# Logger Flavors
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import pystache
from colorize import colorize

# Logger Text
#============
class TextFlavor:

    # Operational variables
    flavor = 'default'
    formats = None

    # Styles definitions
    styles = {
        'default' : {
            'tpl' : '[{{level}}]',
            'separator' : ' :: ',
            'options' : []
        },
        'flat' : {
            'tpl' : '{{level}}',
            'separator' : ' : ',
            'options' : [
                lambda x: x.lower()
            ]
        }
    }

    # Colors
    level_colors = {
        'INFO'    : 'green',
        'ERROR'   : 'red',
        'WARNING' : 'yellow',
        'DEBUG'   : 'blue',
        'VERBOSE' : 'cyan',
        'COLIFRAPY' : 'magenta',
        'CONFIRM' : 'magenta'
    }

    def __init__(self, flavor):

        # Keeping trace of flavor
        if flavor in self.styles:
            self.flavor = flavor

        # Caching string format
        self.formats = {level : colorize(pystache.render(self.styles[self.flavor]['tpl'], {'level' : self.__options(level)}), self.level_colors[level])+self.styles[self.flavor]['separator'] for level in self.level_colors}

    # Option application
    def __options(self, level):
        for func in self.styles[self.flavor]['options']:
            level = func(level)
        return level

    # Style formatting
    def format(self, string, level):
        return self.formats[level]+string


# Logger Title
#=============
class TitleFlavor:

    flavor = 'default'
    styles = [
        'default',
        'heavy'
    ]

    def __init__(self, flavor):
        if flavor in self.styles:
            self.flavor = flavor

    def format(self, message, color):
        return getattr(self, '_'+self.flavor)(message, color)


    def _default(self, message, color):
        return colorize('\n'+message+'\n'+('-'*len(message)), color)

    def _heavy(self, message, color):
        return colorize('\n'+( '#'*(len(message)+4) )+'\n# '+message+' #\n'+( '#'*(len(message)+4) ), color)