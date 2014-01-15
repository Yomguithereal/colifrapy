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
from .utilities import is_func


# Text Flavors
#=============
class LevelFlavor(object):
    """ The TextFlavor class renders and style the logger's output. """

    # Styles definitions
    flavors = {
        'default': lambda lvl: '[%s]' % lvl,
        'flat': lambda lvl: lvl.lower(),
        'reverse': lambda lvl: ' %s %s' % (lvl, '//reverse'),
        'underline': lambda lvl: lvl + '//underline',
        'elegant': lambda lvl: lvl.title()
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
        fmt = flavor if is_func(flavor) else self.flavors.get(flavor)

        if fmt is None:
            raise Exception('Colifrapy::Invalid text flavor (%s)' % flavor)

        (level_str, style) = (fmt(level), None)
        check = level_str.split('//')
        if len(check) > 1:
            (level_str, style) = (check[0], check[1])

        return colorize(
            level_str,
            fore_color=self.level_colors.get(level, 'magenta'),
            style=style
        ) if colors else level_str



# Title Flavor
#=============
class TitleFlavor(object):
    """ The TitleFlavor class provides an abstraction use to output
    some elegant headers. """

    def __call__(self, message, flavor='default'):

        # Passing a function
        if is_func(flavor):
            return flavor(message)

        try:
            func = getattr(self, '_' + flavor)
        except AttributeError as e:
            raise Exception('Colifrapy::Invalid title flavor (%s)' % flavor)

        return func(message)

    def _default(self, message):
        return '\n' + message + '\n' + ('-' * len(message))

    def _elegant(self, message):
        return '\n# ' + message + '\n#' + ('-' * (len(message) + 2))

    def _bold(self, message):
        return '\n# ' + message + '\n#' + ('=' * (len(message) + 2))

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
