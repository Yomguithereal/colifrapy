.. _settings:

Settings
========

Class
-----

The Settings class' aim is to load a 'settings.yml' file containing every piece of configuration for a colifrapy program. This class is initialized by default by colifrapy's hub and is a singleton so its state won't change throughout your code.

Example of a settings.yml file (created by default in 'config/' by the Scaffolder)

.. code-block :: yaml

    # Basic Informations
    version: '[project-name] 0.1.0'
    description: 'Description of the program.'
    usage: 'How to deal with your program'
    arguments:
    - [ ['-t', '--test'], {'help' : 'Test', 'type' : 'int'} ]
    - [ ['positionnal'] ]

    # Logger Settings
    logger:
        strings: 'config/strings.yml'
        flavor: 'default'
        title_flavor: 'default'
        # Delete the path line not to write the log to a file
        directory: 'logs'
        threshold: ['DEBUG', 'ERROR', 'INFO', 'WARNING', 'VERBOSE']

    # Generic Settings needed by your program
    settings:
        hello: 'world'
        bonjour: 3.4
        hash: {'test' : 2}

Model Usage
-----------

In every class that extends colifrapy model, you can access your generic settings with the property settings. The following code assume the precedent yml file was loaded.

.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

            print self.settings.hello
            >>> "world"

            print self.settings.hash['test']
            >>> 2


Standalone Usage
----------------

As every colifrapy class, it is possible to use the Settings one as a standalone. The following example presents how you could do that and what you pass to it to make it work.

.. code-block:: python

    from colifrapy import Settings

    # Loading the YAML file
    s = Settings()
    s.load('path/to/settings.yml')

    # Accessing the generic settings
    d = s.getDict()
    print d.hello
    >>> "world"

    # Accessing cache
    c = s.getCache()

Once loaded, you can use it anywhere in your code and even reinstanciate it if convenient with it keeping the same state.

Options
-------

Standard
^^^^^^^^

Standard program options are the following:
    - **version** : Name and version of your program (outputted with -v/--version option)
    - **description** : Short description of your program and what it does
    - **usage** : How to use your program
    - **prog** : Program's name to display along usage string.
    - **epilog** : A final string to output when help is displayed.

Arguments
^^^^^^^^^

A good command line tool often comes with arguments, you can register those in the yaml file for convenience. Once loaded with arguments, the Settings class will load the Commander one with them.

Those are to be defined as for the python ArgParser_ class.

.. _ArgParser: http://docs.python.org/dev/library/argparse.html

Example of argument definition (under 'arguments' key).

.. code-block:: yaml

    arguments:
    - [ ['-t', '--test'], {'help' : 'Test', 'type' : 'int', 'default' : 5} ]
    - [ ['-b', '--blue'], {'help' : 'Blue option', 'type' : 'int', 'required' : 'True'} ]
    - [ ['some_positionnal_argument'] ]


Logger
^^^^^^

The Logger class can be given some options through settings. If none are supplied, logger will still be initialized with its default values.

For more precise information see :ref:`logger`.

For more precise information about the logger's styles see :ref:`styles`.

.. code-block:: yaml

    logger:

        # Must the logger be activated ?
        # Default: True
        activated: False

        # Strings supplied
        # Default: the logger won't use an externalized string file
        strings: 'config/'

        # Output Log Directory
        # Default: None (if None is supplied, the logger won't write to file)
        directory: 'logs'

        # Output filename
        # Default: 'log.txt'
        filename: 'project.log'

        # Output mode
        # Default: simple (available: simple, overwrite, rotation)
        mode: 'rotation'

        # Max Lines before log rotation
        # Default: 5000
        max_lines: 1000

        # Logger threshold
        # Default: ['DEBUG', 'ERROR', 'INFO', 'WARNING', 'VERBOSE']
        threshold: ['ERROR', 'INFO']

        # Exceptions
        # Default: True, decides whether the ERROR level of log should trigger Exceptions
        exceptions: False

        # Flavor
        # Default: 'default'
        flavor: 'elegant'

        # Title Flavor
        # Default: 'default'
        title_flavor: 'heavy'

.. _cacherSettings:

Cacher
^^^^^^

If needed, the Settings class can also handle the initialization of a cacher. Just provide a 'cache' key to the settings and populate it.

For more precise information see :ref:`cacher`.

.. code-block:: yaml

    cache:
        # Cache Directory
        # Default: cache
        directory: 'cache'

        # Cache filename
        # Default: 'cache.txt' for line mode and 'cache.yml' for yaml mode
        filename: 'project.log'

        # Kind of cache
        # Default: 'line' (choose between line and yaml)
        type: 'yaml'

        # Auto Write
        # Default: False
        auto_write: True

If you need more than one cache instance, just pass an array to the cache key in your YAML settings file. In this case, don't forget to pass a name to your settings to access it. Else it will have an ugly and standardized name like *__cacheInstance0*.

.. code-block:: yaml

    cache
        - name: 'infos'
          filename: 'cache1.yml'
          type: 'yaml'

        - name: 'last_update'
          filename: 'last_update.txt'
          type: 'line'

Then access your cache likewise.

.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

            print self.cache['infos']
            print self.cache['last_update']

General
^^^^^^^

If you need any generic settings more, just provide a settings key to your yaml file and populate it as in the following example.

.. code-block:: yaml

    settings:
        mysql:
            host: localhost
            user: root
            password: foo
        to_index: ["books", "notes"]
        limit: 5

If you need to divide your settings into several YAML files, colifrapy enables you to do so.

.. code-block:: yaml

    # Syntax is 'include::path/to/file.yml'
    # Warning, will only work on the first level (not on a nested one)
    settings:
        hello: 'world'
        hello2: 'include::path/to/another_config_file.yml'

N.B.
----

For every path given, colifrapy will try and decide whether it is absolute or relative (unix-style)::

    '/usr/local/settings.yml' is an absolute path
    'config/settings.yml' is a relative path