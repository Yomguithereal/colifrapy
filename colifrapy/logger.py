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
from colifrapy.tools.colors import color
from colifrapy.tools.decorators import singleton

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
    threshold = 'DEBUG'

    
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
            if threshold in self.levels:
                self.threshold = threshold
            else:
                raise Exception('Logger::WrongThreshold')

    # Setters
    #--------
    def load_strings(self, strings):
        with open(strings, 'r') as sf:
            self.strings = yaml.load(sf.read())


    # Logging Method
    #---------------
    def write(self, message, level='DEBUG', variables={}):

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
                raise Exception('Logger::WrongMessage')
            
            # Getting string back
            string = string.split('//')
            ms = string[0]
            if len(string) > 1:
                level = string[1]

        # Variable substitution
        for k in variables:
            ms = ms.replace('{'+str(k)+'}', str(variables[k]))

        # Printing to console
        print color('['+level+']', self.levels[level]['color'])+' :: '+str(ms)

        # Outputting to file if wanted
        self._toFile(ms, level)
        

    def header(self, message):

        # To terminal
        print ''
        print color(message, 'yellow')
        print color(''.join(['-' for i in message]), 'yellow')

        # To file
        self._toFile(message, 'START')

    def _toFile(self, message, level):
        separator = '\n\n' if level == 'START' else ''
        if self.output_path is not None:
            with open(self.output_path, "a+") as lf :
                lf.write(separator+datetime.now().strftime("%Y-%m-%d %H:%M")+' -- ['+level+'] :: '+str(message)+'\n')