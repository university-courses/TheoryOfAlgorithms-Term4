from collections import OrderedDict


class MarkovAlgorithm:

	def __init__(self, rules: OrderedDict):
		self.__rules = rules
		self.__input_string = None

	def __run_instruction(self):
		restart = False
		for key, value in self.__rules.items():
			copy = self.__input_string.replace(key, value, 1)
			if copy is not self.__input_string:
				self.__input_string = copy
				if '.' not in value:
					restart = True
				break
		return restart

	def transform(self, input_string):
		self.__input_string = '@' + input_string + '@'
		restart = True
		while restart:
			restart = self.__run_instruction()
			self.__input_string = self.__input_string.replace('@', '')
		return self.__input_string.replace('.', '', 1)
