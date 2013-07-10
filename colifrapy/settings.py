# -------------------------------------------------------------------
# Command line tool Settings
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependancies
#=============
import pprint
import yaml
from logger import Logger
from commander import Commander
from tools.decorators import singleton

# Main Class
#=============
@singleton
class Settings():

    __commander = Commander()
    __logger = Logger()

    # Configuration
    #--------------
    def load(self, yaml_file='settings.yml'):

        # Opening Settings Yaml File
        with open(yaml_file, 'r') as yf:
            data = yaml.load(yf.read())

        # Setting Commander
        self.__commander.config(version=data.get('version', '0.1'), arguments=data.get('arguments', []), description=data.get('description', ''), usage=data.get('usage'))

        # Setting Logger
        self.__logger.config(strings=data.get('strings'), output_path=data.get('log_path'), threshold=data.get('log_threshold'))

        # General Settings
        if 'settings' in data:
            for key in data['settings']:
                setattr(self, key, data['settings'][key])

    # Helpers
    #--------------
    def __repr__(self):
        return pprint.pformat(self.__dict__)
