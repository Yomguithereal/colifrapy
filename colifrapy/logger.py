# -------------------------------------------------------------------
# Logger Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependancies
#=============
import os
from datetime import datetime
import yaml
from tools.colors import color
from tools.decorators import singleton

# Main Class
#===========
@singleton
class Logger:

    # Properties
    #-----------
    strings = None
    output_path = None
    levels = {
        'INFO' : 
            {'color' : 'green', 'importance' : 4},
        'ERROR' : 
            {'color' : 'red', 'importance' : 3},
        'WARNING' : 
            {'color' : 'yellow', 'importance' : 2}, 
        'DEBUG' : 
            {'color' : 'blue', 'importance' : 1}
    }
    threshold = ['INFO', 'DEBUG', 'WARNING', 'ERROR']

    
    # Constructor
    #------------
    def __init__(self, strings=None, output_path=None, threshold=None):

        # Loading strings
        if strings is not None:
            self.load_strings(strings)

        # Setting output path
        if output_path is None:
            self.output_path = os.getcwd()+'/logs/'
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path)
            self.output_path += 'log.txt'

        # Setting level
        if threshold is not None:
            self.load_threshold(threshold)
        

    def config(self, **kwargs):
        self.__init__(**kwargs)

    # Setters
    #--------
    def load_strings(self, strings):
        with open(strings, 'r') as sf:
            self.strings = yaml.load(sf.read())

    def load_threshold(self, threshold):
        if not isinstance(threshold, list):
            threshold = [threshold]
        self.threshold = [i for i in threshold if i in self.levels]

    # Logging Method
    #---------------
    def write(self, message, level=None, variables={}):

        # Checking log level
        if level not in self.levels:
            level = 'DEBUG'

        # Retrieving message string
        if self.strings is None:
            ms = message
        else:
            try:
                string = reduce(dict.__getitem__, message.split(':'), self.strings)
            except KeyError:
                raise Exception('Colifrapy::Logger::WrongMessage')
            
            # Getting string back
            string = string.split('//')
            ms = string[0]
            if level == 'DEBUG':
                if len(string) > 1:
                    level = string[1]
        # Do we need to log?
        if level not in self.threshold:
            return False

        # Variable substitution
        for k in variables:
            ms = ms.replace('{'+str(k)+'}', str(variables[k]))

        # Printing to console
        print color('['+level+']', self.levels[level]['color'])+' :: '+str(ms)

        # Outputting to file if wanted
        self._toFile(ms, level)

    # Helper Methods
    def debug(self, message, variables={}):
        self.write(message, 'DEBUG', variables={})

    def info(self, message, variables={}):
        self.write(message, 'INFO', variables={})

    def warning(self, message, variables={}):
        self.write(message, 'WARNING', variables={})

    def error(self, message, variables={}):
        self.write(message, 'ERROR', variables={})
    
    # Header printing    
    def header(self, message):

        # To terminal
        print ''
        print color(message, 'yellow')
        print color(''.join(['-' for i in message]), 'yellow')

        # To file
        self._toFile(message, 'START')

    # Writing to log file
    def _toFile(self, message, level):
        separator = '\n\n' if level == 'START' else ''
        if self.output_path is not None:
            with open(self.output_path, "a+") as lf :
                lf.write(separator+datetime.now().strftime("%Y-%m-%d %H:%M")+' -- ['+level+'] :: '+str(message)+'\n')