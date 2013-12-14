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
from .tools.flavors import TextFlavor
from .tools.flavors import TitleFlavor
from .tools.renderer import Renderer


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
    _stream = logging.getLogger('colifrapy:stream')
    _file = logging.getLogger('colifrapy:file')

    # State
    activated = True
    triggers_exceptions = True

    # Rendering
    renderer = Renderer()
    strings = None
    text_flavor = None
    title_flavor = None

    # Output
    output_directory = None
    output_filename = 'log.txt'
    possible_modes = set(['simple', 'overwrite', 'rotation'])
    output_mode = 'simple'
    max_lines = 5000

    # Levels
    levels = {
        'VERBOSE': 1,
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'ERROR': 40,
        'CRITICAL': 50
    }
    threshold = set(levels)
    necessary_levels = set(['CRITICAL', 'ERROR'])

    # Basic Logging Initialization
    #-----------------------------
    def __init__(self):

        # Base level
        # TODO: drop this debug line
        self._stream.setLevel(1)
        self._file.setLevel(1)

        # Adding custom VERBOSE level
        logging.addLevelName(self.levels['VERBOSE'], 'VERBOSE')

    # Configuration
    #--------------
    def config(self, strings=None, output_directory=None,
               threshold=None, triggers_exceptions=True,
               flavor='default', title_flavor='default', activated=True,
               output_mode='simple', output_filename=None, max_lines=None):

        activated = self.activated is True

        # Stream logger
        if self.activated:
            self._stream.addHandler(logging.StreamHandler())
        else:
            self._stream.addHandler(logging.NullHandler())

        # Flavor
        self.text_flavor = TextFlavor(flavor)
        self.title_flavor = TitleFlavor(title_flavor)

        # Loading strings
        if strings is not None:
            self.load_strings(strings)

        # Setting output path
        self.output_filename = output_filename or 'program.log'
        if output_directory is not None:

            # Enforcing directory existence
            # TODO: make a lazy decorator?
            self.output_directory = output_directory.rstrip('/')
            if not os.path.exists(self.output_directory):
                os.makedirs(self.output_directory)

            # Adding an handler
            log_path = self.output_directory + os.sep + self.output_filename
            if output_mode != 'rotation':
                mode = 'a' if output_mode == 'simple' else 'w'
                fh = logging.FileHandler(log_path, mode=mode)
            else:
                fh = logging.RotatingFileHandler(log_path, maxBytes=1048576)

            self._file.addHandler(fh)
        else:
            self._file.addHandler(logging.NullHandler())

        # Setting level
        if threshold is not None:
            self.load_threshold(threshold)

        # Exceptions ?
        self.triggers_exceptions = triggers_exceptions is True

        # Setting Output mode
        if output_mode in self.possible_modes:
            self.output_mode = output_mode

        # Max Lines
        if max_lines is not None:
            self.max_lines = int(max_lines)

    # Setters
    #--------
    def load_strings(self, strings):
        with open(strings, 'r') as sf:
            self.strings = yaml.load(sf.read())

    def load_threshold(self, threshold):
        self.threshold = (set(threshold) & self.threshold) | self.necessary_levels

    # Logging Method
    #---------------
    def write(self, path, variables={}, level=None):
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

        # Do we need to log?
        if level not in self.threshold:
            return False

        # Rendering
        message = self.renderer.render(message, variables)

        # Carriage returns
        message = message.replace('\\n', '\n')

        # Flavoring
        output = self.text_flavor.format(message, level)

        # Sending to logging handlers
        self.__toHandlers(output, level)

        # Critical Error
        if level == 'CRITICAL' and self.triggers_exceptions:
            raise Exception(path)

    # Helper Methods
    def debug(self, message, v={}):
        self.write(message, level='DEBUG', variables=v)

    def info(self, message, v={}):
        self.write(message, level='INFO', variables=v)

    def warning(self, message, v={}):
        self.write(message, level='WARNING', variables=v)

    def error(self, message, v={}):
        self.write(message, level='ERROR', variables=v)

    def verbose(self, message, v={}):
        self.write(message, level='VERBOSE', variables=v)

    # Header printing
    def header(self, message, color='yellow'):

        # Getting String
        message = self.__getString(message)

        # To terminal
        self.__toHandlers(self.title_flavor.format(message, color))

    # Confirmation from user
    def confirm(self, message, default='y'):
        text = ('Y/n') if default == 'y' else ('y/N')

        output = self.text_flavor.format(self.__getString(message), 'CONFIRM')
        response = input(output + ' ' + text + '\n').lower()
        response = default if response.strip() == '' else response

        return response == 'y'

    # Input from user
    def input(self, message, filter_func=lambda x: x):
        output = self.text_flavor.format(self.__getString(message), 'INPUT')
        return filter_func(input(output + '\n'))

    # Utilities
    #----------

    # Get string from Yaml
    def __getString(self, path):
        if self.strings is None:
            return path
        try:
            string = reduce(dict.__getitem__, path.split(':'), self.strings)
        except KeyError:
            return path
        return string

    # Outputting to console
    def __toHandlers(self, message, level):
        if self.activated:
            if level == 'VERBOSE':
                self._stream.log(self.levels['VERBOSE'], message)
                self._file.log(self.levels['VERBOSE'], message)
            else:
                getattr(self._stream, level.lower())(message)
                getattr(self._file, level.lower())(message)
