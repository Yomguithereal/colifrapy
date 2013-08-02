#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------
# {{project}} Command Line Hub
# -------------------------------------------------------------------
#
#{{author_line}}
#   Version : 1.0

# Dependencies
#=============
from colifrapy import Colifrapy
from model.controller import Controller

# Hub
#======
class {{project}}(Colifrapy):
    
    def launch(self):

        # Welcoming visitors
        self.log.header('main:title')

        # Calling upon the controller
        self.controller.test()

# Launching
#===========
if __name__ == '__main__':
    hub = {{project}}(Controller)
    hub.launch()