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
def is_string(string):
    if py2:
        return isinstance(string, basestring)
    else:
        return isinstance(string, str)

# Is of list kind
def is_of_list(l):
    return True in [isinstance(l, t) for t in [list, tuple, set]]