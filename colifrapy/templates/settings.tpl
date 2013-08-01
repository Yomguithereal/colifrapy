# -------------------------------------------------------------------
# {{project}} Settings
# -------------------------------------------------------------------
#
#{{author_line}}
#   Version : 1.0

# Basic Informations
version: '{{project}} 0.1'
description: 'Description of the program.'
arguments: 
- [ ['-t', '--test'], {'help' : 'Test', 'type' : 'int'} ]
- [ ['positionnal'] ]

# Logger Settings
logger:
    strings: 'config/strings.yml'
    path: 'logs'
    threshold: ['DEBUG', 'ERROR', 'INFO', 'WARNING', 'VERBOSE']

# Generic Settings
settings:
    hello: 'world'
    bonjour: 'test'