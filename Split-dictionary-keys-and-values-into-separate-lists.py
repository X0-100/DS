#	intial_dictionary {'a': 'akshat', 'b': 'bhuvan', 'c': 'chandan'}
#	keys :  dict_keys(['a', 'b', 'c'])
#	values :  dict_values(['akshat', 'bhuvan', 'chandan'])


class App:
	initial_dictionary  = {}
	keys = []
	values = []


	def __init__(self,initial_dictionary, keys, values):
		self.initial_dictionary = initial_dictionary
		self.keys = keys
		self.values = values

	
	def process_keys(self):
		for key in self.initial_dictionary:
			self.keys.append(key)
	
	def print_keys(self):
		print 'keys : dict_keys({})'.format(self.keys)
		

	def process_values(self):
    		for key in self.initial_dictionary:
        		self.values.append(self.initial_dictionary[key])  

	def print_values(self):
		print 'values : dict_values({})'.format(self.values)
    			
      
if __name__ == '__main__':
	app = App({'a': 'akshat', 'b': 'bhuvan', 'c': 'chandan'},[],[])
	app.process_keys()
	app.print_keys()
	app.process_values()
	app.print_values()
	
