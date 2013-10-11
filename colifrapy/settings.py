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
from .tools.utilities import is_string
from .cacher import LineCacher, YAMLCacher

# Attr Dict
#===========
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

# Main Class
#=============
@singleton
class Settings():
    """ The Settings Class' goal is to read the 'settings.yml' file of the project
    in order to set up the tool with Colifrapy utilities such as the logger,
    the commander and the cacher. """

    # Standard Attributes
    __cache = None
    __dictSettings = AttrDict()

    # Sibling Instances
    __commander = Commander()
    __logger = Logger()


    # Configuration
    #--------------
    def load(self, yaml_path='config/settings.yml'):

        # Settings override
        if '--settings' in sys.argv:
            yaml_path = sys.argv[sys.argv.index('--settings')+1]

        # Opening Settings Yaml File
        with open(self.__getPath(yaml_path), 'r') as yf:
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
            possible_types = {'line' : LineCacher, 'yaml' : YAMLCacher}
            cache_type = cache_data.get('type', 'line')
            if cache_type not in possible_types:
                self.__logger.write('Wrong type of cache supplied.', level='COLIFRAPY')
                raise Exception('Colifrapy::Settings::WrongCacheType')
            else:

                # Directory
                cache_directory = cache_data.get('directory')
                if cache_directory is not None:
                    cache_directory = self.__getPath(cache_directory.rstrip('/'))

                # Initializing cache
                self.__cache = possible_types[cache_type](
                    filename=cache_data.get('filename'),
                    directory=cache_directory,
                    auto_write=cache_data.get('auto_write')
                )


        # General Settings
        #-----------------
        if 'settings' in data:
            general_settings = data.get('settings', {})

            # Computing includes
            for k, v in list(general_settings.items()):
                if is_string(v):
                    split = v.split('::')
                    if split[0] == 'include':
                        with open(self.__getPath(split[1]), 'r') as yf:
                            general_settings[k] = yaml.load(yf.read())

            # Final registration
            self.__dictSettings = AttrDict(general_settings)


    # Helpers
    #--------------
    def __repr__(self):
        return pprint.pformat(self.__dictSettings)

    def accessCache(self):
        return self.__cache

    def accessSettingsDict(self):
        return self.__dictSettings

    def __getPath(self, path):
        if os.path.isabs(path):
            return path
        else:
            try:
                sFile = os.path.abspath(sys.modules['__main__'].__file__)
            except:
                sFile = sys.executable
            return os.path.dirname(sFile)+'/'+path