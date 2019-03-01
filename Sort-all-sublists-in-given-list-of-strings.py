'''
Sort all sublists in given list of strings
Input:
lst = [['Machine', 'London', 'Canada', 'France'],
       ['Spain', 'Munich'],
       ['Australia', 'Mandi']]

Output:
flist = [['Canada', 'France', 'London', 'Machine'],
         ['Munich', 'Spain'],
         ['Australia', 'Mandi']]
'''

class App:

	lst = [['Machine', 'London', 'Canada', 'France'],
       	['Spain', 'Munich'],
       	['Australia', 'Mandi']]

	def __init__(self,lst):
		self.lst = lst

	def process(self):
		for x in range(0, len(self.lst)):
			for y in self.lst[x]:
				print('y {}'.format(y))


if __name__ == '__main__':
	app = App([['Machine', 'London', 'Canada', 'France'],
       	['Spain', 'Munich'],
       	['Australia', 'Mandi']])
	app.process()
				
			
				
			
			
			
		
		
