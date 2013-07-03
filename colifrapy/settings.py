# -------------------------------------------------------------------
# Command line tool Settings
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependancies
#=============
from tools.decorators import singleton

# Main Class
#=============
@singleton
class Settings():

	# Loading external data
	def load(self, data):
		for i in data:
			setattr(self, i, data[i])