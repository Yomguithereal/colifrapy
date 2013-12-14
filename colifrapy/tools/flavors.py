# -------------------------------------------------------------------
# Logger Flavors
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
from .colorize import colorize


# Logger Text
#============
class TextFlavor(object):
    """ The TextFlavor class renders and style the logger's output. """

    # Operational variables
    flavor = 'default'
    formats = {}

    # Styles definitions
    styles = {
        'default': {
            'tpl': '[%s]',
            'separator': ' :: '
        },
        'flat': {
            'tpl': '%s',
            'separator': ' : ',
            'filters': [
                lambda x: x.lower()
            ]
        },
        'reverse': {
            'tpl': ' %s ',
            'separator': ' :: ',
            'styles': 'reverse'
        },
        'colorblind': {
            'tpl': '[%s]',
            'separator': ' :: ',
            'styles': 'reset'
        },
        'underline': {
            'tpl': '%s',
            'separator': ' -- ',
            'styles': 'underline'
        },
        'elegant': {
            'tpl': '%s',
            'separator': ' - ',
            'filters': [
                lambda x: x.title()
            ]
        },
    }

    # Colors
    level_colors = {
        'INFO':      'green',
        'ERROR':     'red',
        'WARNING':   'yellow',
        'DEBUG':     'blue',
        'VERBOSE':   'cyan',
        'COLIFRAPY': 'magenta',
        'CONFIRM':   'magenta',
        'INPUT':     'magenta'
    }

    def __init__(self, flavor):

        # Keeping trace of flavor
        if flavor in self.styles:
            self.flavor = flavor

        for level in self.level_colors:

            self.formats[level] = colorize(
                    self.styles[self.flavor]['tpl'] % self.__options(level),
                self.level_colors[level],
                style=self.styles[self.flavor].get('styles')) + \
                        self.styles[self.flavor]['separator']

    # Option application
    def __options(self, level):
        for func in self.styles[self.flavor].get('filters', []):
            level = func(level)
        return level

    # Style formatting
    def format(self, string, level):
        return self.formats[level] + string


# Logger Title
#=============
class TitleFlavor(object):
    """ The TitleFlavor class provides an abstraction use to output
    some elegant headers """

    flavor = 'default'
    styles = [
        'default',
        'heavy'
    ]

    def __init__(self, flavor):
        if flavor in self.styles:
            self.flavor = flavor

    def format(self, message, color):
        return getattr(self, '_' + self.flavor)(message, color)

    def _default(self, message, color):
        return colorize('\n' + message + '\n' + ('-' * len(message)), color)

    def _heavy(self, message, color):
        return colorize(
            '\n%s\n# %s #\n%s'
            % (
                ('#' * (len(message)+4)),
                message,
                ('#' * (len(message)+4))
            ),
            color
        )
