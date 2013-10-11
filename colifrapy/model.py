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
    """ The Models are the core of Colifrapy. They are to be extended to
    grant access to Colifrapy core utilities. """

    # Helper Propertie
    log = None
    settings = None
    opts = None
    cache = None

    # New Instance
    def __new__(cls, *args, **kwargs):

    	# Getting Singletons back
        commander = Commander()
        settings = Settings()

        # Setting reserved attributes
        cls.opts = commander.opts
        cls.settings = settings.accessSettingsDict()
        cls.log = Logger()
        cls.cache = settings.accessCache()

        # Returning class
        return object.__new__(cls)