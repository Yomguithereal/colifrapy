# -------------------------------------------------------------------
# Command line tool Settings
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import os
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
    def load(self, yaml_file=None):

        # Default value
        if yaml_file is None:
            yaml_file = os.getcwd()+'/config/settings.yml'

        # Opening Settings Yaml File
        with open(yaml_file, 'r') as yf:
            data = yaml.load(yf.read())

        # Setting Commander
        commander_settings = {
            "version"     : data.get('version', '0.1'),
            "arguments"   : data.get('arguments', []),
            "description" : data.get('description', ''),
            "usage"       : data.get('usage')
        }
        self.__commander.config(**commander_settings)

        # Setting Logger
        logger_data = data.get('logger', {})
        logger_settings = {
            "strings"     : logger_data.get('strings'),
            "output_path" : logger_data.get('path'),
            "threshold"   : logger_data.get('threshold'),
            "triggers_exceptions" : logger_data.get('exceptions', True),
            "flavor" : logger_data.get('flavor', 'default'),
            "title_flavor" : logger_data.get('title_flavor', 'default')
        }
        self.__logger.config(**logger_settings)

        # General Settings
        if 'settings' in data:
            for key in data['settings']:
                setattr(self, key, data['settings'][key])

    # Helpers
    #--------------
    def __repr__(self):
        return pprint.pformat(self.__dict__)