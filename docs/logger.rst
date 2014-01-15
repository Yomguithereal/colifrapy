.. _logger:

Logger
======

Class
-----
The Logger class is the voice of colifrapy. Its aim is to display feedback from your program into the console and to write it to a file if necessary. It may also feed on externalized strings written in a YAML file.

N.B.: this custom logger is built around the python logging_ module and spawn a logging instance named "colifrapy".

.. _logging: http://docs.python.org/2/library/logging.html


Model Usage
-----------
By default, and even if no settings were initialized before, every colifrapy model is loaded with the Logger so you may use it when convenient.

.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):

        # In every colifrapy model, the Logger is
        # accessible through the "log" property.

        def test(self):
            self.log.write('Hello World!')
            >>> '[DEBUG] :: Hello World!'


Standalone Usage
----------------
If you want to use the colifrapy Logger without messing with the whole framework, it is obviously possible. Note that as a lot of colifrapy classes, the Logger is actually a singleton. You may then instanciate it in different files, it will always be the same one for convenience.

.. code-block:: python

    from colifrapy import Logger

    logger_instance = Logger()

    # Run the configuration method at least one to initialize the logger
    logger_instance.config(**options)

    logger_instance.write('Hello World!')
    >>> '[DEBUG] :: Hello World!'

    # To change the logger's configuration, just rerun the config method
    logger_instance.config(**options)

    # Or for specific options
    logger_instance.configConsole(options)
    logger_instance.configFile(options)

Levels
------
The logger accepts five levels (ordered by importance):

    - VERBOSE (cyan output)
    - DEBUG (blue output)
    - INFO (green output)
    - WARNING (yellow ouput)
    - ERROR (red output)
    - CRITICAL (violet output)  --> will throw an exception for you to catch or not

By default, if no level is specified for a message, DEBUG will always be taken.

Options
-------

.. |br| raw:: html

   <br />

Colifrapy's logger has three different configuration methods, each one dealing with a particular end. You can therefore configure the logger as a whole or rather one of both its handlers (console and file).

Note that if you want to change one of those options on the fly you can always run the config method one more time with the changed options.

Generic Options
^^^^^^^^^^^^^^^

The generic options you may pass to the logger's *config* method (those options are automatically taken care of when the logger is loaded by the Settings class) are the following:

    - **strings**
      {string} |br|
      Path leading to your externalized YAML strings. |br|
      *default*: None (the logger won't use externalized strings)

    - **exceptions**
      {boolean} |br|
      Should the CRITICAL level trigger exceptions. |br|
      *default*: True

    - **flavor**
      {string|lambda} |br|
      The flavor to use to format %(flavored_levelname)s. |br|
      *default*: 'default'

    - **console_kwargs**
      {dict} |br|
      A configuration dict to be run into the configConsole method. |br|
      *default*: None (the configConsole method will be called with its defaults)

    - **file_kwargs**
      {dict} |br|
      A configuration dict to be run into the configFile method. |br|
      *default*: None (the configFile method will be called with its defaults)

For a list of flavors, see :ref:`styles`. If none of the proposed flavors suit you and you need to create your own, please note that you can pass a lambda taking the levelname variable to the flavor option 

**Usage example**

.. code-block:: python

    from colifrapy import Logger

    logger_instance = Logger()
    logger_instance.config(strings='example_string.yml', exceptions=False)

Console Options
^^^^^^^^^^^^^^^

The console options you may pass to the logger's *configConsole* method (those options are automatically taken care of when the logger is loaded by the Settings class under logger:console) are the following:

    - **activated**
      {boolean} |br|
      Whether the console handler should be activated or not. |br|
      *default*: True

    - **threshold**
      {string} |br|
      Threshold for the console handler. |br|
      *default*: 'VERBOSE'

    - **formatter**
      {string} |br|
      Formatter for the console handler. |br|
      *default*: '%(flavored_levelname)s :\: %(msg)s'

**Usage example**

.. code-block:: python

    from colifrapy import Logger

    logger_instance = Logger()
    logger_instance.configConsole(threshold='WARNING', activated=True)

File Options
^^^^^^^^^^^^

The console options you may pass to the logger's *configFile* method (those options are automatically taken care of when the logger is loaded by the Settings class under logger:file) are the following:

    - **activated**
      {boolean} |br|
      Whether the file handler should be activated or not. |br|
      *default*: False

    - **threshold**
      {string} |br|
      Threshold for the file handler. |br|
      *default*: 'VERBOSE'

    - **formatter**
      {string} |br|
      Formatter for the console handler |br|
      *default*: '%(asctime)s %(levelname)s :: %(msg)s'.

    - **directory**
      {string} |br|
      Directory where the file handler is supposed to write its logs. |br|
      *default*: '.'

    - **filename**
      {string} |br|
      Name of the log files. |br|
      *default*: 'program.log'

    - **mode**
      {string} |br|
      File logging mode. See :ref:`modes`. |br|
      *default*: 'simple'

    - **max_bytes**
      {integer} |br|
      When in rotation mode, maximum of bytes for a log file before rotating. |br|
      *default*: 1048576

    - **backup_count**
      {integer} |br|
      When in rotation mode, maximum number of archived log files. |br|
      *default*: 5

Note that the file handler is not activated by default.

**Usage example**

.. code-block:: python

    from colifrapy import Logger

    logger_instance = Logger()
    logger_instance.configFile(threshold='ERROR', activated=True, mode='overwrite')


Strings
-------
Colifrapy offers to externalize your strings in order to enable you to quickly modify them if needed, or even translate them easily. I you do not provide the logger with some strings, it will simply take normal python strings.

The string format used is a mustache-like one, so variables come likewise : {{some_variable}}

Strings given must follow this yaml layout

.. code-block:: yaml

    main:
        process:

            # String with a variable contained within the mustaches
            start: 'Starting corpus analysis (path : {{path}})//INFO'

            # Simply write two slashes at the end to specify the level of the message
            end: 'Exiting//WARNING'
            test_line_break: '\nBonjour'

        title: 'Colifrapy'

    other_string_category:
        test: 'Hello everyone//INFO'
        you:
            can:
                make: 'any levels that you want'
                so: 'you can organize your strings however you need.'

.. _modes:

Modes
-----
The Logger comes with three different outputting modes:

    - **simple**: it will write everything to a single specified file.
    - **overwrite**: the log will be completely overwritten each time you launch the program.
    - **rotation**: each time your log file overcomes a specified number of lines, it will create a new file and archive the old one. E.g. it functions like the apache log.

For more information about file rotation, you can read the python logging module's RotatingFileHandler documentation_.

.. _documentation: http://docs.python.org/2/library/logging.handlers.html#rotatingfilehandler

Methods
-------

Writing
^^^^^^^
.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

            # Main method
            #------------

            # Outputting a message
            self.log.write('main:process:end')
            >>> '[WARNING] :: Exiting'

            # Overriding the message level
            self.log.write('main:process:end', level='INFO')
            >>> '[INFO] :: Exiting'

            # Passing variables
            self.log.write('main:protocol:start', {'path' : 'test'})
            >>> '[INFO] :: Starting corpus analysis (path : test)'

            # Variables can be passed to the logger as:
            # a hash, a list, a tuple, a single string or integer or float

            # Examples
            self.log.write('{{variable}}', 'test')
            >>> '[DEBUG] :: test'

            self.log.write('{{var1}} is {{var2}}', ['python', 'cool'])
            >>> '[DEBUG] :: python is cool'

            # When yml string file is not specified or if message does not exist in the yaml file
            self.log.write('Test string')
            >>> '[DEBUG] :: Test string'

            # Named arguments of write
            # variables --> mixed
            # level --> log level



            # Helper methods
            #---------------

            # Printing a header
            self.log.header('main:title', [optional]flavor='default')
            >>> Colifrapy
            >>> ---------

            # You can also pass a function as the title flavor rather
            # than a predetermined one.
            self.log.header('main:title', flavor=lambda msg: msg.upper())
            >>> COLIFRAPY

            # Write methods shorteners
            self.log.critical(message, vars)
            self.log.error(...)
            self.log.warning(...)
            self.log.info(...)
            self.log.debug(...)
            self.log.verbose(...)


Confirmation
^^^^^^^^^^^^
.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

            # Confirmation
            #---------------

            # 'y' will be taken by default in arg 2
            # will return True for y and False for n
            response = self.log.confirm('Are you sure you want to continue?')
            >>> 'Are you sure you want to continue? (Y/n)'
            >>> y --> True

            response = self.log.confirm('Are you sure you want to continue?', 'n')
            >>> 'Are you sure you want to continue? (y/N)'
            >>> n --> False


User Input
^^^^^^^^^^
.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

            # User Input
            #---------------

            response = self.log.input('What up ?')
            >>> 'What up ?'
            >>> 'feeling fine
            >>> 'feeling fine'

            # You can also provide a lambda to the function as second argument
            # This lambda will affect the input given
            response = self.log.input('What up ?', lambda x: x.upper())
            >>> 'What up ?'
            >>> 'feeling fine'
            >>> 'FEELING FINE'


.. _styles:

Styles
------

Colifrapy's logger comes with several visual alternatives that you may choose from. Those are called flavors and are available for title and standard messages.


Formatters
^^^^^^^^^^

Colifrapy's logger accepts a format string the same way as the python logging module, so you can customize your logging output. It also add a custom variable named *flavored_levelname* which is in fact the level name colored and stylized.

.. code-block:: python

    # Default formatter for console
    '%(flavored_levelname)s :: %(msg)s'
    >>> [DEBUG] :: message to log

    # Default formatter for file
    '%(asctime)s %(levelname)s :: %(msg)s'
    >>> 2014-01-15 13:56:09,798 DEBUG :: message to log

For the full documentation about the variables usable by the formatter, see this page_.

.. _page: http://docs.python.org/2/library/logging.html#logrecord-attributes

Title Flavors
^^^^^^^^^^^^^

**default**

.. code-block:: bash

    Title
    -----

**heavy**

.. code-block:: bash

    #########
    # Title #
    #########

**elegant**

.. code-block:: bash

    # Title
    #-------

**bold**

.. code-block:: bash

    # Title
    #=======

Flavors
^^^^^^^

**default**

.. code-block:: bash

    [DEBUG]

**flat**

.. code-block:: bash

    debug

**reverse**

.. code-block:: bash

    # With reverse colors
    DEBUG

**elegant**

.. code-block:: bash

    Debug

**underline**

.. code-block:: bash

    DEBUG
    -----
