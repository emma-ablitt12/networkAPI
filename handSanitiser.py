#connecting the actual dispenser with the network server

#contains the settings the actual hand sanitiser obides by

#capacity in terms of ml

class HandSanitiser:

	def __init__(self, 
				 dispenser_id,
				 maximum_capacity,
				 minimum_capacity,
				 config_file,
				 single_dispense
				 )

	# dispenser id == int, distinguish each dispenser
	# maximum_capacity == int, in terms of ml, how much the dispenser can hold
	# minimum_capacity = int, in terms of ml, the lowest the dispenser 
	#										      can go before refill
	# config_file == string, containing the path to the json file containing the numbers used
	# single_dispense == int, in terms of ml, how much is dispensed each time dispenser
	#																			is used

	#constuctors
	self.dispenser_id = dispenser_id
	self.maximum_capacity = maximum_capacity
	self.minimum_capacity = minimum_capacity
	self.config_file = config_file


	#setters
	def set_single_dispense(self, quantity):
			if not 0 < quantity < self.maximum_capacity:
				print("Programming error.")
			else:
				self.single_dispense = quantity