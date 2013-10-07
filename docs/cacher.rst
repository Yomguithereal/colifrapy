.. _cacher:

Cacher
======
The Cacher classes' aim is to save some data to files for long-term usage. One could see them as very simplistic databases.



Model Usage
-----------
As for the logger, if a cacher was initialized by the settings while running colifrapy, "cache" will be a reserved attribute of any of your models.

.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

            # We assume that a line cache file containing
            # the string "Hello" was loaded
            print self.cache.get()
            >>> 'Hello'


Standalone Usage
----------------
You can also use the Cacher classes as standalones rather than within colifrapy's architecture.

.. code-block:: python

    from colifrapy import LineCacher, YAMLCacher

    line_cache = LineCacher(options)
    yaml_cache = YAMLCacher(options)

Note that cachers are also singletons.

Modes
-----

Line Cacher
^^^^^^^^^^^
The Line Cacher consists in a strict one-liner file and is aimed at storing really simple data.

Example of cache file content

.. code-block:: bash

    1245

YAML Cacher
^^^^^^^^^^^
The YAML Cacher is designed to store more complex states of data and organized in a key-value fashion. The readability of the YAML file format makes the cache file easy to manually modify if needed. This is also possible to create deep nested data structures that will be accessible by paths.

Example of cache file content

.. code-block:: yaml

    number_of_tries: 14
    countries:
        albania: True
        united_kingdom: "Hello"


Options
-------

.. |br| raw:: html

   <br />

Here are the possible options you may pass to the Cacher classes constructors :

   - **directory**
        (string) |br|
        directory where you want to store your cache |br|
        *default*: "cache/"

   - **filename**
        (string) |br|
        name of the cache file |br|
        *default*: "cache.txt" or "cache.yml"

   - **auto_write**
        (boolean) |br|
        whether you want your cache to be automatically written when changed or not. If set to False, you'll have to write the invoke the cache writing manually. |br|
        *default*: False

Methods
-------

Line Cacher
^^^^^^^^^^^

.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

        # Setting cache
        self.cache.set('Hello')

        # Getting cache
        print self.cache.get()
        >>> 'Hello'

        # Writing to cache
        # N.B. : Useless if auto_write is set to True
        self.cache.write()


        # Reading and writing filters
        # Example of a single date cached
        date_format = "%Y/%m/%d %H:%M:%S"
        self.cache.setReadingFilter(lambda x: datetime.strptime(x, date_format))
        self.cache.setWritingFilter(lambda x: x.strftime(date_format))


YAML Cacher
^^^^^^^^^^^

.. code-block:: python

    from colifrapy import Model

    class MyModel(Model):
        def test(self):

            # Setting cache
            self.cache.set("one", "red")
            self.cache.set("two:deep", "blue")

            # Getting cache
            self.cache.get("one")
            >>> "red"

            self.cache.get("two")
            >>> {"deep" : "blue"}

            self.cache.get("two:deep")
            >>> "blue"

            self.cache.get()
            >>> {"one" : "red", {"deep" : "blue"}}

            # Writing to cache
            self.cache.write()
