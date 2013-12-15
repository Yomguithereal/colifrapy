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
            'tpl': '[%s]',
            'sep': ' ::'
        },
        'flat': {
            'tpl': '%s',
            'sep': ' :',
            'filters': lambda x: x.lower()
        },
        'reverse': {
            'tpl': ' %s ',
            'sep': ' ::',
            'styles': 'reverse'
        },
        'colorblind': {
            'tpl': '[%s]',
            'sep': ' ::',
            'styles': 'reset'
        },
        'underline': {
            'tpl': '%s',
            'sep': ' --',
            'styles': 'underline'
        },
        'elegant': {
            'tpl': '%s',
            'sep': ' -',
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

    def __call__(self, level, flavor='default'):
        fmt = self.flavors.get(flavor)

        if fmt is None:
            raise Exception('Colifrapy::Invalid text flavor (%s)' % flavor)

        return colorize(
            fmt['tpl'] % fmt.get('filters', lambda x: x)(level),
            fore_color=self.level_colors.get(level, 'magenta'),
            style=fmt.get('styles')
        ) + fmt['sep']


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
    def __init__(self, msg, flavor='default', fake_lvl=None):
        logging.Formatter.__init__(self, msg)
        self.flavor = flavor
        self.fake_lvl = fake_lvl

    # Format method override
    def format(self, record):

        # Adding our colored_levelname
        record.colored_levelname = self.level_flavor(
            self.fake_lvl or record.levelname,
            self.flavor
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
