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
    """ The Commander class extends ArgumentParser and has to
    compute the arguments passed to the tool. """

    # Properties
    #-----------
    opts = None
    verbose = False
    types = {'int': int, 'float': float, 'open': open}

    # Methods
    #--------

    # Configuration
    def config(self, version=None, description=None,
               arguments=None, usage=None, prog=None):

        self.version_str = version or '0.1.0'

        # Calling Parent
        ArgumentParser.__init__(
            self,
            description=description or '',
            usage=usage,
            prog=prog
        )

        # Adding Options
        if arguments is not None and len(arguments) > 0:
            self.__addArguments(arguments)

        # Default Arguments
        self.__defaultArguments()

        # Parsing
        self.opts = self.parse_args()

    # Batch adding arguments
    def __addArguments(self, arguments):
        for argument in arguments:

            # Dispatching
            args = argument[0]
            if len(argument) > 1:
                kwargs = argument[1]
            else:
                kwargs = {}

            # Checking verbose
            if len(args) > 1:
                if args[1] == '--verbose':
                    self.verbose = True

            # Associating type to pass yaml formatting
            if 'type' in kwargs:
                kwargs['type'] = self.__checkType(kwargs['type'])

            # Adding arguments
            self.add_argument(*args, **kwargs)

    # Default Arguments
    def __defaultArguments(self):

        # Version
        self.add_argument(
            *['-v', '--version'],
            **{'action': 'version', 'version': self.version_str}
        )

        # Verbose is not overriden, we add it
        if not self.verbose:
            self.add_argument(
                *['-V', '--verbose'],
                **{'action': 'store_true', 'help': 'verbose mode'}
            )

        # Settings override
        self.add_argument(
            '--settings',
            **{'type': str, 'help': 'settings file override'}
        )

    # Checking type
    def __checkType(self, typestr):
        return self.types.get(typestr, typestr)
