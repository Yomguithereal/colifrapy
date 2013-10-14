from setuptools import setup

docstring = """
Colifrapy
=========

Colifrapy is a **Command Line Framework for Python**.
Its aim is to provide several tools to build robust and
structured command line tools very easily.

Its logic is very similar to a MVC framework and is therefore easy to use.

The full documentation is available here_.

.. _here: http://yomguithereal.github.io/colifrapy/


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
arguments, name, version and other contextual settings.

Once those settings are loaded, every part of your application will remain able to access critical
utilities such as argv opts, settings and make use of colifrapy's logger to ouptut nicely to the console and to log files.

So, schematically colifrapy is a YAML configuration file loaded by a command line hub that will call upon
a controller and other models.

Every bit of colifrapy can be used as a standalone.

    - **Logger** (outputs to console)
    - **Settings** (deals with your yml settings)
    - **Commander** (deals with argv)
    - **Cacher** (saves data to file)

Examples
========
My project furuikeya_ is a good example of the usage
of colifrapy since the framework was originally designed for it.

.. _furuikeya: https://github.com/Yomguithereal/furuikeya

Dependencies
============

    - pyyaml
    - argparse

License
=======
Colifrapy is under a MIT license.
"""


setup(name='colifrapy',
      version='0.4.1',
      description='Command Line Framework for Python',
      url='http://yomguithereal.github.io/colifrapy/',
      long_description=docstring,
      author='Yomguithereal',
      license='MIT',
      packages=['colifrapy', 'colifrapy.tools'],
      install_requires=['pyyaml', 'argparse'],
      package_data={'colifrapy' : ['colifrapy/templates/*']},
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      colifrapy=colifrapy.scaffolder:main
      """,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Topic :: Software Development :: Code Generators',
            'Topic :: Software Development :: Libraries :: Application Frameworks'
      ]
)
