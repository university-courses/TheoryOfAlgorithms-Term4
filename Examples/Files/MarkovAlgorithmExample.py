from collections import OrderedDict

from unittest import TestCase as Example

from Algorithms.MarkovAlgorithm import MarkovAlgorithm


class TestMarkovAlgorithm(Example):

	input_data = [
		{
			'title': 'Multiplication',
			'input_string': '|||*||',
			'output_string': '||||||',
			'rules': OrderedDict([
				('b|', '|b'),
				('a|', '|ba'),
				('a', '@'),
				('|*', '*a'),
				('*|', '*'),
				('*', '@'),
				('b', '|')
			])
		},
		{
			'title': 'Duplicate word',
			'input_string': 'aaa',
			'output_string': 'aaaaaa',
			'rules': OrderedDict([
				('@a', '*a'),
				('*a', 'aa*'),
				('*', '.@')
			])
		},
		{
			'title': 'Delete duplicated spaces',
			'input_string': 'aab__cca_bcb__cca__aa__ba_bcb',
			'output_string': 'aab_cca_bcb_cca_aa_ba_bcb',
			'rules': OrderedDict([
				('__', '_'),
				('a@', 'a.@'),
				('b@', 'b.@'),
				('c@', 'c.@')
			]),
		},
		{
			'title': 'Expression of type > 2x+3y',
			'input_string': '2*|||+3*||||',
			'output_string': '||||||||||||||||||',
			'rules': OrderedDict([
				('2*|', '||2*'),
				('3*|', '|||3*'),
				('|2*', '|@'),
				('|3*', '|@'),
				('|+|', '||+'),
				('|+', '|.@')
			]),
		}
	]

	def test_transform(self):
		for data in self.input_data:
			markov = MarkovAlgorithm(rules=data['rules'])
			self.assertEqual(markov.transform(data['input_string']), data['output_string'])


def run(suite):
	suite.addTest(TestMarkovAlgorithm('test_transform'))
