# -------------------------------------------------------------------
# Colifrapy Cacher Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import os
import yaml
from .tools.decorators import singleton

try:
    from functools import reduce
except ImportError:
    pass


# Main Class
#=============
class Cacher:
    """ The Cacher class is the main abstraction that rules all the following ones.
    It contains therefore every general methods and properties that every child
    one could use. """

    # Generic properties
    _loaded = False

    auto_write = False
    directory = 'cache'
    filepath = None

    def __init__(self, filename=None, directory=None, auto_write=False):

        # Registering directory
        if directory is not None:
            self.directory = directory.rstrip('/')

        # Setting filename
        if filename is not None:
            self.filename = filename

        # Setting filepath
        self.filepath = self.directory+'/'+self.filename

        # Auto writing
        self.auto_write = auto_write is True

    # Loading the cache only when we use it
    def lazyLoad(self):
        if not self._loaded:

            # Reading if relevant
            if self.exists():
                self.read()

            # Affecting object state
            self._loaded = True

    # Checking existence of cache file
    def exists(self):
        return os.path.exists(self.filepath)

    # Writing cache
    def checkDirectory(self):

        # Checking Directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)


# Line Cacher
#=============
@singleton
class LineCacher(Cacher):
    """ The Line Cacher is a standard mono-line cache. It can be read,
    overwritten and serves simple purposes. """

    # Properties
    filename = 'cache.txt'
    _cache = None
    __filters = [
        lambda x: x,
        lambda x: x
    ]

    # Set reading filter
    def setReadingFilter(self, func):
        self.__filters[0] = func

    # Set writing filter
    def setWritingFilter(self, func):
        self.__filters[1] = func

    # Reading current cache
    def read(self):

        with open(self.filepath, 'r') as cf:
            self._cache = self.__filters[0](cf.read().strip())

    # Writing cache
    def write(self):

        # Checking Directory
        self.checkDirectory()

        # To file
        with open(self.filepath, 'w') as cf:
            cf.write(self.__filters[1](self._cache))

    # Getting cache
    def get(self):
        self.lazyLoad()
        return self._cache

    # Setting cache
    def set(self, value):
        self._cache = value

        # Auto-writing
        if self.auto_write:
            self.write()


# YAML Cacher
#=============
@singleton
class YAMLCacher(Cacher):
    """ The YAML Cacher is basically a small key-value file database
    that one may use to access organized data without having to
    deploy a server """

    # Properties
    filename = "cache.yml"
    delimiter = ":"
    _cache = {}

    # Reading current cache
    def read(self):

        with open(self.filepath, 'r') as cf:
            self._cache = yaml.load(cf.read())

    # Writing cache
    def write(self):

        # Checking Directory
        self.checkDirectory()

        # To File
        with open(self.filepath, 'w') as cf:
            cf.write(yaml.dump(self._cache, default_flow_style=False, indent=4))

    # Getting cache
    def get(self, key=None):
        self.lazyLoad()

        if key is None:
            return self._cache
        else:
            try:
                value = reduce(dict.__getitem__, key.split(self.delimiter), self._cache)
            except KeyError:
                return None
            return value

    # Setting cache
    def set(self, key, value):
        self.lazyLoad()

        # Setting according to path
        path = key.split(self.delimiter)
        json = self._cache

        # Iterating through path
        for step in path[0:-1]:
            json.update({step: {}})
            json = json[step]
        json[path[-1]] = value

        # Auto-writing
        if self.auto_write:
            self.write()