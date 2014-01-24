# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Colifrapy Commander Functional Tests
# -------------------------------------------------------------------
#
#
#   Author : Guillaume PLIQUE
#   Version : 0.1.0
import sys
import yaml
from colifrapy import Commander

# Faking argv
sys.argv = [sys.argv[0]] + 'second -a test'.split(' ')

sub_settings = open('tests/resources/subparsers-settings.yml', 'r').read()
sub_arguments = yaml.load(sub_settings)['arguments']

# Testing subparsers
c = Commander()
c.config(arguments=sub_arguments, subhelp='subcommands')
print c.opts
c.subparsers['second'].print_help()
