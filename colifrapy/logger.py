# -------------------------------------------------------------------
# Logger Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============

# Back to the Future !
try:
    input = raw_input
except NameError:
    pass

try:
    from functools import reduce
except ImportError:
    pass

# Standard
import os
from datetime import datetime
import logging
import yaml
from .tools.decorators import singleton
from .tools.flavors import CustomFormatter, ColoredHeaderFormatter
from .tools.flavors import LevelFlavor, TitleFlavor
from .tools.renderer import Renderer

# Custom Logging Implementation
#==============================

# Adding verbose
VERBOSE_LVL = 1
logging.addLevelName(VERBOSE_LVL, 'VERBOSE')

def verbose(self, message, *args, **kwargs):
    self._log(VERBOSE_LVL, message, args, **kwargs)
logging.Logger.verbose = verbose


# Main Class
#===========
@singleton
class Logger(object):
    """ The Logger class represents the voice of Colifrapy and has to
    inform the user. It therefore outputs to console and to file in order
    to keep the code flow clear. """

    # Properties
    #-----------

    # Hierarchical instance
    _logger = logging.getLogger('colifrapy')
    _handlers = {
        'console': None,
        'file': None
    }

    # State
    exceptions = True

    # Rendering
    flavor = None
    title_flavor = TitleFlavor()
    renderer = Renderer()
    strings = None

    # Modes
    possible_modes = ['simple', 'overwrite', 'rotation']

    # Levels
    levels = {
        'VERBOSE': VERBOSE_LVL,
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'ERROR': 40,
        'CRITICAL': 50
    }

    # Formats
    formatters = {
        'console': None,
        'file': None
    }

    # Configuration
    #--------------

    def __init__(self):

        # Setting the logger base level to minimum in order to set it
        # at handler level
        self._logger.setLevel(VERBOSE_LVL)

    # Generic configuration
    def config(self, console_kwargs=None, file_kwargs=None,
               exceptions=True, strings=None, flavor='default'):

        # Generic options
        self.flavor = flavor
        self.exceptions = exceptions

        if strings is not None:
            self.loadStrings(strings)

        if console_kwargs is not None:
            self.configConsole(**console_kwargs)

        if file_kwargs is not None:
            self.configFile(**file_kwargs)

    # Console configuration
    def configConsole(self, activated=True,
                      threshold='VERBOSE',
                      formatter='%(flavored_levelname)s :: %(msg)s'):

        self.__resetHandler('console')

        self.formatters['console'] = CustomFormatter(
            formatter,
            self.flavor
        )

        # Activation
        if activated:

            # Loading Custom formatter
            handler = logging.StreamHandler()
            handler.setFormatter(self.formatters['console'])
        else:
            handler = logging.NullHandler()

        # Adding handler
        self._handlers['console'] = handler
        self._logger.addHandler(handler)

        # Threshold
        if self.levels.get(threshold) is None:
            threshold = 'VERBOSE'
        self._handlers['console'].setLevel(self.levels[threshold])

    # File output configuration
    def configFile(self, activated=False, threshold='VERBOSE',
                   directory='.', filename='program.log',
                   max_bytes=1048576, mode='simple', backup_count=5,
                   formatter='%(asctime)s %(levelname)s :: %(msg)s'):

        self.__resetHandler('file')

        # Formatter
        self.formatters['file'] = CustomFormatter(
            formatter,
            self.flavor,
            colors=False
        )

        # Directory setting
        if activated:
            directory = directory.rstrip('/')
            if not os.path.exists(directory):
                os.makedirs(directory)
            log_path = directory + os.sep + filename

            # Mode ?
            if mode not in self.possible_modes:
                raise Exception('Colifrapy::Wrong logger mode (%s)' % mode)

            # Registering correct handler
            if mode != 'rotation':
                write_mode = 'a' if mode == 'simple' else 'w'
                handler = logging.FileHandler(log_path, mode=write_mode)
            else:
                handler = logging.RotatingFileHandler(
                    log_path,
                    maxBytes=max_bytes,
                    backupCount=backup_count
                )
        else:
            handler = logging.NullHandler()

        # Adding handler
        handler.setFormatter(self.formatters['file'])
        self._handlers['file'] = handler
        self._logger.addHandler(handler)

        # Threshold
        if self.levels.get(threshold) is None:
            threshold = 'VERBOSE'
        self._handlers['file'].setLevel(self.levels[threshold])

    def __resetHandler(self, target):
        if self._handlers[target] is not None:
            self._logger.removeHandler(self._handlers[target])
            self._handlers[target] = None

    # Setters
    #--------
    def loadStrings(self, strings):
        with open(strings, 'r') as sf:
            self.strings = yaml.load(sf.read())

    # Logging Methods
    #----------------
    def write(self, path, variables=None, level=None):
        message = path

        # Checking log level
        if self.levels.get(level) is None:
            level = 'DEBUG'

        # Retrieving message string
        if self.strings is not None:
            string = self.__getString(message)

            # Getting string back
            string = string.split('//')
            message = string[0]
            if level == 'DEBUG':
                if len(string) > 1:
                    level = string[1]

        # Rendering
        if variables is not None:
            message = self.renderer.render(message, variables)

        # Carriage returns
        message = message.replace('\\n', '\n')

        # Sending to logging handlers
        self.__toHandlers(message, level)

        # Critical Error
        if level == 'CRITICAL' and self.exceptions:
            raise Exception('Logger:: %s' % path)

    # Helper Methods
    def verbose(self, message, v=None):
        self.write(message, level='VERBOSE', variables=v)

    def debug(self, message, v=None):
        self.write(message, level='DEBUG', variables=v)

    def info(self, message, v=None):
        self.write(message, level='INFO', variables=v)

    def warning(self, message, v=None):
        self.write(message, level='WARNING', variables=v)

    def error(self, message, v=None):
        self.write(message, level='ERROR', variables=v)

    def critical(self, message, v=None):
        self.write(message, level='CRITICAL', variables=v)

    # Header printing
    def header(self, message, flavor='default'):

        # Setting formatters
        self._handlers['console'].setFormatter(
            ColoredHeaderFormatter('%(colored_header)s')
        )
        self._handlers['file'].setFormatter(logging.Formatter('%(msg)s'))

        # Getting String
        message = self.__getString(message)

        # Printing
        self.__toHandlers(self.title_flavor(message, flavor))

        # Resetting formatters
        self._handlers['console'].setFormatter(self.formatters['console'])
        self._handlers['file'].setFormatter(self.formatters['file'])

    # Confirmation from user
    def confirm(self, message, default='y'):

        text = ('Y/n') if default == 'y' else ('y/N')

        output = self.__getString(message)
        response = input(output + ' ' + text + '\n').lower()
        response = default if response.strip() == '' else response

        return response == 'y'

    # Input from user
    def input(self, message, filter_func=lambda x: x):
        output = self.__getString(message)
        return filter_func(input(output + '\n'))

    # Utilities
    #----------

    # Get string from Yaml
    def __getString(self, path):
        if self.strings is None:
            return path
        try:
            return reduce(dict.__getitem__, path.split(':'), self.strings)
        except KeyError:
            return path

    # Outputting
    def __toHandlers(self, message, level='INFO'):
        getattr(self._logger, level.lower())(message)
