# -------------------------------------------------------------------
# Project Title Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

def titler(string):

    # String cases
    cases = [' ', '-', '_']

    # Fixing
    for case in cases:
        if string.count(case) > 0:
            string = "".join([i[0].upper()+i[1:] for i in string.split(case)])

    return string[0].upper()+string[1:]