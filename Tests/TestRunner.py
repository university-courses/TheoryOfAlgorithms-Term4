import unittest

from .Unittest import (
	PostMachineTest,
	TuringMachineTest,
	MarkovAlgorithmTest,
	HamiltonianCycleTest,
	RecursiveFunctionsTest
)


def run():
	suite = unittest.TestSuite()

	PostMachineTest.run(suite)
	TuringMachineTest.run(suite)
	MarkovAlgorithmTest.run(suite)
	HamiltonianCycleTest.run(suite)
	RecursiveFunctionsTest.run(suite)

	unittest.TextTestRunner().run(suite)
