.. _logger:

Logger
======

Class
-----
The Logger class is the voice of colifrapy. Its aim is to display feedback from your program into the console and to write it if necessary to a file for archive purposes. It may also feed on externalized strings written in a YAML file.


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
    logger_instance.config(options)

    logger_instance.write('Hello World!')
    >>> '[DEBUG] :: Hello World!'


Options
-------

.. |br| raw:: html

   <br />

The options you may pass to the constructor of the logger (those options are automatically taken care of when the logger is loaded by the Settings class) are the following:

    - **strings**
        (string) |br|
        path to your externalized YAML string |br|
        *default*: None (the logger won't use externalized strings)

    - **output_directory**
        (string) |br|
        path to your output logging directory |br|
        *default*: None (the logger won't output to file)

    - **output_filename**
        (string) |br|
        name of the log file |br|
        *default*: "log.txt"

    - **output_mode**
        (string) |br|
        choices: simple/overwrite/rotation |br|
        mode of file logging, for more information see :ref:`modes` |br|
        *default*: "simple"

    - **threshold**
        (list) |br|
        a list containing values from ["INFO", "DEBUG", "ERROR", "WARNING", "VERBOSE"] |br|
        list of level you want the logger to express. Note that if you drop ERROR it will still be automatically added for obvious reasons. |br|
        *default*: all of the above list

    - **triggers_exceptions**
        (boolean) |br|
        whether the ERROR level should trigger exceptions. |br|
        *default*: True

    - **flavor**
        (string) |br|
        the style of log to adopt, for a list of those see :ref:`styles`. |br|
        *default*: "default"

    - **title_flavor**
        (string) |br|
        the title style to adopt, for a list of those see :ref:`styles`. |br|
        *default*: "default"

    - **activated**
        (boolean) |br|
        whether the logger should function or not. (Useful to disable it if needed). |br|
        *default*: True

    - **max_lines**
        (integer) |br|
        when in rotation mode, number of lines before changing the log file. |br|
        *default*: 5000

Note that if you want to change one of those options on the fly you can always run the config method one more time with the changed options.

Levels
------
The logger accepts five levels :

    - INFO (green output)
    - VERBOSE (cyan output)
    - DEBUG (blue output)
    - WARNING (yellow ouput)
    - ERROR (red output) --> will throw an exception for you to catch or not

By default, if no level is specified for a message, DEBUG will always be taken.


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
            self.log.header('main:title', [optional]flavor='default|heavy')
            >>> Colifrapy
            >>> ---------

            # Write methods shorteners
            self.log.error(message, vars)
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
            >>> '[CONFIRM] :: Are you sure you want to continue? (Y/n)'
            >>> y --> True

            response = self.log.confirm('Are you sure you want to continue?', 'n')
            >>> '[CONFIRM] :: Are you sure you want to continue? (y/N)'
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
            >>> '[INPUT] :: What up ?'
            >>> 'feeling fine' --> 'feeling fine'

            # You can also provide a lambda to the function as second argument
            # This lambda will affect the input given
            response = self.log.input('What up ?', lambda x: x.upper())
            >>> '[INPUT] :: What up ?'
            >>> 'feeling fine' --> 'FEELING FINE'


.. _styles:

Styles
------

The colifrapy logger comes with several visual alternatives that you may choose from. Those are called flavors and are available for title and standard messages.

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

Flavors
^^^^^^^

**default**

.. code-block:: bash

    [DEBUG] :: text

**flat**

.. code-block:: bash

    debug : text

**colorblind**

.. code-block:: bash

    # Without colors
    [DEBUG] :: text

**reverse**

.. code-block:: bash

    # With reverse colors
    DEBUG  :: text

**elegant**

.. code-block:: bash

    Debug - text

**underline**

.. code-block:: bash

    DEBUG -- text
    -----
