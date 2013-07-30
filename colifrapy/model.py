# -------------------------------------------------------------------
# Command line tool Model
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
from logger import Logger
from commander import Commander
from settings import Settings

# Main Class
#=============
class Model(object):

    # Helper Propertie
    log = Logger()
    settings = Settings()
    opts = None

    # New Instance
    def __new__(cls, *args, **kwargs):
        commander = Commander()
        cls.opts = commander.opts
        return object.__new__(cls)