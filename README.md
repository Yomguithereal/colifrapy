#Colifrapy

##Description
Colifrapy is a Command Line Framework for Python.
Its aim is to provide several tools to build robust and
structured command line tools very easily.

##Installation
It is recommanded to use colifrapy under a python virtualenv.
To install, just type :

```
pip install git+https://github.com/Yomguithereal/colifrapy.git
```

##Philosophy
The goal of colifrapy is to load a yaml configuration file which
is going to manage several settings such as your command line arguments,
version name and if needed, your contextual settings.

Once those settings are loaded, you can call upon colifrapy models to do the
work while remaining able to access critical utilities such as argv opts, settings 
and logger.

##Usage

###Settings
The Settings class is the first thing you will have to import to use Colifrapy.
It has to load your yaml settings file to perform its magic.

Example of settings.yml file:
```yaml
test
```


###Command

###Model

###Logger and strings

###Bonus

##Dependancies
	pyyaml

##License
Colifrapy is under a MIT license.
