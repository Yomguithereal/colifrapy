# -------------------------------------------------------------------
# Colifrapy Utilities
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import sys

# Compatibility variables
py2 = sys.version_info[0] == 2
py3 = sys.version_info[0] == 3

# Python 2/3 is string
def is_string(variable):
    if py2:
        return isinstance(variable, basestring)
    else:
        return isinstance(variable, str)

# Is a number?
def is_number(variable):
    return True in [isinstance(variable, t) for t in [int, float]]

# Is of list kind
def is_of_list(variable):
    return True in [isinstance(variable, t) for t in [list, tuple, set]]

# Get Index with Fallback
def get_index(list, value, fallback):
    try:
        index = list.index(value)
    except ValueError:
        return fallback
    return index