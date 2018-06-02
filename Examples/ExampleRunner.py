from unittest import TestSuite as ExampleSuit
from unittest import TextTestRunner as ExampleTestRunner

from Examples.Files import (
	PostMachineExample,
	TuringMachineExample,
	MarkovAlgorithmExample,
	HamiltonianCycleExample,
	RecursiveFunctionsExample,
	RAMMachineExample
)


def run():
	suite = ExampleSuit()

#	PostMachineExample.run(suite)
#	TuringMachineExample.run(suite)
#	MarkovAlgorithmExample.run(suite)
#	HamiltonianCycleExample.run(suite)
#	RecursiveFunctionsExample.run(suite)
	RAMMachineExample.run(suite)

	ExampleTestRunner().run(suite)
