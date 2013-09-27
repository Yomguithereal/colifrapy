.. colifrapy documentation master file, created by
   sphinx-quickstart on Thu Sep 19 17:27:11 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Colifrapy
=========

Colifrapy is a **Command Line Framework for Python**.
Its aim is to provide several tools to build robust and
structured command line tools very easily.

Its logic is very similar to a MVC framework and is therefore easy to use.

Philosophy
==========
As every framework, colifrapy aims at enable you to work immediately on critical and intersting parts of
your code that will tackle the problems you need to solve instead of battling with petty
things such as the console output, your settings and the arguments passed to your tool.

However, colifrapy is not a tyrant and does not force you to go its way. As such, every part of colifrapy can
be used on its own and you will remain free to code the way you want to.

Concept
=======
When using colifrapy, your tool is called through a command line hub which acts more or less like a router which will call upon a controller using one or several models to perform the job.

Your hub has therefore the task to load a yaml configuration file containing your command line
arguments, name, version and even contextual settings if you need to.

Once those settings are loaded, every part of your application (mainly models) will remain able to access critical
utilities such as argv opts, settings and make use of colifrapy's logger to ouptut nicely to the console and to log files.

So, schematically colifrapy is:

    Settings --> Command Line Hub --> Controller --> Model + Model + Model etc...

Every bit of colifrapy can be used as a standalone.

    - Logger (outputs to console)
    - Settings (deals with your yml settings)
    - Commander (deals with argv)
    - Cacher (saves data to file)


Summary
=======

.. toctree::
   :maxdepth: 2

   installation