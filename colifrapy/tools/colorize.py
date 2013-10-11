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

# Possible Colors and Styles
__colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
__styles = ['reset', 'bold', 'dim', 'italic', 'underline', 'blink-slow', 'blink-rapid', 'reverse', 'hidden']

# Colorization function
def colorize(string, color='black', background=None, style=None):

    # Background
    background_option = '' if background is None else '4'+__colors.get(background, '0')+';'

    # Style
    if is_of_list(style):
        style_option = "".join([";"+str(get_index(__styles, i, 0)) for i in style])
    elif is_string(style):
        style_option = ";"+str(get_index(__styles, style, 0))
    else:
        style_option = ';22'

    return "\033[%s3%s%sm%s\033[0m" % (
        background_option,
        str(get_index(__colors, color, 0)),
        style_option,
        str(string)
    )