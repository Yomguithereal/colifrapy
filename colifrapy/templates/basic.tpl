#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
# {{project}} Command Line Hub
# -------------------------------------------------------------------
#
#{{author_line}}{{organization_line}}
#   Version: 0.1.0

# Dependencies
#=============
from colifrapy import Colifrapy
from model.controller import Controller


# Hub
#====
class {{project}}(Colifrapy):
    pass

# Launching
#==========
if __name__ == '__main__':

    hub = {{project}}(Controller)
