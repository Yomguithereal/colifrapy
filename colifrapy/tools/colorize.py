# -------------------------------------------------------------------
# Colorizing Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Colors
# 1 for bright 2 for dim
# 3 for fore 4 for background
__colorCodes = {
    'black':   '0',
    'red':     '1',
    'green':   '2',
    'yellow':  '3',
    'blue':    '4',
    'magenta': '5',
    'cyan':    '6',
    'white':   '7'
}

# Color Printing
def colorize(string, color='black', background=None, bright=False):
    
    # Options
    background_option = '' if background is None else '4'+__colorCodes.get(background, '0')+';'
    bright_option = ';22' if bright is False else ';1'

    return "\033[%s3%s%sm%s\033[0m" % (
        background_option,
        __colorCodes.get(color, '0'),
        bright_option,
        str(string)
    )