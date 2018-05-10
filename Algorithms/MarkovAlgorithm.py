from collections import OrderedDict


class MarkovAlgorithm:

	def __init__(self, rules: OrderedDict):
		self.rules = rules
		self.input_string = None

	def run_instruction(self):
		restart = False
		for key, value in self.rules.items():
			copy = self.input_string.replace(key, value, 1)
			if copy is not self.input_string:
				self.input_string = copy
				if '.' not in value:
					restart = True
				break
		return restart

	def transform(self, input_string):
		self.input_string = '@' + input_string + '@'
		restart = True
		while restart:
			restart = self.run_instruction()
			self.input_string = self.input_string.replace('@', '')
		return self.input_string.replace('.', '', 1)
