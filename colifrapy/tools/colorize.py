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
from .utilities import *

# Colors
__colors = {
    'black':   '0',
    'red':     '1',
    'green':   '2',
    'yellow':  '3',
    'blue':    '4',
    'magenta': '5',
    'cyan':    '6',
    'white':   '7'
}

# Styles
__styles = {
    'reset' : '0',
    'bold' : '1',
    'dim' : '2',
    'underline' : '4',
    'blink' : '5',
    'reverse' : '7',
    'hidden' : '8'
}

# Color Printing
def colorize(string, color='black', background=None, style=None):

    # Background
    background_option = '' if background is None else '4'+__colors.get(background, '0')+';'

    # Style
    if is_of_list(style):
        style_option = "".join([";"+__styles.get(i, '0') for i in style])
    elif is_string(style):
        style_option = ";"+__styles.get(style, '0')
    else:
        style_option = ';22'

    return "\033[%s3%s%sm%s\033[0m" % (
        background_option,
        __colors.get(color, '0'),
        style_option,
        str(string)
    )