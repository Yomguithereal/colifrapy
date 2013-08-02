# -------------------------------------------------------------------
# Colorizing Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Colors
__colorCodes = {
    'black':    '0;30',     'bright gray':  '0;37',
    'blue':     '0;34',     'white':        '1;37',
    'green':    '0;32',     'bright blue':  '1;34',
    'cyan':     '0;36',     'bright green': '1;32',
    'red':      '0;31',     'bright cyan':  '1;36',
    'magenta':   '0;35',    'bright red':   '1;31',
    'yellow':   '0;33',     'bright magenta':'1;35',
    'dark gray':'1;30',     'bright yellow':'1;33',
    'normal':   '0'
}

# Color Printing
def colorize(string, color='blue'):
    return "\033["+__colorCodes.get(color, '0')+"m"+str(string)+"\033[0m"