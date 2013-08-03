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

    # Styles definitions
    flavor = 'default'
    styles = {
        'default' : {
            'tpl' : '[{{level}}]',
            'separator' : ' :: ',
            'options' : []
        },
        'flat' : {
            'tpl' : '{{level}}',
            'separator' : ' : ',
            'options' : ['lowercase']
        }
    }

    # Colors
    level_colors = {
        'INFO'    : 'green',
        'ERROR'   : 'red',
        'WARNING' : 'yellow',
        'DEBUG'   : 'blue',
        'VERBOSE' : 'cyan',
        'COLIFRAPY' : 'magenta'
    }

    def __init__(self, flavor):
        if flavor in self.styles:
            self.flavor = flavor

    # Style formatting
    def format(self, string, level):
        color = self.level_colors[level]
        if 'lowercase' in self.styles[self.flavor]['options']:
            level = level.lower()
        return colorize(pystache.render(self.styles[self.flavor]['tpl'], {'level' : level}), color)+self.styles[self.flavor]['separator']+string


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