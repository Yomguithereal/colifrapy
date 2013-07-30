# -------------------------------------------------------------------
# {{project}} Settings
# -------------------------------------------------------------------
#
#
#   Author : {{author}}
#   Version : 1.0

# Basic Informations
version: '{{project}} 0.1'
description: 'Description of the program.'
strings: 'config/strings.yml'
log_path: 'logs'
arguments: 
- [ ['-t', '--test'], {'help' : 'Test', 'type' : 'int'} ]
- [ ['positionnal'] ]

# Generic Settings
settings:
    hello: 'world'
    bonjour: 'test'