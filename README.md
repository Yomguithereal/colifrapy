#Colifrapy

##Description
Colifrapy is a **Command Line Framework for Python**.

Its aim is to provide several tools to build robust and structured command line tools very easily.

Its logic is very similar to a MVC framework and is therefore easy to use.

The full documentation for the last released version of colifrapy is available [there](http://colifrapy.readthedocs.org/).

The github repository is available [there](https://github.com/Yomguithereal/colifrapy).

##Installation
It is recommanded to use colifrapy under a python virtualenv.

Install it with pip (version up to 0.4.1):

```
pip install colifrapy
```

If you want to use the latest one which is still in development :

```
pip install git+https://github.com/Yomguithereal/colifrapy.git
```

##Philosophy
As every framework, colifrapy enables you to work immediately on critical and intersting parts of your code that will tackle the problems you need to solve instead of battling with petty things such as the console output, your settings and the arguments passed to your tool.

However, colifrapy is not a tyrant and does not force you to go its way. As such, every part of colifrapy can be used on its own and you will remain free to code however you want to.

##Concept
When using colifrapy, your tool is called through a command line hub which acts more or less like a router which will call upon a controller using one or several models to perform the job.

Your hub has therefore the task to load a yaml configuration file containing your command line
arguments, name, version and other contextual settings.

Once those settings are loaded, every part of your application will remain able to access critical
utilities such as argv opts, settings and make use of colifrapy's logger to ouptut nicely to the console and to log files.

So, schematically colifrapy is a YAML configuration file loaded by a command line hub that will call upon
a controller and other models.

Every bit of colifrapy can be used as a standalone.

* **Logger** (outputs to console)
* **Settings** (deals with your yml settings)
* **Commander** (deals with argv)
* **Cacher** (saves data to file)

##Examples
The project [furuikeya](https://github.com/Yomguithereal/furuikeya) is a good usage example of colifrapy since colifrapy was originally designed to help me doing it.

##Dependencies

	argparse
	pyyaml

##License
Colifrapy is under a MIT license.
