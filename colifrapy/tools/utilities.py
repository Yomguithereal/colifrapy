# -------------------------------------------------------------------
# Colifrapy Utilities
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import os
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


# Determine whether your path is relative or absolute
# if it happens to be relative, the function will assume
# it is relative to the file called (__main__)
# the trailing slash given does not count but will return the path with it
def normalize_path(path, isDir=False):
    if not os.path.isabs(path):
        try:
            sFile = os.path.abspath(sys.modules['__main__'].__file__)
        except:
            sFile = sys.executable
        path = os.path.dirname(sFile)+'/'+path
    if isDir:
        return path.rstrip('/')+'/'
    else:
        return path


# Small function to transform a basic string into an aesthetic title
def titler(string):

    # String cases
    cases = [' ', '-', '_']

    # Fixing
    for case in cases:
        if string.count(case) > 0:
            string = "".join([i[0].upper()+i[1:] for i in string.split(case)])

    return string[0].upper()+string[1:]
