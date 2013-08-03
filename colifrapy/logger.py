# -------------------------------------------------------------------
# Logger Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import os
from datetime import datetime
import yaml
import pystache
from tools.colorize import colorize
from tools.decorators import singleton
from tools.flavors import TextFlavor
from tools.flavors import TitleFlavor

# Main Class
#===========
@singleton
class Logger:

    # Properties
    #-----------
    strings = None
    output_path = None
    text_flavor = None
    title_flavor = None
    triggers_exceptions = True
    levels = [
        'INFO',
        'ERROR',
        'WARNING',
        'DEBUG',
        'VERBOSE',
        'COLIFRAPY'
    ]
    threshold = set(['INFO', 'DEBUG', 'WARNING', 'ERROR', 'VERBOSE', 'COLIFRAPY'])
    necessary_levels = set(['ERROR', 'COLIFRAPY'])


    # Configuration
    #--------------
    def config(self, strings=None, output_path=None,
        threshold=None, triggers_exceptions=True,
        flavor='default', title_flavor='default'):

        # Loading strings
        if strings is not None:
            self.load_strings(strings)

        # Setting output path
        if output_path is not None:
            self.output_path = output_path.rstrip('/')
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path)
            self.output_path += '/log.txt'

        # Setting level
        if threshold is not None:
            self.load_threshold(threshold)

        # Exceptions ?
        self.triggers_exceptions = triggers_exceptions

        # Flavor
        self.text_flavor = TextFlavor(flavor)
        self.title_flavor = TitleFlavor(title_flavor)

    # Setters
    #--------
    def load_strings(self, strings):
        try:
            with open(strings, 'r') as sf:
                self.strings = yaml.load(sf.read())
        except Exception, e:
            self.write('The string file : {path} does not exist.', {'path' : strings}, 'COLIFRAPY')
            raise e

    def load_threshold(self, threshold):
        self.threshold = (set(threshold) & self.threshold) | self.necessary_levels


    # Logging Method
    #---------------
    def write(self, path, variables={}, level=None):
        message = path

        # Checking log level
        if level not in self.levels:
            level = 'DEBUG'

        # Retrieving message string
        if self.strings is not None:
            string = self._getString(message)

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
        output = self.text_flavor.format(pystache.render(message, variables), level)

        # Carriage returns
        output = output.replace('\\n', '\n')

        # If Colifrapy Message
        if level == 'COLIFRAPY':
            output = '\n'+output+'\n'

        # Printing to console
        print output

        # Outputting to file if wanted
        self._toFile(message, level)

        # Fatal Error
        if level == 'ERROR' and self.triggers_exceptions is True:
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
        message = self._getString(message)

        # To terminal
        print self.title_flavor.format(message, color)

        # To file
        self._toFile(message, 'START')


    # Confirmation asking method
    def confirm(self, message, default='y'):
        text = ('Y/n') if default == 'y' else ('y/N')

        output = self.text_flavor.format(self._getString(message), 'CONFIRM')
        response = raw_input(output+' '+text+'\n').lower()
        response = default if response.strip() == '' else response

        return response == 'y'


    # Utilities
    #----------

    # Get string from Yaml
    def _getString(self, path):
        if self.strings is None:
            return path
        try:
            string = reduce(dict.__getitem__, path.split(':'), self.strings)
        except KeyError:
            return path
        return string

    # Writing to log file
    def _toFile(self, message, level):

        # Not writing to file if we do not want to
        if self.output_path is None:
            return False

        # Writing to file
        separator = '\n\n' if level == 'START' else ''
        if self.output_path is not None:
            with open(self.output_path, "a+") as lf :
                lf.write(separator+datetime.now().strftime("%Y-%m-%d %H:%M")+' -- ['+level+'] :: '+str(message)+'\n')