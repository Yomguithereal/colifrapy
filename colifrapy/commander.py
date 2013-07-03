# -------------------------------------------------------------------
# Commander Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependancies
#=============
from argparse import ArgumentParser
from logger import Logger

# Main Class
#===========
class Commander(ArgumentParser):

    # Properties
    #-----------
    opts = None


    # Methods
    #--------

    # Constructor
    def __init__(self, version='0.1', arguments=None, strings=None):

        # Calling Parent
        ArgumentParser.__init__(self, version=version);

        # Adding Options
        if arguments is not None:
            self._add_arguments(arguments)

        # Registering Strings
        if strings is not None:
            Logger().load_strings(strings)

    # Configuration
    def config(self, **kwargs):
        self.__init__(**kwargs)
        
        # Parsing
        self.opts = self.parse_args()

    # Batch adding arguments
    def _add_arguments(self, arguments):
        for argument in arguments:
            self.add_argument(*[argument['short'], argument['long']], **{k : v for k, v in argument.iteritems() if k not in ['short', 'long']})