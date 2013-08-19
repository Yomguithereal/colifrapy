# -------------------------------------------------------------------
# Command line tool Settings
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import os, sys
import pprint
import yaml
from argparse import ArgumentParser
from .logger import Logger
from .commander import Commander
from .tools.decorators import singleton
from .cacher import LineCacher

# Main Class
#=============
@singleton
class Settings():

    # Sibling Instances
    __commander = Commander()
    __logger = Logger()
    _cache = None

    # Configuration
    #--------------
    def load(self, yaml_file=None):

        # Settings override
        if '--settings' in sys.argv:
            yaml_file = sys.argv[sys.argv.index('--settings')+1]

        # Default value
        if yaml_file is None:
            yaml_file = 'config/settings.yml'

        # Opening Settings Yaml File
        with open(self.__getPath(yaml_file), 'r') as yf:
            data = yaml.load(yf.read())

        # Setting Commander
        #------------------
        commander_settings = {
            "version"     : data.get('version'),
            "arguments"   : data.get('arguments'),
            "description" : data.get('description'),
            "usage"       : data.get('usage')
        }
        self.__commander.config(**commander_settings)

        # Setting Logger
        #---------------
        logger_data = data.get('logger', {})

        # Threshold
        logger_threshold = None if self.__commander.opts.verbose else logger_data.get('threshold')

        # Strings
        logger_strings = logger_data.get('strings')
        if logger_strings is not None:
            logger_strings = self.__getPath(logger_strings)

        # Output path
        logger_path = logger_data.get('directory')
        if logger_path is not None:
            logger_path = self.__getPath(logger_path.rstrip('/'))

        logger_settings = {
            "activated"   : logger_data.get('activated', True),
            "strings"     : logger_strings,
            "output_directory" : logger_path,
            "output_mode" : logger_data.get('mode'),
            "output_filename": logger_data.get('filename'),
            "max_lines": logger_data.get('max_lines'),
            "threshold"   : logger_threshold,
            "triggers_exceptions" : logger_data.get('exceptions', True),
            "flavor" : logger_data.get('flavor', 'default'),
            "title_flavor" : logger_data.get('title_flavor', 'default')
        }
        self.__logger.config(**logger_settings)

        # Setting Cache
        #--------------
        cache_data = data.get('cache')
        if cache_data is not None:

            # Checking if type of cache is valid
            possible_types = {'line' : LineCacher}
            cache_type = cache_data.get('type', 'line')
            if cache_type not in possible_types:
                self.__logger.write('Wrong type of cache supplied. ("line")', 'COLIFRAPY')
                raise Exception('Colifrapy::Settings::WrongCacheTypeSupplied')
            else:

                # Initializing cache
                self._cache = possible_types[cache_type](cache_data.get('directory'), cache_data.get('filename'), cache_data.get('auto_write'))


        # General Settings
        #-----------------
        if 'settings' in data:
            for key in data['settings']:
                setattr(self, key, data['settings'][key])

    # Helpers
    #--------------
    def __repr__(self):
        return pprint.pformat(self.__dict__)

    def __getPath(self, path):
        if os.path.isabs(path):
            return path
        else:
            try:
                sFile = os.path.abspath(sys.modules['__main__'].__file__)
            except:
                sFile = sys.executable
            return os.path.dirname(sFile)+'/'+path