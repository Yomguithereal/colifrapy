# -------------------------------------------------------------------
# Command line tool Settings
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependancies
#=============
import yaml
from tools.decorators import singleton

# Main Class
#=============
@singleton
class Settings():

	# Loading external data
	def load(self, yaml_file):
		with open(yaml_file, 'r') as yf:
			data = yaml.load(yf.read())
		for i in data:
			setattr(self, i, data[i])