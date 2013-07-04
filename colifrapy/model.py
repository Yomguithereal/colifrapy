# -------------------------------------------------------------------
# Command line tool Model
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependancies
#=============
from logger import Logger
from commander import Commander
from settings import Settings

# Main Class
#=============
class Model():

    # Helper Properties
    log = Logger()
    settings = Settings()
    opts = Commander().opts
