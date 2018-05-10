import unittest

from .Unittest import PostMachineTest, MarkovAlgorithmTest, RecursiveFunctionsTest


def run():
	suite = unittest.TestSuite()
	PostMachineTest.run(suite)
	MarkovAlgorithmTest.run(suite)
	RecursiveFunctionsTest.run(suite)
	unittest.TextTestRunner().run(suite)
