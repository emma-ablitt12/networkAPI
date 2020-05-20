# setup

import socket
import json

class User:

	def __init__(self, config_file):
		# constructor

		self.config_file = config_file

		with open(self.config_file) as cf_file:
			cf = json.load(cf_file)


			# taking the info from the config file
			# network

			self.host = config["network_settings"]["host"]
			self.port = config["network_settings"]["port"]

			# dispenser settings

			self.maximum_capacity = config["dispenser_settings"]["maximum_capacity"]
			self.minimum_capacity = config["dispenser_settings"]["minimum_capacity"]
			self.single_dispense = config["dispenser_settings"]["single_dispense"]
			self.min_notify_amount = config["dispenser_settings"]["min_notify_amount"]

		settings = []

		settings.append("Network settings")
		settings.append("Host: {}".format(self.host))
		settings.append("Port: {}".format(self.port))
		settings.append("Dispenser settings")
		settings.append("Maximum minimum_capacity: {}ml".format(self.maximum_capacity))
		settings.append("Minimum_capacity: {}ml".format(self.minimum_capacity))	
		settings.append("Single dispense: {}ml".format(self.single_dispense))
		settings.append("Minimum notify: {}ml".format(self.min_notify_amount))
		print("\n".join(settings))

if __name__ == '__main__':
	test_user = User("config_file.json")




