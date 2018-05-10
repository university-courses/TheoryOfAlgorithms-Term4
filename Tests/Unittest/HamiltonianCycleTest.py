from unittest import TestCase

from Algorithms.HamiltonianCycle import HamiltonianCycle


class TestHamiltonianCycle(TestCase):

	h_cycle = HamiltonianCycle({
		1: [4, 5],
		2: [5],
		3: [4],
		4: [1, 3, 5],
		5: [1, 2, 4]
	})

	def test_find_path(self):
		self.assertEqual(self.h_cycle.find_path(1, 5), [1, 4, 5])

	def test_find_all_paths(self):
		self.assertEqual(self.h_cycle.find_all_paths(1, 5), [[1, 4, 5], [1, 5]])

	def test_find_shortest_path(self):
		self.assertEqual(self.h_cycle.find_shortest_path(1, 5), [1, 5])


def run(suite):
	suite.addTest(TestHamiltonianCycle('test_find_path'))
	suite.addTest(TestHamiltonianCycle('test_find_all_paths'))
	suite.addTest(TestHamiltonianCycle('test_find_shortest_path'))
