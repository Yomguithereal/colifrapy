#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------
# {{project}} Command Line Hub
# -------------------------------------------------------------------
#
#
#   Author : {{author}}
#   Version : 1.0

# Dependencies
#=============
from colifrapy import Settings, Commander
from model.controller import Controller

# Loading Colifrapy
settings = Settings()
settings.load()
command = Commander()

# Launching Controller
controller = Controller()