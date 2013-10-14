# -------------------------------------------------------------------
# Colifrapy Command Line Hub
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
from .settings import Settings
from .commander import Commander
from .logger import Logger

# Main Class
#=============
class Colifrapy:
    """ The Colifrapy class is the main project hub. Its aim is to load
    the project's settings and analyze the arguments passed to it in order
    to call the relevant controller methods. """


    log = None
    opts = None
    controller = None
    settings = None
    cache = None

    def __init__(self, controller=None, settings_path='config/settings.yml'):

        # Loading Settings
        settings_instance = Settings()
        settings_instance.load(settings_path)
        self.settings = settings_instance.accessSettingsDict()

        # Loading Opts
        command = Commander()
        self.opts = command.opts

        # Logger just in case
        self.log = Logger()

        # Cache just in case
        self.cache = settings_instance.accessCache()

        # Loading Controller
        if controller is not None:
            self.controller = controller()

            # Triggering default action
            try:
                self.opts.colifrapy_action
            except AttributeError:
                pass
            else:
                if hasattr(self.controller, self.opts.colifrapy_action):
                    getattr(self.controller, self.opts.colifrapy_action)()