from unittest import TestCase as Example

from Algorithms.RAMMachine import *


class TestRAMMachine(Example):

	program = [
		LOAD(10, '='),
		SUB(1, '=', 'loop'),
		STORE(1),
		WRITE(1),
		JGTZ('loop'),
		HALT()
	]

	def test_run(self):
		RAMMachine(self.program).exec()


def run(suite):
	suite.addTest(TestRAMMachine('test_run'))
