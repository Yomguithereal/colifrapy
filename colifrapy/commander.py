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
from tools.decorators import singleton

# Main Class
#===========
@singleton
class Commander(ArgumentParser):

    # Properties
    #-----------
    opts = None


    # Methods
    #--------

    # Configuration
    def config(self, **kwargs):

        # Calling Parent
        ArgumentParser.__init__(self, version=kwargs['version'], description=kwargs['description']);

        # Adding Options
        if kwargs['arguments'] is not None:
            self._add_arguments(kwargs['arguments'])

        # Parsing
        self.opts = self.parse_args()

    # Batch adding arguments
    def _add_arguments(self, arguments):
        for argument in arguments:

            # Dispatching
            args = argument[0]
            kwargs = argument[1] if len(argument) > 1 else {}
            
            # Associating type to pass yaml formatting
            if 'type' in kwargs:
                kwargs['type'] = self._check_type(kwargs['type'])

            # Adding arguments
            self.add_argument(*args, **kwargs)

    # Checking type
    def _check_type(self, typestr):
        if typestr == 'int':
            return int
        elif typestr == 'float':
            return float
        elif typestr == 'open':
            return open
        else:
            raise Exception('Colifrapy::Commander::WrongType')