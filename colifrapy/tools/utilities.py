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
PY2 = sys.version_info[0] == 2


# Python 2/3 is string
def is_string(variable):
    if PY2:
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
def get_index(target, value, fallback):
    try:
        index = target.index(value)
    except ValueError:
        return fallback
    return index
