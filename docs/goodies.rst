Goodies
=======
Colifrapy also gives access to internal functions and helpers that may prove useful.


Colorization
------------
A function used to style console output.

.. code-block:: python

    from colifrapy.tools.colorize import colorize

    # The colorize function accepts up to four arguments
    # 1. Positionnal : the string to style
    # 2. fore_color : color of the string
    # 3. background_color : color of background
    # 4. style : a list or string of style(s)

    # Available colors : black, red, green, yellow, blue, magenta, cyan, white
    # Available styles : reset, bold, dim, underline, blink, reverse, hidden

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
