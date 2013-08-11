# -------------------------------------------------------------------
# Colifrapy Cacher Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import os
import yaml
from .tools.decorators import singleton


# Main Class
#=============
class Cacher:

    # Generic properties
    cache = None
    path = 'config'

    def __init__(self, path=None):

        # Initializing directory in case it does not exists
        if self.path is not None:
            self.path = path.rstrip('/')

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


# Line Cacher
#=============
class LineCacher(Cacher):
    # get write set stream etc.