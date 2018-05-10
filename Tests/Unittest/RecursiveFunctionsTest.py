import math
import random

from unittest import TestCase

from Algorithms.RecursiveFunctions import *


class TestRecursiveFunctions(TestCase):

	x = 17 % 7 + 3  # formula of finding x: (sequence_number mod 7) + 3

	def test_inc(self):
		for i in range(50):
			y = random.randrange(0, 500)
			self.assertEqual(y + 1, inc(y))

	def test_dec(self):
		for i in range(50):
			y = random.randrange(0, 500)
			self.assertEqual(y - 1, dec(y))

	def test_f_plus(self):
		for i in range(500):
			y = random.randrange(0, 500)
			self.assertEqual(self.x + y, f_plus(self.x, y))

	def test_f_minus(self):
		for i in range(500):
			y = random.randrange(0, 500)
			self.assertEqual(self.x - y, f_minus(self.x, y))

	def test_f_minimum(self):
		for i in range(500):
			y = random.randrange(0, 500)
			self.assertEqual(min(self.x, y), f_minimum(self.x, y))

	def test_f_maximum(self):
		for i in range(500):
			y = random.randrange(0, 500)
			self.assertEqual(max(self.x, y), f_maximum(self.x, y))

	def test_f_modulus(self):
		for i in range(500):
			y = random.randrange(0, 500)
			self.assertEqual(abs(self.x - y), f_modulus(self.x, y))

	def test_f_remaining(self):
		for i in range(500):
			y = random.randrange(1, 500)
			self.assertEqual(self.x % y, f_remaining(self.x, y))

	def test_f_fraction(self):
		for i in range(500):
			y = random.randrange(1, 500)
			self.assertEqual(self.x // y, f_fraction(self.x, y))

	def test_f_multiply(self):
		for i in range(50):
			y = random.randrange(0, 160)
			self.assertEqual(self.x * y, f_multiply(self.x, y))

	def test_f_factorial(self):
		self.assertEqual(math.factorial(self.x), f_factorial(self.x))

	def test_f_power(self):
		for i in range(50):
			y = random.randrange(0, 3)
			self.assertEqual(self.x ** y, f_power(self.x, y))


def run(suite):
	suite.addTest(TestRecursiveFunctions('test_inc'))
	suite.addTest(TestRecursiveFunctions('test_dec'))
	suite.addTest(TestRecursiveFunctions('test_f_plus'))
	suite.addTest(TestRecursiveFunctions('test_f_minus'))
	suite.addTest(TestRecursiveFunctions('test_f_minimum'))
	suite.addTest(TestRecursiveFunctions('test_f_maximum'))
	suite.addTest(TestRecursiveFunctions('test_f_modulus'))
	suite.addTest(TestRecursiveFunctions('test_f_remaining'))
	suite.addTest(TestRecursiveFunctions('test_f_fraction'))
	suite.addTest(TestRecursiveFunctions('test_f_multiply'))
	suite.addTest(TestRecursiveFunctions('test_f_factorial'))
	suite.addTest(TestRecursiveFunctions('test_f_power'))
