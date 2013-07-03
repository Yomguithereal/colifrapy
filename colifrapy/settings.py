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
from logger import Logger
from commander import Commander
from tools.decorators import singleton

# Main Class
#=============
@singleton
class Settings():

	__commander = Commander()
	__logger = Logger()

	# Loading external data
	def load(self, yaml_file):

		# Opening Settings Yaml File
		with open(yaml_file, 'r') as yf:
			data = yaml.load(yf.read())
		
		# Setting Commander
		self.__commander.config(version=data.get('version'), arguments=data.get('arguments', []))

		# Setting Logger
		self.__logger.load_strings(strings=data.get('strings'), output_path=data.get('log_path'), threshold=data.get('log_threshold'))

		# Else
		if 'settings' in data:
			for key in data['settings']:
				setattr(self, key, data['settings'][key])
