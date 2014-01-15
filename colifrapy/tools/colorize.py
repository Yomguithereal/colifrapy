# -------------------------------------------------------------------
# Colorizing Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

""" The colorize module proposes a simple function to
style and give some color to console output. """

# Dependencies
import sys
from .utilities import is_string, is_of_list, get_index

# Possible Colors and Styles
COLORS = ['black', 'red', 'green', 'yellow',
          'blue', 'magenta', 'cyan', 'white']

STYLES = ['reset', 'bold', 'dim', 'italic', 'underline', 'blink-slow',
          'blink-rapid', 'reverse', 'hidden']

# Windows?
ANSI = True
if not hasattr(sys.stdout, "isatty") and not sys.stdout.isatty():
    ANSI = False


# Colorization function
def colorize(string, fore_color='black', background=None, style=None):

    if not ANSI:
        return string

    # Background
    if background is None:
        background_option = ''
    else:
        background_option = '4' + COLORS.get(background, '0') + ';'

    # Style
    if is_of_list(style):
        style_option = "".join(
            [";" + str(get_index(STYLES, i, 0)) for i in style])
    elif is_string(style):
        style_option = ";" + str(get_index(STYLES, style, 0))
    else:
        style_option = ';22'

    return "\033[%s3%s%sm%s\033[0m" % (
        background_option,
        str(get_index(COLORS, fore_color, 0)),
        style_option,
        str(string)
    )
