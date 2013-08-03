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

	# From this hub, you can access several things :
	#    self.settings (Settings Instance)
	#    self.log (Logger Instance)
	#    self.opts (Options passed to your hub)
	#    self.controller (Your Controller)

    # If you really want to use a constructor for this class,
    # do not forget to call the parent's one
    # Colifrapy.__init__() with your controller if you want one.

    def launch(self):

        # Welcoming visitors
        self.log.header('main:title')
        self.log.write('main:hub')

        # Calling upon the controller
        self.controller.test()

# Launching
#===========
if __name__ == '__main__':

    # Pass a second argument to the constructor with the location of your settings.yml
    # if you want it to load from anywhere else than config/settings.yml
    hub = {{project}}(Controller)
    hub.launch()