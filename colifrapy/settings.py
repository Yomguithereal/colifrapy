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
import sys
import pprint
import yaml
from .logger import Logger
from .commander import Commander
from .tools.decorators import singleton
from .tools.utilities import is_string, is_of_list, normalize_path
from .tools.utilities import parse_lambda
from .cacher import LineCacher, YAMLCacher


# Attr Dict
#==========
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


# Main Class
#===========
@singleton
class Settings(object):
    """ The Settings Class' goal is to read the 'settings.yml' file of the
    project in order to set up the tool with Colifrapy utilities such as
    the logger, the commander and the cacher. """

    # Standard Attributes
    __cache = {}
    __dictSettings = AttrDict()
    __defaultCacheKey = '__cacheInstance'
    __possibleCacheTypes = {'line': LineCacher, 'yaml': YAMLCacher}

    # Sibling Instances
    __commander = Commander()
    __logger = Logger()

    # Configuration
    #--------------
    def load(self, yaml_path='config' + os.sep + 'settings.yml'):

        # Settings override
        if '--settings' in sys.argv:
            yaml_path = sys.argv[sys.argv.index('--settings')+1]

        # Opening Settings Yaml File
        with open(normalize_path(yaml_path), 'r') as yf:
            data = yaml.load(yf.read())

        # Setting Commander
        #------------------
        commander_settings = {}
        commander_opts = (
            'version',
            'arguments',
            'description',
            'usage',
            'prog',
            'epilog'
        )

        for i in commander_opts:
            commander_settings[i] = data.get(i)
        self.__commander.config(**commander_settings)

        # Setting Logger
        #---------------
        logger_data = data.get('logger', {})
        logger_specific_data = {
            'console': logger_data.get('console', {}),
            'file': logger_data.get('file', {})
        }

        logger_opts = {}
        possible_opts = {
            'generic': [
                'exceptions',
                'strings',
                'activated',
                'threshold',
                'formatter',
                'flavor'
            ],
            'console': [
                'activated',
                'threshold',
                'formatter'
            ],
            'file': [
                'activated',
                'threshold',
                'formatter',
                'directory',
                'filename',
                'max_bytes',
                'backup_count',
                'mode'
            ]
        }

        # Getting generic options
        for i in possible_opts['generic']:
            if i in logger_data:
                logger_opts[i] = logger_data[i]

        # Getting special options
        for kind in ('console', 'file'):
            logger_opts[kind + '_kwargs'] = {}

            for i in possible_opts[kind]:
                    if i not in logger_opts:
                        if i in logger_specific_data[kind]:
                            logger_opts[kind + '_kwargs'][i] = \
                              logger_specific_data[kind][i]
                    else:
                        logger_opts[kind + '_kwargs'][i] = \
                          logger_opts[i]

        # Regularization
        for i in ('activated', 'threshold', 'formatter'):
            if i in logger_opts:
                del logger_opts[i]

        # Parsing lambdas in flavor
        for i in ('generic', 'console_kwargs', 'file_kwargs'):
            target = logger_opts[i] if i != 'generic' else logger_opts
            if 'flavor' in target:
                if 'lambda' in target['flavor']:
                    target['flavor'] = parse_lambda(target['flavor'])

        # Actually loading logger settings
        self.__logger.config(**logger_opts)

        # Setting Cache
        #--------------
        cache_data = data.get('cache')
        if cache_data is not None:

            # Registering all instances
            if not is_of_list(cache_data):
                self.__registerCache(cache_data, True)
            else:
                for c in cache_data:
                    self.__registerCache(c)

        # General Settings
        #-----------------
        if 'settings' in data:
            general_settings = data.get('settings', {})

            # Computing includes
            for k, v in list(general_settings.items()):
                if is_string(v):
                    split = v.split('::')
                    if split[0] == 'include':
                        with open(normalize_path(split[1]), 'r') as yf:
                            general_settings[k] = yaml.load(yf.read())

            # Final registration
            self.__dictSettings = AttrDict(general_settings)

    # Helpers
    #--------
    def __repr__(self):
        return pprint.pformat(self.__dictSettings)

    def getCache(self):
        return self.__cache

    def getDict(self):
        return self.__dictSettings

    def __registerCache(self, cache_settings, alone=False):

        # Cache Instance Name
        cache_name = cache_settings.get(
            'name',
            '%s%s'
            % (
                self.__defaultCacheKey,
                len(self.__cache)
            )
        )

        # Checking Cache type
        cache_type = cache_settings.get('type', 'line')
        if cache_type not in self.__possibleCacheTypes:
            self.__logger.write('Wrong type of cache supplied.',
                                level='COLIFRAPY')
            raise Exception('Colifrapy::Settings::WrongCacheType')
        else:

            # Directory
            cache_directory = cache_settings.get('directory')
            if cache_directory is not None:
                cache_directory = normalize_path(cache_directory, True)

            # Initializing cache
            cache_instance = self.__possibleCacheTypes[cache_type](
                filename=cache_settings.get('filename'),
                directory=cache_directory,
                auto_write=cache_settings.get('auto_write')
            )

            if alone and cache_settings.get('name') is None:
                self.__cache = cache_instance
            else:
                self.__cache[cache_name] = cache_instance
