# -------------------------------------------------------------------
# Colifrapy Command Line Hub
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
from settings import Settings
from commander import Commander
from logger import Logger

# Main Class
#=============
class Colifrapy:
    
    log = None
    opts = None
    controller = None
    settings = None

    def __init__(self, controller, settings_path=None):

        # Loading Settings
        self.settings = Settings()
        self.settings.load(settings_path)

        # Loading Opts
        command = Commander()
        self.opts = command.opts

        # Logger just in case
        self.log = Logger()

        # Loading Controller
        self.controller = controller()