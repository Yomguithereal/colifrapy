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
    
    def __init__(self, message, data):
        Exception.__init__(self, message)
        self.data = data