from unittest import TestCase as Example

from Algorithms.PostMachine import PostMachine


class TestPostMachine(Example):

	command_list = [
		['E', 2],  	   # 1
		['->', 3],     # 2
		['?', 4, 5],   # 4
		['V', 6],  	   # 5
		['->', 3],     # 6
		['->', 7],     # 7
		['?', 9, 8],   # 8
		['!', None],   # 9
		['<-', 10],    # 10
		['?', 11, 9],  # 11
		['->', 1],     # 12
	]

	def test_transform(self):
		post_machine = PostMachine(self.command_list)
		self.assertEqual(post_machine.transform_line('1100011'), '0001111')
		self.assertEqual(post_machine.transform_line('111111000000000000011'), '000000000000011111111')


def run(suite):
	suite.addTest(TestPostMachine('test_transform'))
