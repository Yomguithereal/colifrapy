# -------------------------------------------------------------------
# Colifrapy Extended Exceptions
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Main Class
#=============
class DataException(Exception):
    """ Just an standard python exception that one may
    load with data. """

    def __init__(self, message, data):
        Exception.__init__(self, message)
        self.data = data