Goodies
=======
Colifrapy also gives access to internal functions and helpers that may prove useful.


Colorization
------------
A function used to style console output. Note that not every style work on every consoles.

.. code-block:: python

    from colifrapy.tools.colorize import colorize

    # The colorize function accepts up to four arguments
    # 1. Positionnal : the string to style
    # 2. fore_color : color of the string
    # 3. background_color : color of background
    # 4. style : a list or string of style(s)

    # Available colors : black, red, green, yellow, blue, magenta, cyan, white
    # Available styles : reset, bold, italic, dim, underline, blink-slow, blink-fast, reverse, hidden

    # Example
    print colorize('hello', fore_color='red', background_color='black', style='bold')


Singleton Decorator
-------------------
Most of colifrapy classes are actually meant to be singletons. To perform this, the framework uses a simplistic decorator.

.. code-block:: python

    from colifrapy.tools.decorators import singleton

    @singleton
    class MySingleton():
        pass


Data Exceptions
---------------
Custom exceptions carrying data.

.. code-block:: python

    from colifrapy import DataException

    raise DataException(message, data)


Helper Functions
----------------
Some functions that may prove useful

.. code-block:: python
    
    # You would rather import only functions you need,
    # but for the sake of the example I use '*'
    from colifrapy.tools.utilities import *

    # Is the variable a number ?
    is_number('test')
    >>> False

    # Is the variable a string (python 2/3 compatible) ?
    is_string('test')
    >>> True

    # Is the variable a list or a tuple or a set ?
    is_of_list(['red', 'blue'])
    >>> True

    # Get Index with fallback
    get_index(['red', 'blue'], 'green', 5)
    >>> 5

    # Determine whether your path is relative or absolute
    # if it happens to be relative, the function will assume
    # it is relative to the file called (__main__)

    # For those examples, we assume that the file called by the command
    # line is /home/user/test/test.py
    determine_path('/home/user/path/to/file.txt')
    >>> '/home/user/path/to/file.txt'

    normalize_path('/resources/file.txt')
    >>> '/home/user/test/resources/file.txt'


Simplified Action Hub
---------------------
If your program is just simple as getting only one positionnal argument from the user in order to choose the action to perform, you might want to use colifrapy_action argument in you yaml setting file.

Example::

    python my-program.py action

Your settings yaml file

.. code-block:: yaml

    version: 'Basic action program'
    description: 'Let the user choose the action he wants.'
    arguments:
    - [ ['colifrapy_action'], {'choices' : ['test', 'hello', 'delete']}]

Once this argument setup, just write a simplistic colifrapy hub that will automatically trigger the relevant controller method named after a choice that the use can make.

**Command line hub**

.. code-block:: python

    from colifrapy import Colifrapy
    from model.controller import Controller

    # Hub
    class MyProject(Colifrapy):
        pass

    # Launching
    if __name__ == '__main__':
        hub = MyProject(Controller)

**Controller**

.. code-block:: python

    from colifrapy import Model

    class Controller(Model):

        def test(self):
            self.log.write('test')

        def hello(self):
            self.log.write('Hello World!')

        def delete(self):
            self.log.write('Deleting...')

**Usage**

.. code-block:: bash

    python my-program.py test
    >>> '[DEBUG] :: 'test'

    python my-program.py hello
    >>> '[DEBUG] :: 'Hello World!'

    python my-program.py delete
    >>> '[DEBUG] :: 'Deleting...'
