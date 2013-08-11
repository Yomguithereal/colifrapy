# -------------------------------------------------------------------
# Command line tool Model
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
from .logger import Logger
from .commander import Commander
from .settings import Settings

# Main Class
#=============
class Model(object):

    # Helper Propertie
    log = None
    settings = None
    opts = None
    cache = None

    # New Instance
    def __new__(cls, *args, **kwargs):

    	# Loading every necessary piece
        commander = Commander()
        settings = Settings()
        cls.opts = commander.opts
        cls.settings = settings
        cls.log = Logger()
        cls.cache = settings._cache
        return object.__new__(cls)