Models
======
Models are the bulk of Colifrapy. You can extend them to access your settings and commands easily.


Usage
-----

.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):
            print self.settings.hello

    m = MyModel()
    m.test()
    >>> 'world'



Reserved Attributes
-------------------

    - **cache** (access to cache)
    - **log** (access to the logger described right after)
    - **opts** (access to the command line options)
    - **settings** (access to the program's settings)

Controller
----------
The Controller, as referred in other part of this documentation, is strictly speaking a model no different than any other. It is just a convention to use it as a central point for launching other models.
