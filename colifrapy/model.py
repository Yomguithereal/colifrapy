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

# Main Class
#=============
class Model():

	log = Logger()
	opts = Commander().opts
	settings = None