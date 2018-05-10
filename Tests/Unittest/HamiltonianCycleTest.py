from unittest import TestCase

from Algorithms.HamiltonianCycle import HamiltonianCycle


class TestHamiltonianCycle(TestCase):

	graph = {
		1: [4, 5],
		2: [5],
		3: [4],
		4: [1, 3, 5],
		5: [1, 2, 4]
	}

	def test_find_path(self):
		h_cycle = HamiltonianCycle()
		self.assertEqual(h_cycle.find_path(self.graph, 1, 5), [1, 4, 5])

	def test_find_all_paths(self):
		h_cycle = HamiltonianCycle()
		self.assertEqual(h_cycle.find_all_paths(self.graph, 1, 5), [[1, 4, 5], [1, 5]])


def run(suite):
	suite.addTest(TestHamiltonianCycle('test_find_path'))
	suite.addTest(TestHamiltonianCycle('test_find_all_paths'))
