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

try:
    from functools import reduce
except ImportError:
    pass

# Decorators
#===========
def lazyLoad(func):
    def _lazyLoad(self, *args, **kwargs):
        if not self._loaded:

            # Reading if relevant
            if self.exists():
                self.read()

            # Affecting object state
            self._loaded = True
        return func(self, *args, **kwargs)

    return _lazyLoad


# Main Class
#===========
class Cacher(object):
    """ The Cacher class is the main abstraction that rules
    all the following ones. It contains therefore every general
    methods and properties that every child one could use. """

    def __init__(self, filename=None, directory=None,
                 auto_write=False):

        # Generic properties
        self._loaded = False
        self.auto_write = auto_write is True
        self.filename = filename or 'cache.txt'

        if directory is not None:
            directory = directory.rstrip(os.sep)
        self.directory = directory or 'cache'

        # Setting filepath
        self.filepath = self.directory + os.sep + self.filename

    # Checking existence of cache file
    def exists(self):
        return os.path.exists(self.filepath)

    # Deleting cache
    def delete(self):
        if self.exists():
            os.remove(self.filepath)

    # Writing cache
    def checkDirectory(self):

        # Checking Directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    # Printing
    def __repr__(self):
        return '<%s.%s object at %s> #{%s}' % \
            (
                self.__module__,
                self.__class__.__name__,
                id(self),
                str(self.get())
            )


# Line Cacher
#============
class LineCacher(Cacher):
    """ The Line Cacher is a standard mono-line cache. It can be read,
    overwritten and serves simple purposes. """

    def __init__(self, *args, **kwargs):

        # Default filters
        self.filters = [
            lambda x: x,
            lambda x: x
        ]
        self._cache = None

        if kwargs.get('filename') is None:
            kwargs['filename'] = 'cache.txt'

        # Calling parent init
        super(LineCacher, self).__init__(*args, **kwargs)

    # Set reading filter
    def setReadingFilter(self, func):
        self.filters[0] = func

    # Set writing filter
    def setWritingFilter(self, func):
        self.filters[1] = func

    # Reading current cache
    def read(self):

        with open(self.filepath, 'r') as cf:
            self._cache = self.filters[0](cf.read().strip())

    # Writing cache
    def write(self):

        # Checking Directory
        self.checkDirectory()

        # To file
        with open(self.filepath, 'w') as cf:
            cf.write(self.filters[1](self._cache))

    # Getting cache
    @lazyLoad
    def get(self):
        return self._cache

    # Setting cache
    def set(self, value):
        self._cache = value

        # Auto-writing
        if self.auto_write:
            self.write()


# YAML Cacher
#============
class YAMLCacher(Cacher):
    """ The YAML Cacher is basically a small key-value file database
    that one may use to access organized data without having to
    deploy a server. """

    def __init__(self, *args, **kwargs):
        self.delimiter = ':'
        self._cache = {}

        if kwargs.get('filename') is None:
            kwargs['filename'] = 'cache.txt'

        # Calling parent init
        super(YAMLCacher, self).__init__(*args, **kwargs)

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
            cf.write(yaml.dump(self._cache,
                               default_flow_style=False, indent=4))

    # Getting cache
    @lazyLoad
    def get(self, key=None):

        if key is None:
            return self._cache
        else:
            try:
                path = key.split(self.delimiter)
                value = reduce(dict.__getitem__, path, self._cache)
            except KeyError:
                return None
            return value

    # Setting cache
    @lazyLoad
    def set(self, key, value):

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

    # Unsetting cache
    @lazyLoad
    def unset(self, key):

        # Setting according to path
        path = key.split(self.delimiter)
        json = self._cache

        # Iterating through path
        for step in path[0:-1]:
            if json.get(step) is not None:
                json = json[step]
            else:
                return False
        del json[path[-1]]

    # Overwrite cache
    def overwrite(self, data):
        self._cache = data
