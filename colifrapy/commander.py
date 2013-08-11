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
from .tools.decorators import singleton

# Main Class
#===========
@singleton
class Commander(ArgumentParser):

    # Properties
    #-----------
    opts = None
    __hasVerbose = False


    # Methods
    #--------

    # Configuration
    def config(self, version='0.1', description='Description Here', arguments=None, usage=None):

        # Calling Parent
        ArgumentParser.__init__(self, version=version, description=description, usage=usage);

        # Adding Options
        if arguments is not None and len(arguments) > 0:
            self._add_arguments(arguments)

        # Parsing
        self.opts = self.parse_args()

    # Batch adding arguments
    def _add_arguments(self, arguments):
        for argument in arguments:

            # Dispatching
            args = argument[0]
            kwargs = argument[1] if isinstance(argument[1], dict) else {}

            # Checking verbose
            if args[1] == '--verbose':
                self.__hasVerbose = True

            # Associating type to pass yaml formatting
            if 'type' in kwargs:
                kwargs['type'] = self._check_type(kwargs['type'])

            # Adding arguments
            self.add_argument(*args, **kwargs)

        # Verbose is not overriden, we add it
        if not self.__hasVerbose:
            self.add_argument(*['-V', '--verbose'], **{'action' : 'store_true'})

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