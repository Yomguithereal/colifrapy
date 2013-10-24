# -------------------------------------------------------------------
# {{project}} Settings
# -------------------------------------------------------------------
#
#{{author_line}}{{organization_line}}
#   Version : 0.1.0

# Basic Informations
version: '{{project}} 0.1.0'
description: 'Description of the program.'
usage: 'How to deal with your program'
arguments:
- [ ['-t', '--test'], {'help' : 'Test', 'type' : 'int'} ]
- [ ['positionnal'], {'choices' : ['test']}]

# Logger Settings
logger:
    strings: 'config/strings.yml'
    flavor: 'default'
    title_flavor: 'default'
    # Delete the path line not to write the log to a file
    directory: 'logs'
    # Log filename, defaults to 'log.txt'
    filename: 'archive.log'
    # Logging mode to file (simple, overwrite or rotation)
    mode: 'simple'
    threshold: ['DEBUG', 'ERROR', 'INFO', 'WARNING', 'VERBOSE']

# Generic Settings
settings:
    hello: 'world'
    bonjour: 'test'