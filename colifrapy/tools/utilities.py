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


# TODO: Optimize, can be written to be faster but less concise
# Is a number?
def is_number(variable):
    if isinstance(variable, bool):
        return False
    return True in [isinstance(variable, t) for t in [int, float]]


# Is of list kind
def is_of_list(variable):
    return True in [isinstance(variable, t) for t in [list, tuple]]


# Is a function
def is_func(variable):
    return hasattr(variable, '__call__')


# Parse a lambda string
# UNSAFE: use only from settings
def parse_lambda(string):
    func = eval(string)
    return func if is_func(func) else None


# Get Index with Fallback
def get_index(target, value, fallback=None):
    try:
        return target.index(value)
    except ValueError:
        return fallback


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
        path = os.path.dirname(sFile) + os.sep + path
    if isDir:
        return path.rstrip(os.sep) + os.sep
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

    return string[0].upper() + string[1:]
