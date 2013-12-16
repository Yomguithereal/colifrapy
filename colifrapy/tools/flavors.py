# -------------------------------------------------------------------
# Logger Flavors
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import logging
from .colorize import colorize


# Text Flavors
#=============
class LevelFlavor(object):
    """ The TextFlavor class renders and style the logger's output. """

    # Styles definitions
    flavors = {
        'default': {
            'tpl': '[%s]'
        },
        'flat': {
            'tpl': '%s',
            'filters': lambda x: x.lower()
        },
        'reverse': {
            'tpl': ' %s ',
            'styles': 'reverse'
        },
        'colorblind': {
            'tpl': '[%s]',
            'styles': 'reset'
        },
        'underline': {
            'tpl': '%s',
            'styles': 'underline'
        },
        'elegant': {
            'tpl': '%s',
            'filters': lambda x: x.title()
        },
    }

    # Colors
    level_colors = {
        'INFO':      'green',
        'ERROR':     'red',
        'WARNING':   'yellow',
        'DEBUG':     'blue',
        'VERBOSE':   'cyan'
    }

    def __call__(self, level, flavor='default', colors=True):
        fmt = self.flavors.get(flavor)

        if fmt is None:
            raise Exception('Colifrapy::Invalid text flavor (%s)' % flavor)

        level_str = fmt['tpl'] % fmt.get('filters', lambda x: x)(level)

        return colorize(
            level_str,
            fore_color=self.level_colors.get(level, 'magenta'),
            style=fmt.get('styles')
        ) if colors else level_str



# Title Flavor
#=============
class TitleFlavor(object):
    """ The TitleFlavor class provides an abstraction use to output
    some elegant headers. """

    flavors = [
        'default',
        'heavy'
    ]

    def __call__(self, message, flavor='default'):
        if flavor not in self.flavors:
            raise Exception('Colifrapy::Invalid title flavor (%s)' % flavor)


        return getattr(self, '_' + flavor)(message)

    def _default(self, message):
        return '\n' + message + '\n' + ('-' * len(message))

    def _heavy(self, message):
        return '\n%s\n# %s #\n%s' \
            % (
                ('#' * (len(message)+4)),
                message,
                ('#' * (len(message)+4))
            )


# Custom Logging Formatters
#==========================
class CustomFormatter(logging.Formatter):

    level_flavor = LevelFlavor()

    # Init override
    def __init__(self, msg, flavor='default', colors=True):
        logging.Formatter.__init__(self, msg)
        self.flavor = flavor
        self.colors = colors is True

    # Format method override
    def format(self, record):

        # Adding our colored_levelname
        record.flavored_levelname = self.level_flavor(
            record.levelname,
            self.flavor,
            colors=self.colors
        )
        return logging.Formatter.format(self, record)

class ColoredHeaderFormatter(logging.Formatter):

    # Init override
    def __init__(self, msg):
        logging.Formatter.__init__(self, msg)

    def format(self, record):

        # Adding colored_header
        record.colored_header = colorize(record.msg, 'yellow')
        return logging.Formatter.format(self, record)
