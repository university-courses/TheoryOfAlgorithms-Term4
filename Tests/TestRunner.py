import unittest

from .Unittest import PostMachineTest, MarkovAlgorithmTest


def run():
	suite = unittest.TestSuite()
	PostMachineTest.run(suite)
	MarkovAlgorithmTest.run(suite)
	unittest.TextTestRunner().run(suite)
