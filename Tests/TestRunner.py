import unittest

from .Unittest import PostMachineTest, MarkovAlgorithmTest, RecursiveFunctionsTest, HamiltonianCycleTest


def run():
	suite = unittest.TestSuite()
	PostMachineTest.run(suite)
	MarkovAlgorithmTest.run(suite)
	RecursiveFunctionsTest.run(suite)
	HamiltonianCycleTest.run(suite)
	unittest.TextTestRunner().run(suite)
