class PostMachine:

	def __init__(self, commands):
		self.__available_commands = [
			'->',  # move the caret to the right for 1 cell
			'<-',  # move the caret to the left for 1 cell
			'V',   # replace 0 into 1
			'E',   # replace 1 into 0
			'?',   # if-else statement ['?', i, j]: if cell is 0 than run command 'a', else - run command 'b'
			'!'	   # terminates program
		]
		self.__validate_commands(commands)
		self.__commands = commands
		self.__caret_position = 0
		self.__operations_count = 0

	def __validate_commands(self, commands):
		has_terminal_command = False
		for command in commands:
			if command[0] not in self.__available_commands:
				raise KeyError('command "{}" does not exist'.format(command[0]))
			if command[0] == '!':
				has_terminal_command = True
		if not has_terminal_command:
			raise KeyError('machine does not contain terminal command')

	def __execute_command(self, commands, string):
		new = list(string)
		next_command = 1
		current_command_index = next_command
		while True:
			current_command = commands[current_command_index - 1][0]
			next_command = commands[current_command_index - 1][1]
			if current_command == '->':
				if self.__caret_position < len(string):
					self.__caret_position += 1
			elif current_command == '<-':
				if self.__caret_position >= 0:
					self.__caret_position -= 1
			elif current_command == 'V':
				new[self.__caret_position] = '1'
			elif current_command == 'E':
				new[self.__caret_position] = '0'
			elif current_command == '?':
				if new[self.__caret_position] == '1':
					next_command = commands[current_command_index - 1][2]
			elif current_command == '!':
				break
			else:
				raise KeyError('command "{}" does not exist'.format(commands[next_command - 1][0]))
			self.__operations_count += 1
			current_command_index = next_command
		return ''.join(new)

	def transform_line(self, input_line, start_pos=0, indent=0):
		if indent < 0:
			indent = 0
		if start_pos < 0:
			start_pos = 0
		self.__caret_position = start_pos + indent
		string = ('0' * indent) + input_line + ('0' * indent)
		return self.__execute_command(self.__commands, string)

	@property
	def operations_ran(self):
		return self.__operations_count
