# -------------------------------------------------------------------
# Logger Flavors
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
from .renderer import Renderer
from .colorize import colorize

# Logger Text
#============
class TextFlavor:
    """ The TextFlavor class renders and style the logger's output """

    # Operational variables
    flavor = 'default'
    formats = None
    renderer = Renderer()

    # Styles definitions
    styles = {
        'default' : {
            'tpl' : '[{{level}}]',
            'separator' : ' :: '
        },
        'flat' : {
            'tpl' : '{{level}}',
            'separator' : ' : ',
            'filters' : [
                lambda x: x.lower()
            ]
        },
        'reverse' : {
            'tpl' : ' {{level}} ',
            'separator' : ' :: ',
            'styles' : 'reverse'
        },
        'colorblind' : {
            'tpl' : '[{{level}}]',
            'separator' : ' :: ',
            'styles' : 'reset'
        },
        'underline' : {
            'tpl' : '{{level}}',
            'separator' : ' -- ',
            'styles' : 'underline'
        },
        'elegant' : {
            'tpl' : '{{level}}',
            'separator' : ' - ',
            'filters' : [
                lambda x: x.title()
            ]
        },
    }

    # Colors
    level_colors = {
        'INFO'    : 'green',
        'ERROR'   : 'red',
        'WARNING' : 'yellow',
        'DEBUG'   : 'blue',
        'VERBOSE' : 'cyan',
        'COLIFRAPY' : 'magenta',
        'CONFIRM' : 'magenta',
        'INPUT' : 'magenta'
    }

    def __init__(self, flavor):

        # Keeping trace of flavor
        if flavor in self.styles:
            self.flavor = flavor

        self.formats = {}
        for level in self.level_colors:
            self.formats[level] = colorize(self.renderer.render(self.styles[self.flavor]['tpl'], self.__options(level)), self.level_colors[level], style=self.styles[self.flavor].get('styles')) + self.styles[self.flavor]['separator']

    # Option application
    def __options(self, level):
        for func in self.styles[self.flavor].get('filters', []):
            level = func(level)
        return level

    # Style formatting
    def format(self, string, level):
        return self.formats[level]+string


# Logger Title
#=============
class TitleFlavor:
    """ The TitleFlavor class provides an abstraction use to output some elegant headers """

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
