# -------------------------------------------------------------------
# {{project}} Settings
# -------------------------------------------------------------------
#
#{{author_line}}{{organization_line}}
#   Version: 0.1.0

# Basic Informations
version: '{{project}} 0.1.0'
description: 'Description of the program.'
usage: 'How to deal with your program'
prog: {{project}}
arguments:
- [ ['-t', '--test'], {'help': 'Test', 'type': 'int'} ]
- [ ['positionnal'], {'choices': ['test']} ]

# Logger Settings
logger:
    strings: 'config/strings.yml'
    flavor: 'default'

# Generic Settings
settings:
    hello: 'world'
    bonjour: 'test'
