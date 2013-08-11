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


# Main Class
#=============
class Cacher:
    ''' The Cacher class is the main abstraction that rules all the following ones.
    It contains therefore every general methods and properties that every child
    one could use. '''

    # Generic properties
    __cache = None
    auto_write = False
    directory = 'config'
    loaded = False

    def __init__(self, directory=None, auto_write=False):

        # Registering directory
        if self.directory is not None:
            self.directory = directory.rstrip('/')

        # Auto writing
        self.auto_write = auto_write is True

    # Loading the cache only when we use it
    def lazyLoad(self):
        if not self.loaded:

            # Checking Directory
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)

            # Reading if relevant
            if self.exists:
                self.read()

            # Affecting object state
            self.loaded = True

    # Checking existence of cache file
    def exists(self):
        return os.path.exists(self.filepath)

    # Writing cache
    def write(self):
        with open(self.filepath, 'w') as cf:
            cf.write(self.__cache)


# Line Cacher
#=============
@singleton
class LineCacher(Cacher):
    ''' The Line Cacher is a standard mono-line cache. It can be read,
    overwritten and serves simple purposes. '''

    # Properties
    filename = 'cache.txt'
    filepath = None
    filter_func = lambda x: x

    # Completing parent's constructor
    def __init__(self, path, filename=None):
        Cacher.__init__(self, path)

        # Setting filename
        if filename is not None:
            self.filename = filename

        # Setting filepath
        self.filepath = self.directory+'/'+self.filename

    # Set reading filter
    def setReadingFilter(self, func):
        self.filter_func = func

    # Reading current cache
    def read(self):

        # Checking Existence
        if self.exists():
            with open(self.filepath, 'r') as cf:
                self.cache = self.filter_func(cf.read().strip())

    # Getting cache
    def get(self):
        self.lazyLoad()
        return self.__cache

    # Setting cache
    def set(self, value):
        self.lazyLoad()
        self.__cache = value

        # Auto-writing
        if self.auto_write:
            self.write()